import csv
from matplotlib import pyplot as plt
from matplotlib import dates as mdates
import matplotlib.ticker as mticker
import numpy as np
from datetime import datetime

months = mdates.MonthLocator()
mon_fmt = mdates.DateFormatter('%b %Y')

def get_weather_pic_of_month():
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


def get_weather_pic_of_year():
    filename = 'sitka_weather_2014.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        header = next(reader)
        # for idx, column in enumerate(header):
        #     print(idx, column)
        dates, highs = [], []
        for row in reader:
            # we cannot use strftime method here, or it will list all dates through out the whole year.
            dates.append(datetime.strptime(row[0], "%Y-%m-%d"))
            highs.append(int(row[1]))

    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red')
    ax = fig.add_subplot(111)
    # make sure all 12 months will be listed, by default it only lists every 2 months.
    ax.xaxis.set_major_locator(months)
    # set month format here
    ax.xaxis.set_major_formatter(mon_fmt)
    # set limitation of x_axis, or it will show Jan 2015 as well
    plt.xlim(dates[0], dates[-1])
    plt.title("Daily high temperatures, 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    # need to set custom rotation after fig.autofmt_xdate(), or it will be overridden
    # for label in ax.xaxis.get_ticklabels():
    #     label.set_rotation('vertical')
    plt.xticks(rotation=50)
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

get_weather_pic_of_year()