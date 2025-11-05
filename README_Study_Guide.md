# M344 Final Exam Study Guide

**Prepared by Yolymatics Tutorials**

## About This Document

This comprehensive yet concise study guide has been specially prepared for your M344 final exam. It covers all the essential topics from your course syllabus:

### Topics Covered

1. **Number Theory**
   - Ring of integers modulo n (ℤ/nℤ)
   - Proving the ring axioms
   - Group of units
   - Euler's Theorem & Wilson's Theorem
   - Chinese Remainder Theorem
   - Euler's phi function

2. **Relations**
   - Formal definitions
   - Proving equivalence relations (reflexive, symmetric, transitive)

3. **Linear Congruences**
   - Solving equations: ax ≡ b (mod n)
   - Solvability criteria based on gcd(a,n)
   - Extended Euclidean Algorithm

4. **Combinatorics**
   - Basic counting formulas (with/without repetition, order)
   - Multisets and their applications
   - Multinomial Theorem and coefficients
   - Ordered partitions

5. **Graph Theory**
   - Graph definitions and examples
   - Graph types (complete, path, cycle, bipartite)
   - Testing for bipartite graphs
   - Graph isomorphism
   - Subgraphs, walks, connected graphs, and trees

## File Structure

- `M344_Final_Exam_Study_Guide.tex` - LaTeX source file
- `M344_Final_Exam_Study_Guide.pdf` - Compiled PDF document
- `Makefile` - Build automation

## How to Use

The PDF is ready to use! It features:
- Color-coded boxes for definitions (blue), theorems (green), examples (orange), and tips (purple)
- Clear step-by-step procedures
- Quick reference formulas
- Concise explanations perfect for last-minute review

## Compiling from Source

If you need to modify or rebuild the PDF:

```bash
# Build the PDF
make

# View the PDF
make view

# Clean auxiliary files
make clean

# Clean everything including PDF
make cleanall

# Rebuild from scratch
make rebuild
```

Or compile directly with pdflatex:
```bash
pdflatex M344_Final_Exam_Study_Guide.tex
pdflatex M344_Final_Exam_Study_Guide.tex  # Run twice for proper formatting
```

## Good Luck!

Remember: You've prepared well. Trust yourself and show what you know!

**Exam Time: 2:00 PM**

---

*Prepared with care by Yolymatics Tutorials*
