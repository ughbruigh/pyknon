#!/usr/bin/env python

from pyknon.plot import plot2
from pyknon.simplemusic import inversion

n1 = [11, 10, 7]

for x in range(12):
    plot2(n1, inversion(n1, x), "ex-inversion-plot-{0:02}.ps".format(x))

n2 = [1, 3, 7, 9, 4]
plot2(n2, inversion(n2, 9), "ex-inversion-plot.ps")
