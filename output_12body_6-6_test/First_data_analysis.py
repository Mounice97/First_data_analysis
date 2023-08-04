import pandas as pd
import numpy as np
import Data_ploting

data=pd.read_csv('data_analysis_2.csv', sep='\s+', index_col='t')

# =================== List with zero values ===================

col_zeros=[col for col in data.columns if data[col].eq(0).any()]

for i in col_zeros:
    #print(i)
    output=data[i].eq(0).value_counts()
    print(f'The number of zeros is true for: \n {output}')


# =================== Ploting ===================

#Data_ploting.making_plot(data['mdot'])
Data_ploting.making_plot(data.iloc[:,0:2], data['mdot'], data['phi'])