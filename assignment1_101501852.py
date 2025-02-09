"""
Author: Nima Abady
Assignment: #1
"""
from email.policy import default

# String
gym_member = "Alex Alliton"

# Double
preferred_weight_kg = 20.5

# Integer
highest_reps = 25

# Boolean
membership_active = True

# Data Type: String | Tuple
workout_stats = {
    "Alex": (30, 40, 50),
    "Jamie": (40, 50, 60),
    "Adam": (20, 30, 40)
}

workout_stats_temp =  workout_stats.copy()
for person in workout_stats:
    workout_mins = workout_stats_temp.get(person)
    total = 0
    for minutes in workout_mins:
        total += minutes

    person_total1 = person + "_Total"
    workout_stats_temp.update({person_total1: total})


# Data Type: List of Lists
workout_list = []
for person in workout_stats:
    workout_list.append(workout_stats.get(person))

workout_stats = workout_stats_temp

total_yoga_minutes = 0
for minute_list in workout_list:
    for x in minute_list[slice(2)]:
        total_yoga_minutes += x

print(f"Total Yoga and Running Minutes: {total_yoga_minutes}\n")

last_2_weightlifting_minutes = 0
isFirst = True
for minute_list in workout_list:
    if isFirst:
        isFirst = False
        continue

    for x in minute_list[slice(2,3)]:
        last_2_weightlifting_minutes += x

print(f"Last 2 People Weightlifting minutes: {last_2_weightlifting_minutes}\n")

i = 0
for minute_list in workout_list:
    total = 0
    for minutes in minute_list:
        total += minutes

    if total >= 120:
        print("Great job staying active " + list(workout_stats)[i] + "!")

    i += 1


checkingFriend = input("\nEnter your friends name to check if they are in the list: ")

if workout_stats.get(checkingFriend) is not None:
    minutes = workout_stats.get(checkingFriend)
    print(f"{checkingFriend}'s Yoga Minutes: {list(minutes)[0]}")
    print(f"{checkingFriend}'s Running Minutes: {list(minutes)[1]}")
    print(f"{checkingFriend}'s Weight Lifting Minutes: {list(minutes)[2]}")

    total = 0
    for min in minutes:
        total += min

    print(f"{checkingFriend}'s Total Workout Minutes: {total}\n")

else:
    print(f"Friend {checkingFriend} not found in the records.\n")

highest = 0
highest_person = ""
if workout_stats.get("Alex_Total") > highest:
    highest = workout_stats.get("Alex_Total")
    highest_person = list(workout_stats.keys())[0]

if workout_stats.get("Jamie_Total") > highest:
    highest = workout_stats.get("Jamie_Total")
    highest_person = list(workout_stats.keys())[1]

if workout_stats.get("Adam_Total") > highest:
    highest = workout_stats.get("Adam_Total")
    highest_person = list(workout_stats.keys())[2]

print(f"{highest_person} had the most minutes with: {highest}" )

lowest = 100000
lowest_person = {}
if workout_stats.get("Alex_Total") < lowest:
    lowest = workout_stats.get("Alex_Total")
    lowest_person = list(workout_stats)[0]

if workout_stats.get("Jamie_Total") < lowest:
    lowest = workout_stats.get("Jamie_Total")
    lowest_person = list(workout_stats)[1]

if workout_stats.get("Adam_Total") < lowest:
    lowest = workout_stats.get("Adam_Total")
    lowest_person = list(workout_stats)[2]

print(f"{lowest_person} had the least minutes with: {lowest}")