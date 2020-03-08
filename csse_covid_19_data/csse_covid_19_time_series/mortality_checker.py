# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 10:47:45 2020

@author: John Paul
"""

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

df_death = pd.read_csv('time_series_19-covid-Deaths.csv')
df_recovered = pd.read_csv('time_series_19-covid-Recovered.csv')
df_confirmed = pd.read_csv('time_series_19-covid-Confirmed.csv')

# test of code
total_deaths = df_death['3/5/20'].sum()
total_recovered = df_recovered['3/5/20'].sum()

mortality_rate = total_deaths/total_recovered

print(mortality_rate)
#######################################

time_deaths = df_death.sum().tolist()[2:]
time_recovers = df_recovered.sum().tolist()[2:]
time_confirms = df_confirmed.sum().tolist()[2:]

dates = df_death.columns.tolist()[4:]


mortality = []
for x,y in zip(time_deaths,time_confirms):
    mortality.append(x/y)


df_mortality = pd.DataFrame(zip(dates,mortality,time_confirms,time_recovers,time_deaths),
                            columns=['dates', 'mortality_rate', 'confirms', 'recovers', 'deaths'])
plt.figure(figsize=(10,7))
plt.plot(dates, mortality)
plt.title('Mortality Rate')
plt.xticks(rotation=90)
plt.ylabel('%')
plt.xlabel('Dates')
plt.autoscale()

plt.figure(2, figsize=(10,7))
plt.title('Stats')
plt.plot(dates, time_deaths, label='Deaths')
plt.plot(dates, time_recovers, label='Recovered')
plt.plot(dates, time_confirms, label= 'Confirmed')
plt.legend()
plt.xticks(rotation=90)
plt.yticks(np.arange(0,150000, step=5000))
plt.ylabel('stats')
plt.xlabel('Dates')
plt.autoscale()

