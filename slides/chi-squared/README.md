# Chi-Squared Test Slides

**Yolymatics Tutorials**  
www.yolymaticstutorials.com

## Overview

Professional presentation slides covering Chi-Squared tests following standard statistical textbook structure (e.g., Crawshaw and Chambers). Designed for advanced mathematics education with comprehensive examples and practice problems.

## Contents

The slides cover:

1. **Chi-Squared Distribution** (2 slides)
   - Definition and properties
   - Hypothesis testing framework
   - Decision rules and validity conditions

2. **Goodness of Fit Test** (1 slide)
   - Purpose and degrees of freedom
   - Worked example: Genetics ratio (3 slides)

3. **Goodness of Fit: Practice Problems** (5 slides)
   - Fair die test
   - Blood type distribution
   - Uniform distribution
   - Coin fairness test
   - Day of week births

4. **Test of Independence** (1 slide)
   - Contingency tables
   - Expected frequency calculation
   - Worked example: Exercise and health (3 slides)

5. **Independence: Practice Problems** (5 slides)
   - Gender and subject preference
   - Smoking and disease
   - Education and income
   - Age and technology adoption
   - Treatment effectiveness

6. **Chi-Squared Tables** (1 slide)
   - Critical values for multiple significance levels

7. **Summary** (1 slide)

**Total: 26 slides** with 10 substantial practice problems

## Features

✓ **Professional Design**: Madrid theme with custom Yolymatics branding  
✓ **Comprehensive Coverage**: Both goodness of fit and independence tests  
✓ **Worked Examples**: Step-by-step solutions with full calculations  
✓ **Practice Problems**: 5 problems per test type (10 total)  
✓ **Clean Workspaces**: Blank areas without annotations for student work  
✓ **Statistical Tables**: Complete critical value reference  
✓ **Professional Footer**: Branding on every slide  

## Building the PDF

### Prerequisites

LaTeX distribution required:
- **Linux**: `sudo apt-get install texlive-latex-base texlive-latex-extra`
- **Mac**: Install MacTeX
- **Windows**: Install MiKTeX or TeX Live

### Compilation

Using the Makefile:

```bash
make              # Build PDF
make view         # Build and view
make clean        # Remove auxiliary files
make cleanall     # Remove all generated files
make rebuild      # Clean and rebuild
```

Or compile manually:

```bash
pdflatex chi_squared_slides.tex
pdflatex chi_squared_slides.tex  # Run twice for TOC
```

## Customization

Edit `chi_squared_slides.tex` to:
- Modify color scheme (see preamble color definitions)
- Add more practice problems
- Adjust slide content
- Change branding elements

Rebuild after changes using `make`

## Practice Problems Summary

**Goodness of Fit (5 problems):**
1. Fair die test (300 rolls)
2. Blood type distribution (500 people)
3. Uniform distribution (5 categories)
4. Coin fairness (200 tosses)
5. Birth distribution (7 days)

**Test of Independence (5 problems):**
6. Gender and subject preference (3×2 table)
7. Smoking and lung disease (2×2 table)
8. Education and income (3×3 table)
9. Age and technology (3×2 table)
10. Treatment effectiveness (2×3 table)

All problems include realistic data and appropriate significance levels.

## Contact

**Yolymatics Tutorials**  
www.yolymaticstutorials.com

---

*Professional Mathematics Education*
