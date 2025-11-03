# Makefile for Improper Integrals Slides
# Yolymatics Tutorials - www.yolymaticstutorials.com

# Variables
LATEX = pdflatex
MAIN = improper_integrals_slides
SRC = $(MAIN).tex
PDF = $(MAIN).pdf

# Default target
all: $(PDF)

# Build the PDF
$(PDF): $(SRC)
	@echo "Compiling $(MAIN)..."
	$(LATEX) $(SRC)
	$(LATEX) $(SRC)
	@echo "✓ Compilation complete: $(PDF)"

# View the PDF
view: $(PDF)
	@if command -v xdg-open > /dev/null; then \
		xdg-open $(PDF); \
	elif command -v open > /dev/null; then \
		open $(PDF); \
	else \
		echo "Cannot find a PDF viewer"; \
	fi

# Clean auxiliary files
clean:
	@echo "Cleaning auxiliary files..."
	@rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb
	@echo "✓ Cleanup complete"

# Clean all generated files including PDF
cleanall: clean
	@echo "Removing PDF..."
	@rm -f $(PDF)
	@echo "✓ All generated files removed"

# Rebuild from scratch
rebuild: cleanall all

# Help target
help:
	@echo "Available targets:"
	@echo "  make          - Build the PDF (default)"
	@echo "  make view     - Build and view the PDF"
	@echo "  make clean    - Remove auxiliary files"
	@echo "  make cleanall - Remove all generated files including PDF"
	@echo "  make rebuild  - Clean and rebuild from scratch"
	@echo "  make help     - Show this help message"

.PHONY: all view clean cleanall rebuild help
