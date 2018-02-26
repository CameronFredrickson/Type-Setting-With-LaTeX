# python code to generate a random walk in TikZ

import random

directions = [(1,0), (-1,0), (0,1), (0,-1)]

steps = 2000

tikz =  "\\begin{tikzpicture}[scale = .1]\n"
tikz += "\draw [black!10] (-50,-50) grid (50,50);\n"
tikz += "\draw [->] (-51,0) -- (51,0);\n"
tikz += "\draw [->] (0,-51) -- (0,51);\n"
tikz += "\draw [ultra thick, red] (0,0)"
for i in range(steps):
    tikz += " -- ++" + str(random.choice(directions))
tikz += ";\n\end{tikzpicture}"

print(tikz)
