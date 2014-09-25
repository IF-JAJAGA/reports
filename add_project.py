#!/usr/bin/env python

import os
import shutil

project_name = input('Enter project\'s name: ')

try:
    os.mkdir(project_name)
except OSError:
    print('This project already exists')
    exit(1)
else:
    header_in = 'header.in'
    footer_in = 'footer.in'
    header = os.path.join(project_name, 'header.html')
    footer = os.path.join(project_name, 'footer.html')
    config = os.path.join(project_name, 'config')
    makefile = os.path.join(project_name, 'Makefile')

    shutil.copyfile(header_in, header)
    shutil.copyfile(footer_in, footer)

    with open(config, 'w') as f:
        f.write('header.html\nfooter.html')
    with open(makefile, 'w') as f:
        f.write('\
\
# This is a generated Makefile for IF-JAJAGA\n\
# Please just manage HTML files and let the magic do the rest.\n\
\n\
# HTML Files:\n\
HTML = $(shell cat config)\n\
\n\
all: '+project_name+'.pdf\n\
\n\
'+project_name+'.pdf: '+project_name+'.html\n\
\t@echo "Compiling PDF..."\n\
\t@weasyprint $^ $@\n\
\n\
'+project_name+'.html: $(HTML)\n\
ifeq ($(strip $(HTML)),)\n\
\t@echo "Error: No file to compile, check config file"\n\
\t@exit 1\n\
else\n\
\t$(shell cat $^ > '+project_name+'.html)\n\
endif\n\
\n\
clean:\n\
\t@rm '+project_name+'.{pdf,html}\n\
\n\
')
