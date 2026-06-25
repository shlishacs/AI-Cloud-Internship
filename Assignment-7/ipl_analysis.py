import pandas as pd
import os

# Get the path of the CSV file
csv_path = os.path.join(os.path.dirname(__file__), "ipl_players.csv")

# Read the CSV file
data = pd.read_csv(csv_path)

while True:
    print("\n" + "=" * 60)
    print("               IPL DATASET ANALYSIS")
    print("=" * 60)
    print("1. Show All Player Details")
    print("2. Show Teams and Their Members")
    print("3. Highest Run Scorer")
    print("4. Most Wickets")
    print("5. Best Strike Rate")
    print("6. Search Player")
    print("7. Average Runs by Team")
    print("8. Best All-Rounder")
    print("9. Team with Most Wins")
    print("10. Exit")

    choice = input("\nEnter your choice (1-10): ")

    # 1. Show all player details
    if choice == "1":
        print("\n" + "=" * 60)
        print("ALL PLAYER DETAILS")
        print("=" * 60)
        print(data.to_string(index=False))

    # 2. Show teams and their members
    elif choice == "2":
        print("\n" + "=" * 60)
        print("TEAMS AND THEIR MEMBERS")
        print("=" * 60)

        teams = data.groupby("Team")

        for team, members in teams:
            print(f"\n🏏 {team}")
            print("-" * 40)

            for i, player in enumerate(members["Player_Name"], start=1):
                print(f"{i}. {player}")

    # 3. Highest Run Scorer
    elif choice == "3":
        player = data.loc[data["Runs"].idxmax()]

        print("\nHighest Run Scorer")
        print("-" * 30)
        print("Player :", player["Player_Name"])
        print("Team   :", player["Team"])
        print("Runs   :", player["Runs"])

    # 4. Most Wickets
    elif choice == "4":
        player = data.loc[data["Wickets"].idxmax()]

        print("\nMost Wickets")
        print("-" * 30)
        print("Player  :", player["Player_Name"])
        print("Team    :", player["Team"])
        print("Wickets :", player["Wickets"])

    # 5. Best Strike Rate
    elif choice == "5":
        player = data.loc[data["Strike_Rate"].idxmax()]

        print("\nBest Strike Rate")
        print("-" * 30)
        print("Player      :", player["Player_Name"])
        print("Team        :", player["Team"])
        print("Strike Rate :", player["Strike_Rate"])

    # 6. Search Player
    elif choice == "6":
        name = input("\nEnter Player Name: ")

        player = data[data["Player_Name"].str.lower() == name.lower()]

        if not player.empty:
            print("\nPlayer Details")
            print("-" * 60)
            print(player.to_string(index=False))
        else:
            print("\nPlayer not found!")

    # 7. Average Runs by Team
    elif choice == "7":
        print("\nAverage Runs by Team")
        print("-" * 40)

        avg_runs = data.groupby("Team")["Runs"].mean()

        for team, runs in avg_runs.items():
            print(f"{team:<25} {runs:.2f}")

    # 8. Best All-Rounder
    elif choice == "8":
        data["All_Rounder_Score"] = data["Runs"] + (data["Wickets"] * 20)

        player = data.loc[data["All_Rounder_Score"].idxmax()]

        print("\nBest All-Rounder")
        print("-" * 30)
        print("Player :", player["Player_Name"])
        print("Team   :", player["Team"])
        print("Runs   :", player["Runs"])
        print("Wickets:", player["Wickets"])
        print("Score  :", player["All_Rounder_Score"])

    # 9. Team with Most Wins
    elif choice == "9":
        team_wins = data.groupby("Team")["Team_Wins"].max()

        print("\nTeam Wins")
        print("-" * 30)

        for team, wins in team_wins.items():
            print(f"{team:<25} {wins}")

        print("\nTeam with Most Wins")
        print("-" * 30)
        print("Team :", team_wins.idxmax())
        print("Wins :", team_wins.max())

    # 10. Exit
    elif choice == "10":
        print("\nThank you for using IPL Dataset Analysis!")
        break

    else:
        print("\nInvalid choice! Please enter a number between 1 and 10.")
