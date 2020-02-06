pk.groupby(['Type 1']).mean() # which columb has number it will agv or mean the all columb without Type 1

pk.groupby(['Type 1']).mean().sort_values('Defense') #it will sort the value according to Defense and also base on mean value

pk.groupby(['Type 1']).mean().sort_values('Sp. Atk' , ascending = False) # it will show the name of the type 1 pokemon which has the highest sp.Atk

pk.groupby(['Type 1']).sum() #it will sum the all numeric coloum 
