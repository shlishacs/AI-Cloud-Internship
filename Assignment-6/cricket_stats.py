import json
import os
from collections import Counter

# Get the path of the JSON file
json_path = os.path.join(os.path.dirname(__file__), "cricket_data.json")

# Read JSON file
with open(json_path, "r", encoding="utf-8") as file:
    matches = json.load(file)

# Variables
total_runs = 0
total_balls = 0
outs = 0

home_runs = 0
home_matches = 0

away_runs = 0
away_matches = 0

dismissals = []

# Process each match
for match in matches:
    runs = match["runs"]
    balls = match["balls"]
    condition = match["condition"]
    dismissal = match["dismissal"]

    total_runs += runs
    total_balls += balls

    # Count outs
    if dismissal.lower() != "not out":
        outs += 1
        dismissals.append(dismissal)

    # Home/Away performance
    if condition.lower() == "home":
        home_runs += runs
        home_matches += 1

    elif condition.lower() == "away":
        away_runs += runs
        away_matches += 1

# Strike Rate
strike_rate = (total_runs / total_balls) * 100 if total_balls > 0 else 0

# Batting Average
average = total_runs / outs if outs > 0 else total_runs

# Home and Away Average
home_average = home_runs / home_matches if home_matches > 0 else 0
away_average = away_runs / away_matches if away_matches > 0 else 0

# Better Condition
if home_average > away_average:
    better_condition = "Home"
elif away_average > home_average:
    better_condition = "Away"
else:
    better_condition = "Equal"

# Frequent Dismissal
dismissal_counter = Counter(dismissals)

if dismissal_counter:
    frequent = dismissal_counter.most_common(1)[0]
    dismissal_type = frequent[0]
    dismissal_count = frequent[1]
else:
    dismissal_type = "None"
    dismissal_count = 0

# Display Results
print("=" * 55)
print("        SMRITI MANDHANA CRICKET STATS")
print("=" * 55)

print(f"Total Matches           : {len(matches)}")
print(f"Total Runs              : {total_runs}")
print(f"Total Balls Faced       : {total_balls}")
print(f"Strike Rate             : {strike_rate:.2f}")
print(f"Batting Average         : {average:.2f}")

print("\nPerformance by Conditions")
print("-" * 30)
print(f"Home Average            : {home_average:.2f}")
print(f"Away Average            : {away_average:.2f}")
print(f"Better Performance      : {better_condition}")

print("\nDismissal Analysis")
print("-" * 30)
print(f"Most Frequent Dismissal : {dismissal_type}")
print(f"Dismissed               : {dismissal_count} time(s)")