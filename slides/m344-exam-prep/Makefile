# Makefile for M344 Exam Preparation Slides

# Variables
TEX_FILE = m344_exam_prep_slides.tex
PDF_FILE = m344_exam_prep_slides.pdf
LATEX = pdflatex

# Default target: compile the slides
all: $(PDF_FILE)

# Compile the LaTeX file (run twice for TOC)
$(PDF_FILE): $(TEX_FILE)
	$(LATEX) $(TEX_FILE)
	$(LATEX) $(TEX_FILE)

# View the PDF
view: $(PDF_FILE)
	@echo "Opening PDF..."
	@if command -v xdg-open > /dev/null; then \
		xdg-open $(PDF_FILE); \
	elif command -v open > /dev/null; then \
		open $(PDF_FILE); \
	else \
		echo "No PDF viewer found. Please open $(PDF_FILE) manually."; \
	fi

# Clean auxiliary files
clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb

# Clean everything including PDF
distclean: clean
	rm -f $(PDF_FILE)

# Rebuild from scratch
rebuild: distclean all

.PHONY: all view clean distclean rebuild
