pk.loc[pk['Type 1'] == 'Fire'] # print all the Fire pokemon on the type 1 coloum

pk.loc[(pk['Type 1']=='Grass') & (pk['Type 2']=='Ice')] # and oparetion

pk.loc[(pk['Type 1']=='Grass') | (pk['Type 2']=='Ice')] # or oparation

pk.loc[(pk['Type 1']=='Grass') | (pk['Type 2']=='Ice') & (pk["HP"] >70 ) ]

pk.loc[pk['Name'].str.contains('Mega')] # it print all the name of pokemon who contain mega name.

pk.loc[~pk['Name'].str.contains('Mega')] # it will print all the name of pokemon which not contain mega name

pk.loc[pk['Type 1'] == 'Fire','Type 1'] = 'Flamer' # it will change all the Type 1 columb which has fire name trun them into Flammer

pk.loc[pk['Type 1'] == 'Fire','Legendary'] = TRUE #it will change all the Legendary columb which has fire name trun them into TRUE
