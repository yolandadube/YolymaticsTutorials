# Makefile for Chi-Squared Test Slides
# Yolymatics Tutorials - www.yolymaticstutorials.com

TEXFILE = chi_squared_slides
PDFLATEX = pdflatex

.PHONY: all clean view

# Default target: build PDF
all: $(TEXFILE).pdf

# Build PDF from LaTeX source
$(TEXFILE).pdf: $(TEXFILE).tex
	$(PDFLATEX) $(TEXFILE).tex
	$(PDFLATEX) $(TEXFILE).tex

# Open the PDF (Linux)
view: $(TEXFILE).pdf
	xdg-open $(TEXFILE).pdf 2>/dev/null || open $(TEXFILE).pdf 2>/dev/null || echo "Please open $(TEXFILE).pdf manually"

# Clean auxiliary files
clean:
	rm -f $(TEXFILE).aux $(TEXFILE).log $(TEXFILE).nav $(TEXFILE).out $(TEXFILE).snm $(TEXFILE).toc $(TEXFILE).vrb

# Clean everything including PDF
cleanall: clean
	rm -f $(TEXFILE).pdf

# Quick rebuild
rebuild: clean all
