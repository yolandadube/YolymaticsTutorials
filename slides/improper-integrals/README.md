# Improper Integrals Slides

Professional presentation slides on **Improper Integrals** created for Yolymatics Tutorials.

## 📋 Overview

This presentation covers the theory and practice of improper integrals, including both Type 1 (infinite limits) and Type 2 (infinite discontinuities) problems. The slides are designed for interactive teaching with blank working spaces for live problem-solving.

## 🎯 Features

- **Professional Design**: Custom Yolymatics color scheme and branding
- **Comprehensive Theory**: Clear explanations of improper integral types, convergence, and divergence
- **Practice Problems**: 16 carefully selected problems covering all major topics
- **Working Spaces**: Blank slides after each problem for stylus-based live teaching
- **Reference Materials**: Important formulas, convergence tests, and useful results
- **No Worked Solutions**: Students work through problems with instructor guidance

## 📚 Content Structure

### Theory Sections
1. **Introduction to Improper Integrals**
   - Definitions and types
   - Type 1: Infinite limits
   - Type 2: Infinite discontinuities
   - Convergence and divergence

2. **Reference Formulas**
   - p-integrals for both types
   - Common convergent integrals
   - Comparison tests

### Practice Problems (16 Total)

#### Type 1: Infinite Limits (7 problems)
1. Basic upper limit infinite: $\int_1^{\infty} \frac{1}{x^2}\,dx$
2. Divergent integral: $\int_1^{\infty} \frac{1}{x}\,dx$
3. Exponential decay: $\int_0^{\infty} e^{-3x}\,dx$
4. Lower limit infinite: $\int_{-\infty}^0 e^{2x}\,dx$
5. Both limits infinite: $\int_{-\infty}^{\infty} \frac{1}{1+x^2}\,dx$
6. p-integral analysis: $\int_2^{\infty} \frac{1}{x^p}\,dx$
7. Trigonometric (divergent): $\int_0^{\infty} \sin(x)\,dx$

#### Type 2: Infinite Discontinuities (5 problems)
8. Discontinuity at upper limit: $\int_0^1 \frac{1}{\sqrt{1-x}}\,dx$
9. Discontinuity at lower limit: $\int_0^1 \frac{1}{\sqrt{x}}\,dx$
10. Interior discontinuity: $\int_0^3 \frac{1}{x-1}\,dx$
11. Logarithmic integrand: $\int_0^1 \ln(x)\,dx$
12. Power function: $\int_0^4 \frac{1}{x^{2/3}}\,dx$

#### Mixed and Advanced Problems (4 problems)
13. Both types combined: $\int_0^{\infty} \frac{1}{\sqrt{x}(1+x)}\,dx$
14. Comparison test: $\int_1^{\infty} \frac{1+\sin^2(x)}{x^2}\,dx$
15. Integration by parts: $\int_0^{\infty} x^2 e^{-x}\,dx$
16. Partial fractions: $\int_2^{\infty} \frac{1}{x^2-1}\,dx$

## 🛠️ Compilation

### Prerequisites
- LaTeX distribution (TeX Live, MiKTeX, or MacTeX)
- pdflatex compiler

### Build Commands

```bash
# Compile the slides
make

# Compile and view
make view

# Clean auxiliary files
make clean

# Remove all generated files
make cleanall

# Rebuild from scratch
make rebuild
```

### Manual Compilation
```bash
pdflatex improper_integrals_slides.tex
pdflatex improper_integrals_slides.tex  # Run twice for table of contents
```

## 📖 Usage

These slides are designed for:
- Interactive classroom teaching
- Live problem-solving with a stylus or pen
- Student practice and review
- Homework assignment reference

Each problem is followed by a blank "Working Space" slide for:
- Live calculations during lectures
- Step-by-step solution development
- Student participation
- Clear presentation of solution methods

## 📧 Contact

**Yolymatics Tutorials**  
Website: www.yolymaticstutorials.com

## 📄 License

© 2025 Yolymatics Tutorials. All rights reserved.

---

*Professional mathematics education materials for A-Level, university calculus, and advanced mathematics courses.*
