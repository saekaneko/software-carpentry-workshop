import pandas as pd
import analyze_mosquito_data_lib_sk as mosquito_lib

filename = "A1_mosquito_data.csv"

data = pd.read_csv(filename)

print data.head()

data["temperature"] = mosquito_lib.fahr_to_celsius(data["temperature"]) #temperature conversion

parameters = mosquito_lib.analyze(data, "A1_mosquito_data.png")
parameters.to_csv("paramters.csv") #why this is not pd.to_csv is beyond me

print parameters