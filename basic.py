import pandas as pd
pk = pd.read_csv('pokemon_data.csv') 

print(pk.columns) # print all columns

print(pk.Name) #print all the name of the colummns

print(pk.Name [0:6]) #print first six element

print(pk[['Name','Type 1','Generation']]) #print name type1 or generation
