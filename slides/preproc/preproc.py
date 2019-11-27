#! /usr/local/bin/python3.7

import os
import sys
import shutil
import string
import pathlib

################################################################

anchor_prefix = r'[//]:# ('
anchor_suffix = ')'

anchor_begin_prefix = anchor_prefix + 'BEGIN'
anchor_end = anchor_prefix + 'END' + anchor_suffix

class g:
    toc_level = 0

def toc():
    g.toc_level += 1
    s = 'template: toc\n\n'
    for i in range(g.toc_level-1):
        s += '### &nbsp;\n\n'
    s += '### >>>>'
    return s

def include_code(fname, ftype):
    if (fname.startswith('~')):
        fname = str(pathlib.Path(fname).expanduser())
    s = '```' + ftype + '\n'
    f = open(fname, 'r')
    s += f.read()
    f.close()
    s += '```'
    return s

def use_template(fname, dt_keyword):
    f = open(fname, 'r')
    t = string.Template(f.read())
    f.close()
    return t.substitute(dt_keyword)

def title_page(title):
    return use_template('./template/title_page.md', dict(title=title))

def toc_page(*ls_section):
    s = ''
    for section in ls_section:
        s += '### ' + section.strip() + '\n\n'
    s = s.strip()
    return use_template('./template/toc_page.md', dict(str_section=s))

def thanks():
    return use_template('./template/thanks.md', dict())

################################################################

fname = sys.argv[1]

assert os.path.isfile(fname)
fin = open(fname, 'r')
ls_line = fin.readlines()
fin.close()

# backup
os.makedirs('.bak', exist_ok=True)
shutil.copy(fname, '.bak')

#===========================================================
# find anchor

class anchor:
    def __init__(self):
        self.begin_idx = 0
        self.end_idx = 0
        self.line = ''

    def __str__(self):
        return self.line

def new_anchor(i, line):
    a = anchor()
    a.begin_idx = i
    a.line = line
    return a


ls_anchor = list()
for (i, line) in enumerate(ls_line):
    line = line.strip()
    if (line.startswith(anchor_prefix) and line.endswith(anchor_suffix)):
        if (line == anchor_end):
            # end of anchor
            assert (ls_anchor[-1].end_idx == 0), ls_anchor[-1]
            ls_anchor[-1].end_idx = i
        elif (line.startswith(anchor_begin_prefix)):
            # begin of anchor
            ls_anchor.append(new_anchor(i, line))


ls_line_type = [''] * len(ls_line)
for a in ls_anchor:
    if (a.end_idx == 0):
        ls_line_type[a.begin_idx] = 'be' # begin+end
    else:
        ls_line_type[a.begin_idx] = 'b'
        ls_line_type[a.end_idx] = 'e'
        for i in range(a.begin_idx+1, a.end_idx):
            ls_line_type[i] = 'c' # content

#===========================================================
# process anchor

def proc_anchor(line):
    c = line[len(anchor_begin_prefix) : -1 * len(anchor_suffix)].strip()
    if (not c.endswith(')')):
        c += '()'
    print('proc_anchor: %s' % c)
    s = eval(c)
    ls_line = s.split('\n')
    ls_line = map(lambda s: s + '\n', ls_line)
    return ls_line

ls_new = list()
for (line, line_type) in zip(ls_line, ls_line_type):
    if (line_type == ''):
        ls_new.append(line)
    elif (line_type in ['be', 'b']):
        ls_new.append(line)
        ls_new += proc_anchor(line.strip())
        ls_new.append(anchor_end + '\n')

#===========================================================

# for line in ls_new:
#     print(line, end='')

# inline replace to the same file
fout = open(fname, 'w')
fout.writelines(ls_new)
fout.close()
