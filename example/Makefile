# This is a generated Makefile for IF-JAJAGA
# Please just manage HTML files and let the magic do the rest.

# HTML Files:
HTML = $(shell cat config)

all: example.pdf

example.pdf: example.out.html
	@echo "Compiling PDF..."
	@weasyprint $^ $@

example.out.html: $(HTML)
ifeq ($(strip $(HTML)),)
	@echo "Error: No file to compile, check config file"
	@exit 1
else
	$(shell cat $^ > example.out.html)
endif

clean:
	@rm example.{pdf,out.html}

