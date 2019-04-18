This is a proof-of-concept implementation of MPI-style message
passing between Mathematica kernels using MathLink.

In contrast to the Parallel` package, which currently offers only
the master/slave or map/reduce paradigm with its quite limited
expressivity, the message passing approach can be helpful when
constructing more complex parallel algorithms.

It turns out that, despite some suggestions in the Parallel`
documentation that slave kernels are not capable of direct
communication with one another, the implementation is actually
quite easy (though it does rely on undocumented behaviour of the
MathLink functions).

This is a slightly updated version of a notebook previously referred
to on MathGroup:

http://forums.wolfram.com/mathgroup/archive/2011/Jun/msg00535.html

