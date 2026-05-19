""" Level 2 — Still entry, but combined

Show only active agents, sorted by nps_score descending.
From Team B only, show agent_name and aht_seconds.
Filter agents who handled more than 100 calls AND have an NPS above 65. """

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

# 01
sorted_agents = df[df['status'] == 'active'].sort_values('nps_score', ascending=False)
# print(sorted_agents)

# 02
team_b = df[df['team'] == 'Team B'][['agent_name', 'aht_seconds']]
# print(team_b)

# 03
top_agents = df[(df['calls_handled'] > 100) & (df['nps_score'] > 65)]
# print(top_agents)