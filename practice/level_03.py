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

""" Level 3 — New columns (your arithmetic territory)

Create a column fcr_rate = calls_resolved / calls_handled. (This is your First Call Resolution.)
Create a column aht_minutes = aht_seconds / 60.
Create a column unresolved_calls = calls_handled - calls_resolved.
Create fcr_rate, then filter agents whose FCR is below 0.85 — these are your coaching candidates. """

df['fcr_rate'] = df['calls_resolved'] / df['calls_handled']
df['aht_minutes'] = df['aht_seconds'] / 60
df['unresolved_calls'] = df['calls_handled'] - df['calls_resolved']
coachings = df[df['fcr_rate'] < 0.85]
print(df.head())
print(coachings.head())
