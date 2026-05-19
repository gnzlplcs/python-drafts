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

""" Level 4 — Mid level: .groupby()
This is the next natural step. It's like a pivot table in Excel.

Calculate the average nps_score per team.
Find the total calls_handled per team.
Get the average aht_seconds per team, sorted lowest to highest.
Count how many agents per team have status == 'active' — filter first, then groupby. """

average_nps = df.groupby('team')['nps_score'].mean()
print(average_nps)

total_calls_handled = df.groupby('team')['calls_handled'].sum()
print(total_calls_handled)

average_aht_secs = df.groupby('team')['aht_seconds'].mean().sort_values()
print(average_aht_secs)

count_active = df[df['status'] == 'active'].groupby('team')['agent_id'].count()
print(count_active)
