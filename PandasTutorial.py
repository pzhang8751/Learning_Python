import numpy as np
import matplotlib.pyplot as pyplot
from datetime import datetime
import os

event_types = ['Rain', 'Thunderstorm', 'Snow', 'Fog']
num_events = len(event_types)

def event2int(event):
    return event_types.index(event)

def date2int(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    return date.toordinal()

def r_squared(actual, ideal):
    actual_mean = np.mean(actual)
    ideal_dev = np.sum([(val - actual_mean)**2 for val in ideal])
    actual_dev = np.sum([(val - actual_mean)**2 for val in actual])

    return ideal_dev / actual_dev

def read_weather(file_name):
    dtypes = np.dtype({ 'names' : ('timestamp', 'max temp', 'mean temp', 'min temp', 'events'),
                        'formats' : [np.int, np.float, np.float, np.float, 'S100'] })

    data = np.loadtxt(file_name, delimiter=',', skiprows=1,
            converters = { 0 : date2int },
            usecols=(0,1,2,3,21), dtype=dtypes)

    return data


def temp_plot(dates, mean_temps, min_temps = None, max_temps = None):

    year_start = datetime(2012, 1, 1)
    days = np.array([(d - year_start).days + 1 for d in dates])

    fig = pyplot.figure()
    pyplot.title('Temperatures in Bloomington 2012')
    pyplot.ylabel('Mean Temperature (F)')
    pyplot.xlabel('Day of Year')

    if (max_temps is None or min_temps is None):
        # Normal plot without error bars
        pyplot.plot(days, mean_temps, marker='o')
    else:
        # Compute min/max temperature difference from the mean
        temp_err = np.row_stack((mean_temps - min_temps,
                                 max_temps - mean_temps))

        # Make line plot with error bars to show temperature range
        pyplot.errorbar(days, mean_temps, marker='o', yerr=temp_err)
        pyplot.title('Temperatures in Bloomington 2012 (max/min)')

    slope, intercept = np.polyfit(days, mean_temps, 1)
    ideal_temps = intercept + (slope * days)
    r_sq = r_squared(mean_temps, ideal_temps)

    fit_label = 'Linear fit ({0:.2f})'.format(slope)
    pyplot.plot(days, ideal_temps, color='red', linestyle='--', label=fit_label)
    pyplot.annotate('r^2 = {0:2f}'.format(r_sq), (0.05, 0.9), xycoords='axes fraction')
    pyplot.legend(loc='lower right')

    return fig

data = read_weather('data/weather.csv')
min_temps = data['min temp']
mean_temps = data['mean temp']
max_temps = data['max temp']
dates = [datetime.fromordinal(d) for d in data['timestamp']]
events = data['events']

if not os.path.exists('plots'):
    os.mkdir('plots')