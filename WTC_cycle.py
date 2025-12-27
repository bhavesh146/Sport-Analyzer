import pandas as pd

WTC_2023_25_players = {
    "top_batsmen" : {

    "player_name" : ["JOE Root (ENG)", "Yashashvi Jaiswal (IND)","Ben Duckett (ENG)","Harry Brook (ENG)","Usman Khawaja (AUS)",
                         "Steven Smith (AUS)","Travis Head (AUS)","Zak Crawley (ENG)","Kane Williamson (NZ)","Kamindu Mendis (SL)"],
    
    "matches_played" : [22, 19, 22, 17, 20, 20, 20, 19, 11, 11],
    "innings" : [40, 36, 41, 29, 39, 37, 36, 34, 22, 20],
    "runs" : [1968, 1798, 1470, 1463, 1428, 1403, 1197, 1175, 1152, 1123],
    "highest_score" :["262", "214*", "153", "317", "232", "141", "152", "189", "156", "182*"],
    "avg" : [54.66, 52.88, 36.75, 50.44, 39.66, 41.26, 34.2, 34.55, 54.85, 62.38],
    "ball_faced" : [3006, 2738, 1743, 1755, 3211, 2686, 1483, 1509, 2128, 1702],
    "SR" : [65.46, 65.66, 84.33, 83.36, 44.47, 52.23, 80.71, 77.86, 54.13, 65.98],
    "Century" : [7, 4, 2, 4, 2, 5, 3, 1, 5, 5],
    "half_century" : [7, 10, 8, 7, 6, 5, 5, 8, 4, 3],
    "4s" : [186, 207, 187, 144, 149, 144, 153, 152, 134, 116],
    "6s" : [9, 39, 7, 17, 5, 11, 13, 10, 6, 23]
    },

    "top_10_bowlers" : {
        
        "player_name" : ["Pat Cummins (AUS)", "Jasprit Bumrah (IND)", "Mitchell Starc (AUS)", "Nathan Lyon (AUS)", "Ravichandran Ashwin (IND)",
                          "Josh Hazlewood (AUS)", "Prabhat Jayasuriya (SL)","Kagiso Rabada (SA)","Ravindra Jadeja (IND)","Gus Atkinson (ENG)"],
        "matches_played" : [18, 15, 19, 17, 14, 14, 12, 11, 15, 11 ],
        "innings" : [35, 28, 37, 30, 26, 26, 22, 22, 26, 21],
        "overs_bowled" : [563.5, 393.4, 538, 546.5, 445.3, 393.2, 611.5, 330.3, 418.1, 308.4],
        "maidens" : [76, 91, 81, 76, 61, 88, 79, 64, 70, 52 ],
        "wickets_taken" : [80, 77, 77, 66, 63, 59, 58, 56, 55, 52],
        "BBF" : ["6/28", "6/45", "6/48", "6/65", "7/71", "5/31", "6/42", "6/46", "5/41", "7/45"],
        "avg" : [23.48, 15.09, 26.89, 25.18, 24.55, 20.45, 36.74, 18.73, 23.43, 22.15], 
        "economy" : [3.33, 2.95, 3.84, 3.03, 3.47, 3.06, 3.48, 3.17, 3.08, 3.73],
        "4_wkt_haul" : [4, 5, 4, 6, 1, 3, 2, 1, 1, 2],
        "5_wkt_haul" : [6, 5, 2, 1, 5, 3, 4, 4, 3, 3]

    }
}

df_top_batsmen = pd.DataFrame(WTC_2023_25_players["top_batsmen"])
df_top_10_bowlers = pd.DataFrame(WTC_2023_25_players["top_10_bowlers"])
# print(df_top_batsmen)
# print(df_top_10_bowlers)
df_top_batsmen.to_csv('top_batsmen.csv')
print(df_top_batsmen)
df_top_10_bowlers.to_csv('top_10_bowlers.csv')
print(df_top_10_bowlers)


def top_3_players(df,name_col,innings_col,runs_col, avg_col,highest_score, hundreds_col, half_century_col, sort_by,  higher_is_better=True):

    return df.sort_values(
        by=sort_by,
        ascending=not higher_is_better
    )[[name_col,innings_col,runs_col, avg_col, highest_score, hundreds_col, half_century_col]].head(3)

top_run_scorer = top_3_players(
    df_top_batsmen,
    "player_name",
    "innings",
    "runs",
    "avg",
    "highest_score",
    "Century",
    "half_century",
    sort_by="runs",
    higher_is_better=True
)

top_avg_batsmen = top_3_players(
    df_top_batsmen,
    "player_name",
    "innings",
    "runs",
    "avg",
    "highest_score",
    "Century",
    "half_century",
    sort_by="avg",
    higher_is_better=True
)

highest_individual_score = top_3_players(
    df_top_batsmen,
    "player_name",
    "innings",
    "runs",
    "avg",
    "highest_score",
    "Century",
    "half_century",
    sort_by="highest_score",
    higher_is_better=True
)

Most_Century = top_3_players(
    df_top_batsmen,
    "player_name",
    "innings",
    "runs",
    "avg",
    "highest_score",
    "Century",
    "half_century",
    sort_by="Century",
    higher_is_better=True
)

Most_Half_Century = top_3_players(
    df_top_batsmen,
    "player_name",
    "innings",
    "runs",
    "avg",
    "highest_score",
    "Century",
    "half_century",
    sort_by="half_century",
    higher_is_better=True

)


def top_3_players(df,name_col,innings_col,wickets_taken_col, avg_col, five_wkt_haul, sort_by,  higher_is_better=False):

    return df.sort_values(
        by=sort_by,
        ascending=not higher_is_better
    )[[name_col,innings_col,wickets_taken_col, avg_col,five_wkt_haul]].head(3)

Most_Wickets = top_3_players(
    df_top_10_bowlers,
    "player_name",
    "innings",
    "wickets_taken",
    "avg",
    "5_wkt_haul",
    sort_by="wickets_taken",
    higher_is_better=True
)

Best_Average = top_3_players(
    df_top_10_bowlers,
    "player_name",
    "innings",
    "wickets_taken",
    "avg",
    "5_wkt_haul",
    sort_by="avg",
    higher_is_better=False
)

Most_Fifers = top_3_players(
    df_top_10_bowlers,
    "player_name",
    "innings",
    "wickets_taken",
    "avg",
    "5_wkt_haul",
    sort_by="5_wkt_haul",
    higher_is_better=True
)

while True:
    print("\n--- World Test Championship 2023-25 Records ---")
    print("1. Player with most Runs")
    print("2. Best Average in WTC 23-25")
    print("3. Highest Individual Score of WTC 23-25")
    print("4. Most no. of Century")
    print("5. Most No. of Half Century")
    print("6. Most Wickets in WTC 23-25")
    print("7. Best Average in WTC 23-25")
    print("8. Most 5_wkt_haul")



    choice = int(input("Enter choice: "))

    if choice == 1:
        print(top_run_scorer)
    elif choice == 2:
        print(top_avg_batsmen)
    elif choice == 3:
        print(highest_individual_score)
    elif choice == 4:
        print(Most_Century)
    elif choice == 5:
        print(Most_Half_Century)
    elif choice == 6:
        print(Most_Wickets)
    elif choice == 7:
        print(Best_Average)
    elif choice == 8:
        print(Most_Fifers)
    else:
        print("❌ Invalid choice")