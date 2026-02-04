# average_turnaround.py
# This script calculates the average imaging turnaround time

turnaround_times = [30, 45, 25, 60, 40]  # minutes

total_time = sum(turnaround_times)
number_of_cases = len(turnaround_times)

average_time = total_time / number_of_cases

print("Average imaging turnaround time:", average_time, "minutes")
