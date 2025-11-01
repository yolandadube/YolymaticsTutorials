# Hypothesis Testing — Yolymatics Tutorials

A beautiful Beamer slide deck covering hypothesis testing: concepts, common tests, power, and examples.

- Slides: `hypothesis_testing_slides.tex`
- Output (after build): `hypothesis_testing_slides.pdf`
- Branding: custom color theme + footer with contact

## Quick build

If you already have LaTeX installed (e.g., TeX Live), you can compile with:

```bash
pdflatex -interaction=nonstopmode -halt-on-error hypothesis_testing_slides.tex
pdflatex -interaction=nonstopmode -halt-on-error hypothesis_testing_slides.tex
```

Or, if you have `latexmk`:

```bash
latexmk -pdf -quiet hypothesis_testing_slides.tex
```

The PDF will appear in this folder.

## Install LaTeX on Ubuntu (minimal set)

```bash
sudo apt-get update
sudo apt-get install -y texlive texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-science latexmk
```

> Note: This repo uses only standard packages: beamer, amsmath, amssymb, lmodern, microtype, siunitx, tikz, hyperref.

## Handout mode (optional)

To generate a simple handout without overlays or navigation, you can temporarily switch the document class to:

```tex
\documentclass[aspectratio=169,professionalfonts,handout]{beamer}
```

…and recompile. Alternatively, duplicate the file to a `*_handout.tex` variant.

## Customize branding

Edit the color definitions at the top of the `.tex` file:

```tex
\definecolor{YolyPrimary}{HTML}{533E85}
\definecolor{YolyAccent}{HTML}{00A8A8}
```

You can also tweak the footline template to change or remove the contact string.
