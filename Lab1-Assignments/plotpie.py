import matplotlib
matplotlib.use("TkAgg")

from matplotlib import pyplot

#prepare data
machine_counts = [18, 4, 2]
#prepare label
machine_names = ["PC", "MAC", "Linux"]
#draw pie
pyplot.title("PC vs MAC vs Linux usage")
pyplot.pie(machine_counts, labels = machine_names, autopct="%.1f%%", shadow = True, explode =[0,0.2,0])
pyplot.axis("equal")
#show
pyplot.show()