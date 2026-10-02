#!/usr/bin/env python3
"""Draw the actual polytope, an illustrative smoothing and the barrier.

Dependencies: numpy and matplotlib. Transverse coordinates are rescaled by
epsilon. The displayed delta is illustrative, not a certified counterexample.
"""
from pathlib import Path
import math

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

ROOT = Path(__file__).resolve().parent
EPSILON = 1e-12
DELTA = 0.08
A = np.array([(1,0,0),(-1,0,0),(0,0,1),(0,0,-1),(0,-1,0),
              (0,.1,.9),(0,.1,-.9),(.9,.1,0),(-.9,.1,0)])
VERTICES = np.array([(x,y,z) for x in (-1,1) for y in (-1,1)
                     for z in (-1,1)] + [(0,10,0)])


def faces():
    result = []
    for normal in A:
        points = VERTICES[np.isclose(VERTICES @ normal, 1)]
        assert len(points) >= 3
        center = points.mean(axis=0)
        u = points[0] - center
        u /= np.linalg.norm(u)
        v = np.cross(normal, u)
        v /= np.linalg.norm(v)
        order = np.argsort(np.arctan2((points-center) @ v, (points-center) @ u))
        result.append(points[order])
    return result


def smooth_surface():
    # Solve Phi_delta(r theta) = 1 in rescaled coordinates. The quadratic
    # term uses PHYSICAL coordinates (x, epsilon*y, epsilon*z).
    phi = np.linspace(0, 2*np.pi, 241)
    theta = np.linspace(0, np.pi, 161)
    ph, th = np.meshgrid(phi, theta)
    direction = np.stack((np.sin(th)*np.cos(ph), np.sin(th)*np.sin(ph),
                          np.cos(th)), axis=-1)
    dots = direction @ A.T
    right = 1 / dots.max(axis=-1)
    left = np.zeros_like(right)
    norm2 = direction[...,0]**2 + EPSILON**2 * np.sum(direction[...,1:]**2, axis=-1)
    for _ in range(70):
        radius = (left+right)/2
        values = radius[...,None]*dots
        maximum = values.max(axis=-1)
        gauge = maximum + DELTA*np.log(np.exp((values-maximum[...,None])/DELTA).sum(axis=-1))
        gauge += DELTA*radius**2*norm2
        below = gauge < 1
        left = np.where(below, radius, left)
        right = np.where(below, right, radius)
    points = ((left+right)/2)[...,None]*direction
    return points


def setup_3d(ax):
    ax.set_xlabel(r'$x$', labelpad=2)
    ax.set_ylabel(r'$z_1/\varepsilon$', labelpad=3)
    ax.set_zlabel(r'$z_2/\varepsilon$', labelpad=2)
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,10)
    ax.set_zlim(-1,1)
    ax.set_xticks([-1,0,1])
    ax.set_yticks([0,5,10])
    ax.set_zticks([-1,0,1])
    ax.set_box_aspect((2,4,1.6))
    ax.view_init(elev=23, azim=-52)
    ax.tick_params(labelsize=8, pad=0)


def main():
    plt.rcParams.update({'font.size':10, 'font.family':'DejaVu Sans', 'svg.fonttype':'none'})
    fig = plt.figure(figsize=(11,7.6), layout='constrained')
    grid = fig.add_gridspec(2,2, height_ratios=[1.45,1])
    ax = fig.add_subplot(grid[0,0], projection='3d')
    ax.add_collection3d(Poly3DCollection(faces(), facecolor='#aed5df',
                                       edgecolor='#234b63', linewidth=.9, alpha=.55))
    setup_3d(ax)
    ax.set_title('Convex starting polytope', pad=8, fontweight='bold')
    ax = fig.add_subplot(grid[0,1], projection='3d')
    points = smooth_surface()
    ax.plot_surface(points[...,0], points[...,1], points[...,2], color='#d69b54',
                    edgecolor='none', rcount=161, ccount=241, alpha=.97, rasterized=True)
    setup_3d(ax)
    ax.set_title(r'Smooth family: illustrative $\delta=0.08$', pad=8, fontweight='bold')
    ax = fig.add_subplot(grid[1,:])
    x = np.linspace(-1,1,801)
    t = 1-np.abs(x)
    p = (8+(2*math.sqrt(82)-2)*t)/(4+18*t-9*t*t)
    ax.axvspan(-.25,.25, color='#fae6ce', label=r'Central slab $|x|\leq 1/4$')
    ax.plot(x,p,color='#234b63',linewidth=2.2,label=r'$p(1-|x|)$')
    k = 2*math.sqrt(82)-2
    tstar = (-144+math.sqrt(144**2-4*9*k*(4*k-144)))/(18*k)
    xstar = 1-tstar
    minimum = (8+k*tstar)/(4+18*tstar-9*tstar*tstar)
    ax.scatter([-xstar,xstar],[minimum,minimum],color='#a45d21',zorder=5)
    ax.axhline(1.6,color='#a45d21',ls='--',linewidth=1.2,label=r'Barrier bound $8/5$')
    ax.set(xlim=(-1,1),ylim=(1.4,2.04),xlabel=r'Axial coordinate $x$',
           ylabel='Fiber perimeter / area')
    ax.set_title('Two transverse-energy wells separated by a central barrier',fontweight='bold')
    ax.grid(alpha=.18)
    ax.legend(loc='upper center',ncol=3,frameon=False,fontsize=9)
    fig.suptitle(r'Positive Robin gap construction: $\alpha=1$, $\varepsilon=10^{-12}$',fontsize=14)
    fig.supxlabel('Transverse axes are enlarged by 10^12. The drawn smoothing is illustrative; its spectral gap is not certified.',fontsize=9)
    fig.savefig(ROOT/'domain.svg',bbox_inches='tight')
    svg = ROOT/'domain.svg'
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n', encoding='utf-8')
    fig.savefig(ROOT/'domain.png',dpi=180,bbox_inches='tight')
    plt.close(fig)

    # Standalone TeX source: embed vector drawing commands, no external
    # image dependencies in the built-in LaTeX editor.
    project = lambda p: (1.25*p[0]+.35*p[1], .25*p[1]+.55*p[2])
    coords = lambda p: '('+','.join(f'{v:.5f}' for v in p)+')'
    lines = [r'\begin{figure}[tb]',r'\centering',r'\begin{tikzpicture}[scale=0.9]']
    for face in sorted(faces(),key=lambda f:f[:,2].mean()):
        path = ' -- '.join(coords(project(point)) for point in face)
        lines.append(r'\draw[fill=cyan!12,fill opacity=.4,draw=black!65,line width=.5pt] '+path+' -- cycle;')
    lines += [r'\node[align=center] at (1,3.6) {Starting polytope\\$(x,z_1/\varepsilon,z_2/\varepsilon)$};',
              r'\begin{scope}[shift={(5.6,-.9)}]',r'\draw[->] (0,0) -- (6,0) node[right] {$x$};',
              r'\draw[->] (0,0) -- (0,4.4) node[above] {$p(1-|x|)$};',
              r'\fill[orange!15] (2.15625,0) rectangle (3.59375,4);']
    curve = [(2.875*(xx+1),6*((8+k*(1-abs(xx)))/(4+18*(1-abs(xx))-9*(1-abs(xx))**2)-1.4))
             for xx in np.linspace(-1,1,161)]
    lines.append(r'\draw[blue!60!black,thick] plot coordinates {'+' '.join(coords(point) for point in curve)+'};')
    lines += [r'\draw[orange!70!black,dashed] (0,1.2) -- (5.75,1.2);',
              r'\node[left] at (0,1.2) {$8/5$};',r'\node[left] at (0,3.6) {$2$};',
              r'\node[below] at (0,0) {$-1$};',r'\node[below] at (2.875,0) {$0$};',
              r'\node[below] at (5.75,0) {$1$};',r'\end{scope}',r'\end{tikzpicture}',
              r'\caption{The convex polytope is shown with transverse coordinates rescaled by $\varepsilon^{-1}$; it is not drawn at physical aspect ratio. The right panel shows the two minima of the fiber perimeter-to-area ratio and the central slab (shaded). The smooth counterexample is a sufficiently small member of the explicit family in Section~\ref{sec:smoothing}.}',
              r'\label{fig:domain}',r'\end{figure}']
    tex = ROOT/'robin_gap_021.tex'
    text = tex.read_text(encoding='utf-8')
    begin = '% BEGIN GENERATED DOMAIN FIGURE'
    end = '% END GENERATED DOMAIN FIGURE'
    figure = begin+'\n'+'\n'.join(lines)+'\n'+end+'\n'
    if begin in text:
        start = text.index(begin)
        stop = text.index(end,start)+len(end)+1
        text = text[:start]+figure+text[stop:]
    else:
        marker = r'\section{A uniform small-parameter Robin estimate on every fiber}'
        text = text.replace(marker,figure+'\n'+marker)
    tex.write_text(text,encoding='utf-8')
    print('Wrote domain.svg, domain.png and an embedded vector figure in the manuscript.')


if __name__ == '__main__':
    main()
