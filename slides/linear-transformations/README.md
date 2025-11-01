# Linear Transformations — Yolymatics Tutorials

Professional Beamer slides covering linear transformations in $\mathbb{R}^2$ for first-year university calculus students.

- Slides: `linear_transformations_slides.tex`
- Output (after build): `linear_transformations_slides.pdf`
- Branding: Yolymatics Tutorials with professional blue/amber theme

## Topics covered

1. **Foundations**
   - Definition of linear transformations
   - Matrix representation
   - Properties and composition

2. **Five fundamental transformations**
   - Scaling
   - Reflections
   - Projections
   - Shearing
   - Rotation

3. **Practice problems** (25 problems)
   - Identifying transformations
   - Computing images
   - Composing transformations
   - Finding inverse transformations
   - Geometric interpretation
   - Double workspace pages for each problem

## Quick build

If you have LaTeX installed:

```bash
pdflatex -interaction=nonstopmode -halt-on-error linear_transformations_slides.tex
pdflatex -interaction=nonstopmode -halt-on-error linear_transformations_slides.tex
```

Or with `latexmk`:

```bash
latexmk -pdf -quiet linear_transformations_slides.tex
```

Or use the Makefile:

```bash
make
```

## Install LaTeX on Ubuntu

```bash
sudo apt-get update
sudo apt-get install -y texlive texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended latexmk
```

## Features

- Professional blue/amber color scheme
- Modern geometric design elements
- TikZ diagrams illustrating transformations
- 25 practice problems with double workspace pages
- Clear step-by-step procedures
- Examples at university calculus level
- Ready for tablet/stylus annotation

## Customize branding

Edit color definitions at the top of the `.tex` file:

```tex
\definecolor{YolyPrimary}{HTML}{1E3A8A}
\definecolor{YolyAccent}{HTML}{F59E0B}
```

Contact info in footline can be modified in the `\setbeamertemplate{footline}` section.
