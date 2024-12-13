import random
import datetime

# Define a list of activities
activities = [
    
]

# Specify the meeting details
meeting_date = "2024-12-17"  # Meeting is set for Tuesday
meeting_time = "11:00"  
meeting_activity = 

# Specify the Friday afternoon details
Friday_date = "2024-12-20"
Friday_time = "17:00"
Friday_activity = 
# Define the start of the week (Monday)
start_date = datetime.datetime.strptime("2024-12-16", "%Y-%m-%d")  # Change to the desired start date

# Create a list of days in the week
days_of_week = [(start_date + datetime.timedelta(days=i)).strftime("%A, %Y-%m-%d") for i in range(5)]

# Function to generate the plan for a single day
def generate_daily_plan():
    time_slots = []
    start_time = datetime.datetime.strptime("09:00", "%H:%M")
    end_time = datetime.datetime.strptime("18:00", "%H:%M")
    current_time = start_time
    while current_time < end_time:
        time_slots.append(current_time.strftime("%H:%M"))
        current_time += datetime.timedelta(hours=1)

    # Randomly shuffle the activities (09:00 - 6:00)
    random.shuffle(activities)

   # Choose a random activity and duplicate it 5 times (or more as needed)
    num_duplicates = 5  # Change this to set how many times you want the activity to repeat
    duplicated_activity = random.choice(activities)

    # Add the duplicated activity to the list
    activities_with_duplicates = activities + [duplicated_activity] * (num_duplicates - 1)  # Add extra copies of the chosen activity

    # Shuffle activities including the duplicates
    random.shuffle(activities_with_duplicates)

    # Assign activities to time slots
    daily_plan = []
    for idx, time in enumerate(time_slots):
        if idx < len(activities_with_duplicates):
            if time != "12:00":  # Reserve noon as empty
                if time == "09:00":
                    morning_activities = random.choice(["Candidature","Gerer le Linkedin"])
                    daily_plan.append(f"{time} - {morning_activities}")
                # elif "scripting/code" is in the daily plan, replace it with either "Remise a niveau" or "MEP env"
                elif "scripting/code" in daily_plan:
                    replacement_activity = random.choice(["Remise a niveau", "MEP env"])
                    daily_plan.append(f"{time} - {replacement_activity}")
                else:
                    daily_plan.append(f"{time} - {activities_with_duplicates[idx]}")
            else:
                daily_plan.append(f"{time} - ")  # Leave noon empty
    return daily_plan

# Generate weekly plan
weekly_plan = {}

# Generate daily plans and insert the meeting at the specified time
for day in days_of_week:
    daily_plan = generate_daily_plan()
    
    # Check if today is the meeting day
    if day == f"Tuesday, {meeting_date}":
        # Find the index for the meeting time slot and replace it with the meeting activity
        for i, time in enumerate(daily_plan):
            if time.startswith(meeting_time):
                daily_plan[i] = f"{meeting_time} - {meeting_activity}"
                break
    if day == f"Friday, {Friday_date}":
        for i, time in enumerate(daily_plan):
            if time.startswith(Friday_time):
                daily_plan[i] = f"{Friday_time} - {Friday_activity}"
                break
    weekly_plan[day] = daily_plan

# Format the output as a table with "|" and "-" for borders
output = ""

# Header row with day names
header = "| Time Slot | " + " | ".join(days_of_week) + " |"
output += header + "\n"

# Add separator line
output += "|" + "-" * (len(header) - 2) + "|\n"

# Add the time slots and activities for each day
for i in range(9):  # Since we have 9 time slots (from 9 AM to 5 PM)
    row = f"| {9 + i}:00 "
    for day in days_of_week:
        if i < len(weekly_plan[day]):
            row += f"| {weekly_plan[day][i].split(' - ')[1]:<20} "
    row += "|"
    output += row + "\n"

# Add separator line at the end
output += "|" + "-" * (len(header) - 2) + "|\n"

# Write the output to a file for viewing
with open("weekly_plan_16_au_20_decembre.txt", "w") as file:
    file.write(output)

print("Weekly plan saved to 'weekly_plan__16_au_20_decembre.txt'. You can now open it in NotepadQQ.")

