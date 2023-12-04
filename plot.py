import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df=pd.read_csv('multiracial.csv')


# See how much child affinity for culture decreased by by race and gender
father_decrease_by=df.groupby(by='Father Race')\
    .mean(numeric_only=True)\
    ['ΔConnected to Father Culture']

mother_decrease_by=df.groupby(by='Mother Race')\
    .mean(numeric_only=True)\
    ['ΔConnected to Mother Culture']

decrease_by=pd.concat([father_decrease_by, mother_decrease_by], axis=1) #join father_decrease_by and mother_decrease_by on race
print(decrease_by)


# Parent Combos: % Surveyed
# Plot 3D of count of parents and % surveyed
parent_combos=df.groupby(['Father Race', 'Mother Race']).size().reset_index(name='Count')
parent_combos['Percent']=parent_combos['Count']*100/len(df)
parent_combos.sort_values(by='Percent', ascending=False, inplace=True)
print(parent_combos)


parent_combos.to_excel('parent_combos.xlsx')

