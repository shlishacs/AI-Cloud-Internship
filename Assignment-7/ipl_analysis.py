import pandas as pd
import os

# Get the path of the CSV file
csv_path = os.path.join(os.path.dirname(__file__), "ipl_players.csv")

# Read the CSV file
data = pd.read_csv(csv_path)

print("=" * 50)
print("IPL DATASET ANALYSIS")
print("=" * 50)

# Highest Run Scorer
highest_run_scorer = data.loc[data["Runs"].idxmax()]

print("\nHighest Run Scorer")
print("-------------------------")
print("Player :", highest_run_scorer["Player_Name"])
print("Team   :", highest_run_scorer["Team"])
print("Runs   :", highest_run_scorer["Runs"])

# Most Wickets
most_wickets = data.loc[data["Wickets"].idxmax()]

print("\nMost Wickets")
print("-------------------------")
print("Player   :", most_wickets["Player_Name"])
print("Team     :", most_wickets["Team"])
print("Wickets  :", most_wickets["Wickets"])

# Best Strike Rate
best_sr = data.loc[data["Strike_Rate"].idxmax()]

print("\nBest Strike Rate")
print("-------------------------")
print("Player      :", best_sr["Player_Name"])
print("Team        :", best_sr["Team"])
print("Strike Rate :", best_sr["Strike_Rate"])

# Team with Most Wins
team_wins = data.groupby("Team")["Team_Wins"].max()

best_team = team_wins.idxmax()
wins = team_wins.max()

print("\nTeam with Most Wins")
print("-------------------------")
print("Team :", best_team)
print("Wins :", wins)