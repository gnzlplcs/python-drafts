import pandas as pd

agents = pd.DataFrame({
    'agent_id': [101, 102, 103, 104],
    'name': ['Ana', 'Luis', 'Maria', 'Carlos']
}).set_index('agent_id')  # <-- agent_id es el índice

skills = pd.DataFrame({
    'agent_id': [101, 102, 103, 104],
    'skill': ['Medicare', 'Medicaid', 'Medicare', 'Billing']
})  # <-- agent_id es columna normal

surveys = pd.DataFrame({
    'survey_id': [1, 2, 3, 4, 5],
    'agent_id': [101, 102, 101, 103, 101],
    'score': [9, 7, 10, 6, 8]
}).set_index('survey_id')  # <-- survey_id es el índice

"""
Tasks:
1. Une agents con skills. Uno tiene agent_id como índice, el otro como columna.
2. Al resultado anterior, agrégale los surveys. Piensa bien qué tiene cada lado.
3. Self join: en surveys, une cada encuesta de Ana (101) consigo misma para ver todos los pares de scores posibles. Pista: merge surveys con surveys usando el índice de un lado y la columna agent_id del otro... espera, eso no funciona directamente. Primero resetea el índice.
4. ¿Cuántas encuestas tiene Ana en total según el resultado del self join? """

# task 1
agents_skills = agents.merge(skills, how='inner', left_index=True, right_on='agent_id').set_index('agent_id')

# task 2
agents_skills_surveys = agents_skills.merge(surveys.reset_index(), how='left', left_index=True, right_on='agent_id').set_index('agent_id')

# task 3
self_surveys = surveys.reset_index().merge(surveys.reset_index(), how="inner", on='agent_id', suffixes=['_1st','_2nd'])

# task 4
surveys_ana = self_surveys[self_surveys['agent_id'] == 101]['survey_id_1st'].nunique()