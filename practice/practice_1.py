import pandas as pd
import numpy as np

data = {
    'agente': ['Ana', 'Ana', 'Ana', 'Luis', 'Luis', 'Luis',
               'Marta', 'Marta', 'Marta', 'Carlos', 'Carlos', 'Carlos',
               'Sofia', 'Sofia', 'Sofia', 'Pedro', 'Pedro', 'Pedro'],
    'campana': ['UHC', 'UHC', 'Iberia', 'UHC', 'UHC', 'Iberia',
                'UHC', 'Iberia', 'Iberia', 'UHC', 'UHC', 'Iberia',
                'Ally', 'Ally', 'UHC', 'Aon', 'Aon', 'UHC'],
    'aht': [310, 295, 340, 280, 305, 260,
            420, 390, 410, 300, 315, 295,
            250, 270, 265, 330, 345, 320],
    'llamadas': [45, 50, 38, 60, 55, 62,
                 30, 35, 33, 48, 46, 50,
                 70, 65, 68, 40, 38, 42]
}

df = pd.DataFrame(data)
print(df)

avg_aht = df.groupby('agente')['aht'].mean()
print(avg_aht)

q1 = np.quantile(avg_aht, 0.25)
q3 = np.quantile(avg_aht, 0.75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers = avg_aht[(avg_aht < lower) | (avg_aht > upper)]
print(outliers)
