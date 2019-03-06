import csv
from matplotlib import pyplot as plt
import numpy as np
from datetime import datetime

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)
    # for idx, column in enumerate(header):
    #     print(idx, column)
    dates, highs = [], []
    for row in reader:
        dates.append(datetime.strptime(row[0], "%Y-%m-%d").strftime("%B %d %Y"))
        highs.append(int(row[1]))

    fig = plt.figure(dpi=200, figsize=(5, 3))
    plt.plot(dates, highs, c='red')
    ax = fig.add_subplot(111)
    # print(plt.xticks([]))
    # only show 3th x_ticks
    ax.set_xticks(ax.get_xticks()[::3])
    # set frequency for y axis
    plt.yticks(np.arange(round(min(highs))-1, round(max(highs))+2, 2))
    # set limits of axis
    plt.axis([0, 31, round(min(highs))-1, round(max(highs))+1])
    plt.title("Daily high temperatures, July 2014", fontsize=20)
    plt.xlabel('', fontsize=12)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=12)
    plt.show()
