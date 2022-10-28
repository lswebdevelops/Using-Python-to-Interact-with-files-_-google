#!/usr/bin/env python3

minutes_to_automate = 40*60
minutes_taken_per_task = 60
number_of_times_month = 40

if minutes_to_automate <(minutes_taken_per_task * number_of_times_month):
    print("Then automate")
elif minutes_to_automate == (minutes_taken_per_task * number_of_times_month):
    print("it takes the same time")
else:
    print("It's not worth it!")
