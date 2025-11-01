PDF=linear_transformations_slides.pdf
TEX=linear_transformations_slides.tex

all: pdf

pdf:
	@if command -v latexmk >/dev/null 2>&1; then \
		latexmk -pdf -quiet $(TEX); \
	else \
		pdflatex -interaction=nonstopmode -halt-on-error $(TEX); \
		pdflatex -interaction=nonstopmode -halt-on-error $(TEX); \
	fi

clean:
	@rm -f *.aux *.log *.nav *.out *.snm *.toc *.fls *.fdb_latexmk *.synctex* $(PDF)

.PHONY: all pdf clean
