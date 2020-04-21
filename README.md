# eisenstein

A python representation of the Eisenstein Integers

## File structure
```
├── eisenstein-test.py ------------------> EisensteinInt unit tests
├── eisenstein.py -----------------------> EisensteinInt class
├── plot.py -----------------------------> generate sample plots
├── plots -------------------------------> stores the generated plots
└── requirements.txt ---------------------> package requirements
```

# Notes to self
- Figuring out the division algorithm. The problem was figuring out what the floor of a number is in the Eisenstein integers. It is where the norm of the remainder is the smallest.
- Plotting the points. Plotting the points and figuring out the translation in coordinates.
- GCD can be up to units only - as long as it is an associate it is good or you can pick a canonical sextant representation.
- Bug: I was looking for a minimum but returned the element of the last iteration in best_candidate()

# Sources
- http://math.bu.edu/people/jsweinst/Teaching/MA341Spring18/MA341Notes.pdf
- https://proofwiki.org/wiki/Norm_of_Eisenstein_Integer
- https://arxiv.org/pdf/1602.09106.pdf
- https://doi.org/10.1016/j.jsc.2004.02.006
- https://en.wikipedia.org/wiki/Eisenstein_integer
- http://hackage.haskell.org/package/arithmoi-0.8.0.0/docs/Math-NumberTheory-Quadratic-EisensteinIntegers.html
- https://thekeep.eiu.edu/cgi/viewcontent.cgi?article=3459&context=theses
- https://mathworld.wolfram.com/EisensteinPrime.html
- https://stackoverflow.com/questions/28417604/plotting-a-line-from-a-coordinate-with-and-angle
- https://pdfs.semanticscholar.org/f871/a066a9a75bcf3435bc1c5960bd6e6d53502a.pdf
- https://en.wiktionary.org/wiki/Eisenstein_integer#English
