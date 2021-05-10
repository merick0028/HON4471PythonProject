from collections import defaultdict
import csv
from statistics import mean

from matplotlib import pyplot as plt


def get_entries(subjects):
    entries = [defaultdict(list)] * 3
    entries = {
        'IP': defaultdict(list),
        'CON': defaultdict(list),
        'INP': defaultdict(list)
    }
    for subject in subjects:
        for event in subjects[subject]:
            for idx in range(1,326):
                entries[event['condition']][str(idx)].append(event[str(idx)])
    return entries


def show_plot(subjects):
    entries = get_entries(subjects)

    x_ax = []
    for i in range(1, 326):
        x_ax.append(i)

    y_ax = [[], [], []]
    for i in range(1, 326):
        y_ax[0].append(mean(map(float, entries['IP'][str(i)])))
        y_ax[1].append(mean(map(float, entries['CON'][str(i)])))
        y_ax[2].append(mean(map(float, entries['INP'][str(i)])))

    plt.plot(x_ax, y_ax[0])
    plt.plot(x_ax, y_ax[1])
    plt.plot(x_ax, y_ax[2])
    plt.show()


if __name__ == '__main__':
    subjects = defaultdict(list)

    with open('FHfullData.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            subjects[row['subject']].append({
                **{str(idx) : row[str(idx)] for idx in range(1, 326)},
                'condition' : row['condition']
            })

    show_plot(subjects)
