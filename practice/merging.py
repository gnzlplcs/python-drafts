import pandas as pd

agents = pd.DataFrame({
    'agent_id': [101, 102, 103, 104],
    'name': ['Ana', 'Luis', 'Maria', 'Carlos'],
    'skill': ['Medicare', 'Medicaid', 'Medicare', 'Billing']
})

surveys = pd.DataFrame({
    'agent_id': [101, 102, 101, 103, 105],
    'score': [9, 7, 10, 6, 8],
    'date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-02']
})

"""
task 1
do an inner join. how many rows you get and why? """
agents_surveys = agents.merge(surveys, how='inner', on='agent_id')
print(agents_surveys.head())

"""
task 2
do an left join. what happens with Carlos? """
agents_surveys_left = agents.merge(surveys, how='left', on='agent_id')
print(agents_surveys_left[agents_surveys_left['name'] == 'Carlos'])

"""
task 3
do an left join from surveys. what happens with the agent 105? """
surveys_agents_left = surveys.merge(agents,how='left', on='agent_id')
print(surveys_agents_left[surveys_agents_left['agent_id'] == 105])


"""
task 4
what is the average score per agent? (inner join + groupby)"""
agents_with_surveys = surveys.merge(agents, on='agent_id', how='inner')
surveys_avg = agents_with_surveys.groupby('name').agg({'score':'mean'})
print(surveys_avg)

"""
task 5
what join would you use if you want to see all the agents even though not to have any surveys?"""
agents_surveys_all = agents.merge(surveys, how='left', on='agent_id')
print(agents_surveys_all.head(10))
