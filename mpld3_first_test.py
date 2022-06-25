from matplotlib.pyplot import figure
from matplotlib.pyplot import savefig
import mpld3

fig = figure()
ax = fig.gca()
ax.plot([1,2,3,4])

fig.savefig("example_figure.png")
print(mpld3.fig_to_html(fig))
