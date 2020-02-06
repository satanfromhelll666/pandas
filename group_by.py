pk.groupby(['Type 1']).mean() # which columb has number it will agv or mean the all columb without Type 1

pk.groupby(['Type 1']).mean().sort_values('Defense') #it will sort the value according to Defense and also base on mean value

pk.groupby(['Type 1']).mean().sort_values('Sp. Atk' , ascending = False) # it will show the name of the type 1 pokemon which has the highest sp.Atk

pk.groupby(['Type 1']).sum() #it will sum the all numeric coloum 

pk.groupby(['Type 1' , 'Type 2']).count() # here type 1 is bug and type 2 is electric....etc

'''
Bug	
  Electric	2	2	2	2	2	2	2	2	2	2
  Fighting	2	2	2	2	2	2	2	2	2	2
  Fire	2	2	2	2	2	2	2	2	2	2
  Flying	14	14	14	14	14	14	14	14	14	14
  Ghost	1	1	1	1	1	1	1	1	1	1
'''
