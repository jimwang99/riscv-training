#! /usr/bin/env python3.7

import os
import sys
import re
import shutil
import string
import pathlib
import jinja2 as j2

################################################################

class preproc_t:
    def __init__(self, pp_type, tmplt_dpath, src_dpath):
        self.pp_type = pp_type
        assert pp_type in ['bs', 'hugo'], pp_type
        self.tmplt_dpath = tmplt_dpath
        self.src_dpath = src_dpath

        self.toc_level = 0

    def include_template(self, fpath, **kwargs):
        assert os.path.isfile(fpath), fpath
        f = open(fpath, 'r')
        t = string.Template(f.read())
        f.close()
        return t.substitute(kwargs)


    def title_page(self, title):
        return self.include_template(os.path.join(self.tmplt_dpath, 'title_page.md'), title=title)


    def toc_page(self, *ls_section):
        s = ''
        for section in ls_section:
            s += '### ' + section.strip() + '\n\n'
        s = s.strip()
        return self.include_template(os.path.join(self.tmplt_dpath, 'toc_page.md'), str_section=s)


    def thanks(self):
        return self.include_template(os.path.join(self.tmplt_dpath, 'thanks.md'))


    def toc(self):
        if (self.pp_type == 'hugo'):
            return ''

        self.toc_level += 1
        s = 'template: toc\n\n'
        for i in range(self.toc_level-1):
            s += '### &nbsp;\n\n'
        s += '### >>>>'
        return s


    def include_code(self, fpath, ftype):
        print(fpath)
        if (fpath.startswith('~')):
            fpath = str(pathlib.Path(fpath).expanduser())
        elif (not fpath.startswith('/')):
            fpath = os.path.join(self.src_dpath, fpath)
        print('->  ' + fpath)

        s = '```' + ftype + '\n'
        f = open(fpath, 'r')
        s += f.read()
        f.close()
        s += '```'
        return s


################################################################

if __name__ == '__main__':
    pp_type = sys.argv[1]
    assert pp_type in ['bs', 'hugo'], pp_type

    if (pp_type == 'bs'):
        tmplt_dpath = './bs/template'
    elif (pp_type == 'hugo'):
        tmplt_dpath = './hugo/template'
    assert os.path.isdir(tmplt_dpath), tmplt_dpath

    src_fpath = sys.argv[2]
    assert os.path.isfile(src_fpath), src_fpath
    output_fpath = sys.argv[3]

    # prepare preproc
    src_dpath = os.path.dirname(src_fpath)
    pp = preproc_t(pp_type, tmplt_dpath, src_dpath)

    # jinja2
    env = j2.Environment(loader=j2.FileSystemLoader('.'))
    for func_name in dir(pp):
        if callable(getattr(pp, func_name)):
            env.globals[func_name] = getattr(pp, func_name)

    result = env.get_template(src_fpath).render()

    # special for hugo
    if (pp_type == 'hugo'):
        new_result = ''
        num_split = 0
        for line in result.split('\n'):
            # skip split lines
            if (line.strip() == '---'):
                num_split += 1
                if (num_split > 2):
                    continue

            # skip duplicated titles
            if (line.strip().startswith('#') and line.strip().endswith('(cont\'d)')):
                continue

            # remove ":scale xx%"
            line = re.sub(r'\[:scale \d+%\]', '[pic]', line)

            # change image to ../image
            line = line.replace('(image/', '(../image/')
            line = line.replace('(./image/', '(../image/')

            # skip special keyword
            if (line.strip().startswith('class:')):
                continue
            if (line.strip().startswith('.col-') or (line.strip() == ']')):
                continue

            new_result += (line + '\n')
        result = new_result

        new_result = ''
        num_empty = 0
        for line in result.split('\n'):
            if (len(line.strip()) == 0):
                num_empty += 1
                if (num_empty > 2):
                    continue
            else:
                num_empty = 0

            new_result += (line + '\n')
        result = new_result

    with open(output_fpath, 'w') as f:
        f.write(result)

    print('** {}: {} -> {} using {}'.format(pp_type, src_fpath, output_fpath, tmplt_dpath))
