import pandas as pd

data = {
    'agent_id': ['A001','A002','A003','A004','A005','A006','A007','A008'],
    'agent_name': ['Rosa','Carlos','Milagros','Jorge','Ana','Luis','Carmen','Pedro'],
    'team': ['Team A','Team B','Team A','Team C','Team B','Team C','Team A','Team B'],
    'calls_handled': [120, 95, 140, 88, 110, 73, 130, 102],
    'calls_resolved': [108, 80, 133, 70, 99, 60, 117, 91],
    'aht_seconds': [310, 420, 290, 510, 380, 490, 305, 360],
    'nps_score': [72, 58, 85, 49, 76, 44, 81, 67],
    'status': ['active','active','active','inactive','active','inactive','active','active']
}

df = pd.DataFrame(data)

# Show only agent_name, team, and nps_score.
data_min = df[['agent_name', 'team', 'nps_score']]

# Filter agents whose nps_score is above 70.
score_over_70 = data_min[data_min['nps_score'] > 70]

# Sort the full dataframe by calls_handled, highest first.
sorted_df = df.sort_values('calls_handled', ascending=False)

# Show only agents from Team A or Team C (use .isin()).
selected_teams = df[df['team'].isin(['Team A', 'Team C'])]

# Filter agents with status == 'active'.
active_agents = df[df['status']=="active"]
