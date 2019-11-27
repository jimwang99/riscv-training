SHELL=/bin/bash

default: preproc

serve:
	bs serve

html:
	bs export --output ./output/html --no-inline

pdf:
	bs pdf --output ./output/pdf --verbose

################################################################

md=$(wildcard *.md)
stamp=$(addprefix .bak/,$(md))

preproc: $(stamp)

.bak/%.md: %.md
	./preproc/preproc.py $<

.PHONY: default serve html pdf preproc
