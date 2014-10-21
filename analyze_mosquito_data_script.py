import pandas as pd
import analyze_mosquito_data_lib_sk as mosquito_lib
import sys

#filename = "A1_mosquito_data.csv"
filename = sys.argv[1] #heading back string

print "ANALYZING"
data = pd.read_csv(filename)

print data.head()

data["temperature"] = mosquito_lib.fahr_to_celsius(data["temperature"]) #temperature conversion

print "RUNNING ANALYZE"
parameters = mosquito_lib.analyze(data, filename.replace("csv","png")) #replace csv in filename with png
parameters.to_csv(filename.replace("data","parameters")) #why this is not pd.to_csv is beyond me

print parameters