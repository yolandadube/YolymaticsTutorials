# Confidence Intervals Slides

**Yolymatics Tutorials**  
www.yolymaticstutorials.com

## Overview

Professional presentation slides covering confidence intervals for statistical inference. Designed for advanced mathematics education with comprehensive theory and practice problems. No worked solutions included—workspace provided for teaching with stylus.

## Contents

The slides cover:

1. **Introduction to Confidence Intervals** (2 slides)
   - Definition and interpretation
   - Confidence levels and trade-offs

2. **Confidence Interval for Population Mean** (3 slides)
   - Known variance (z-distribution)
   - Unknown variance (t-distribution)
   - t-distribution critical values table

3. **Mean CI: Practice Problems** (5 problems + 5 working slides)
   - Battery life (known σ)
   - Student heights (unknown σ)
   - Fuel efficiency
   - Test scores
   - Manufacturing process

4. **Confidence Interval for Population Proportion** (1 slide)
   - Large sample formula and conditions

5. **Proportion CI: Practice Problems** (5 problems + 5 working slides)
   - Voter preference
   - Product defect rate
   - Medical treatment success
   - Student satisfaction
   - Market share

6. **Sample Size Determination** (1 slide)
   - For means and proportions

7. **Sample Size: Practice Problems** (2 problems + 2 working slides)
   - Required sample for mean
   - Required sample for proportion

8. **Confidence Interval for Difference of Means** (1 slide)
   - Independent samples, Welch approximation

9. **Difference of Means: Practice Problems** (2 problems + 2 working slides)
   - Comparing teaching methods
   - Drug efficacy comparison

10. **Confidence Interval for Difference of Proportions** (1 slide)
    - Large sample formula

11. **Difference of Proportions: Practice Problems** (2 problems + 2 working slides)
    - Gender wage gap
    - Treatment comparison

12. **Summary** (2 slides)
    - Formula reference table
    - Key points

**Total: 50 slides** with 16 practice problems

## Features

✓ **Professional Design**: Madrid theme with Yolymatics branding  
✓ **Comprehensive Coverage**: All major CI types (mean, proportion, differences)  
✓ **Theory Slides**: Clear formulas and assumptions  
✓ **16 Practice Problems**: Realistic scenarios across all topics  
✓ **Clean Workspaces**: Blank slides after each problem for stylus teaching  
✓ **No Solutions**: Problems only—you work them with students  
✓ **Reference Tables**: t-distribution and z critical values  
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
pdflatex confidence_intervals_slides.tex
pdflatex confidence_intervals_slides.tex  # Run twice for TOC
```

## Practice Problems Summary

**Population Mean (5 problems):**
1. Battery life with known σ
2. Student heights with unknown σ
3. Fuel efficiency (small sample, 99% CI)
4. Test scores (medium sample, 95% CI)
5. Manufacturing process (large sample, 90% CI)

**Population Proportion (5 problems):**
6. Voter preference survey
7. Product defect rate
8. Medical treatment success (99% CI)
9. Student satisfaction
10. Market share estimation

**Sample Size (2 problems):**
11. Determining sample size for mean estimation
12. Determining sample size for proportion estimation

**Difference of Means (2 problems):**
13. Comparing two teaching methods
14. Drug efficacy comparison

**Difference of Proportions (2 problems):**
15. Gender wage gap analysis
16. Treatment comparison

All problems include realistic data, varied confidence levels (90%, 95%, 99%), and diverse sample sizes.

## Customization

Edit `confidence_intervals_slides.tex` to:
- Modify color scheme (see preamble)
- Add more practice problems
- Adjust slide content
- Change branding elements

Rebuild after changes using `make`

## Contact

**Yolymatics Tutorials**  
www.yolymaticstutorials.com

---

*Professional Mathematics Education*
