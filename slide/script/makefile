SHELL=/bin/bash

preproc=./script/preproc.py

all:
	cd ..; \
	    $(preproc) bs ./script/test.md ./script/bs.md; \
	    $(preproc) hugo ./script/test.md ./script/hugo.md

.PHONY: all cmp
