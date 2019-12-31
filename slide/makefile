SHELL=/bin/bash

default: preproc
.PHONY: default

bs = ~/node_modules/backslide/bin/bs

################################################################

SRC ?= all

ifeq ($(SRC),all)
ls_src = $(wildcard src/*.md)
endif
ifeq ($(SRC),lecture)
ls_src = $(wildcard src/*-lecture.*.md src/00-schedule.md)
endif
ifeq ($(SRC),demo)
ls_src = $(wildcard src/*-demo.*.md)
endif

ls_bs = $(subst src/,bs/,$(ls_src))
ls_bs_tmplt = $(wildcard bs/template/*.md)
ls_hugo = $(subst src/,hugo/,$(ls_src))
ls_hugo_tmplt = $(wildcard hugo/template/*.md)

bs/%.md: src/%.md $(ls_bs_tmplt)
	./script/preproc.py bs $< $@

hugo/%.md: src/%.md $(ls_hugo_tmplt)
	./script/preproc.py hugo $< $@

preproc: $(ls_bs) $(ls_hugo)
.PHONY: preproc

################################################################

serve: preproc
	cd bs; $(bs) serve

html: preproc
	cd bs; $(bs) export --output ../output/html --no-inline

pdf: preproc
	cd bs; $(bs) pdf --output ../output/pdf --verbose
.PHONY: serve html pdf

################################################################

clean:
	-rm -f bs/*.md hugo/*.md
.PHONY: clean
