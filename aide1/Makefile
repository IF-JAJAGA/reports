# This is a generated Makefile for IF-JAJAGA
# Please just manage HTML files and let the magic do the rest.

# HTML Files:
HTML = $(shell cat config)
CSS  = ../reports.css

all: aide1.pdf

aide1.pdf: aide1.out.html
	@echo "Compiling $@..."
	@weasyprint $^ $@ -s $(CSS)

aide1.out.html: $(HTML)
ifeq ($(strip $(HTML)),)
	@echo "Error: No file to compile, check config file"
	@exit 1
else
	@echo "Generating $@..."
	$(shell cat $^ > $@)
endif

clean:
	@rm aide1.{pdf,out.html}
