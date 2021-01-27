#!/usr/bin/env python
# coding: utf-8

# nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# What was the average temperature in first week of Jan
# What was the maximum temperature in first 10 days of Jan
# Figure out data structure that is best for this problem

data = []
with open('nyc_weather.csv', 'r') as f:
    for line in f:
        tokens = line.split(',')
        data.append(float(tokens[1]))

print(data)


# What was the average temperature in first week of Jan
print(sum(data[0:7])/(len(data[0:7])))


# What was the maximum temperature in first 10 days of Jan
print(data[0:10])


print(max(data[0:10]))


# (2) nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# (a) What was the temperature on Jan 9?
# (b) What was the temperature on Jan 4? Figure out data structure that is best for this problem

data = {}
with open('nyc_weather.csv', 'r') as f:
    for line in f:
        tokens = line.split(',')
        data[tokens[0]] = float(tokens[1])


print(data)


# #### What was the temperature on Jan 9

print(data['Jan-09'])


# #### What was the temperature on Jan 4

print(data['Jan-04'])





