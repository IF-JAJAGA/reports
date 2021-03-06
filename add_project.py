#!/usr/bin/env python

import os
import shutil
import pystache
import locale
import datetime

project_name = input('Enter project\'s name: ')
project_title = input('Enter report\'s main title: ')
project_subtitle = input('Enter report\'s subtitle (if necessary): ')

if project_title == "":
    project_title = project_name

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
    date = ""
    date_now = datetime.date.today()
    try:
        locale.setlocale(locale.LC_TIME, 'fr_FR.utf8')
        date = str(date_now.day) + ' ' + locale.nl_langinfo(locale.MON_1+(date_now.month-1)) + ' ' + str(date_now.year)
    except locale.Error:
        print('Unable to select french locale, keeping default')
        date = date_now.strftime('%d/%m/%y')

    shutil.copyfile(footer_in, footer)

    with open(header_in,'r') as f:
        with open(header, 'w') as f2:
            f2.write(pystache.render(f.read(), {'title': project_title, 'subtitle': project_subtitle, 'date': date}))
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
CSS = ../reports.css\n\
\n\
all: '+project_name+'.pdf\n\
\n\
'+project_name+'.pdf: '+project_name+'.out.html\n\
\t@echo "Compiling $@..."\n\
\t@weasyprint $^ $@ -s $(CSS)\n\
\n\
'+project_name+'.out.html: $(HTML)\n\
ifeq ($(strip $(HTML)),)\n\
\t@echo "Error: No file to compile, check config file"\n\
\t@exit 1\n\
else\n\
\t@echo "Generating $@..."\n\
\t$(shell cat $^ > $@)\n\
endif\n\
\n\
clean:\n\
\t@rm '+project_name+'.{pdf,out.html}\n\
\n\
')
