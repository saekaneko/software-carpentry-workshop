import pandas as pd
import analyze_mosquito_data_lib_sk as mosquito_lib

filename = "A1_mosquito_data.csv"

data = pd.read_csv(filename)

print data.head()

parameters = mosquito_lib.analyze(data)
print parameters