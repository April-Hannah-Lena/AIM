# Three-center constant-frame holonomy certificate

Let `d>=2`, let `A_1,A_2,A_3` be noncollinear, and let `V_i` be their Voronoi cells. Define

```math
W_i(x)=G(|x-A_i|)\frac{x-A_i}{|x-A_i|},
\qquad R_{ij}=I-2n_{ij}\otimes n_{ij},
\quad n_{ij}=\frac{A_j-A_i}{|A_j-A_i|},
```

where `G(r)>0` for `r>0`. On the pairwise bisector,

```math
W_j=R_{ij}W_i.                                         \tag{C1}
```

Suppose `F=Q_iW_i` on `V_i`, with each `Q_i` invertible. Every pairwise Voronoi face has nonempty relative interior, and the values of `W_i` on that face span `R^d`. Matching Sobolev traces therefore gives

```math
Q_i=Q_jR_{ij}.                                         \tag{C2}
```

The three relations imply

```math
R_{12}R_{23}R_{31}=I.                                 \tag{C3}
```

But `det R_{ij}=-1`, and hence the left side of (C3) has determinant `-1`. Contradiction.

Thus no nonsingular constant frames glue the three radial fields across a noncollinear three-site Voronoi partition. If a pairwise trace is left unmatched, the distributional derivative of `F` contains the surface term

```math
[F]\otimes n\,\mathcal H^{d-1}\!\restriction H_{ij},
```

so `F` is not `H^1_loc`. The obstruction extends verbatim to every odd cycle in the cell-adjacency graph for which the face traces span `R^d`.

Scope: for a field needed only on a fixed `Omega`, a face matters only when it meets `Omega` in positive `(d-1)`-measure. Tree-like active adjacencies, position-dependent frames, singular-frame constructions, and non-Voronoi scalar families are not excluded.
