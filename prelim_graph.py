import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

current_labels = []
current_data = []
coffee_labels = []
coffee_data = []
with open("testing_prelim_results.txt") as res:
    for line in res:
        data = line.split(",")
        if (len(data)==6):
            title = data[0]

            sum=0
            for i in range(1,len(data)):
                sum+=float(data[i])
            for i in range(1,len(data)):
                data[i] = float(data[i])/sum

            if "Current" in title:
                current_labels.append(title[:-19])
                current_data.append(data[1:])
            else:
                coffee_labels.append(title[:-18])
                coffee_data.append(data[1:])

        # else:
            # print("bad data")
            # print(line)

def percentage(x, pos):
    'The two args are the value and tick position'
    return '%2.1f%%' % (x * 100)


formatter = FuncFormatter(percentage)
x = np.array([5,4,3,2,1])
fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(formatter)

colors = ['C2', 'C3', 'C4']
gap = 0.8/len(current_data)
for i in range(len(current_data)):
    plt.bar(x+(i-len(current_data)/2.0)*gap, current_data[i], color=colors[i], width=gap, label=current_labels[i])

plt.vlines([1.367, 3.367],0,0.55, color = 'k', label="Acceptable Range")
plt.title("Output after 3x through the Current Grinder")
plt.xticks([1,2,3,4,5], ["< 0.75", "0.75-1.5", "1.5-3", "3-5", "> 5"])
plt.xlabel("Size of Output [mm]")
plt.ylabel("Output Composition by Weight")
plt.legend()


fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(formatter)

gap = 0.8/len(coffee_data)
for i in range(len(coffee_data)):
    plt.bar(x+(i-len(coffee_data)/2.0)*gap, coffee_data[i], width=gap, label=coffee_labels[i])

plt.vlines([1.367, 3.367],0,0.65, color = 'k', label="Acceptable Range")
plt.title("Output from the Coffee Grinder")
plt.xticks([1,2,3,4,5], ["< 0.75", "0.75-1.5", "1.5-3", "3-5", "> 5"])
plt.xlabel("Size of Output [mm]")
plt.ylabel("Output Composition by Weight")
plt.legend()



plt.show()
