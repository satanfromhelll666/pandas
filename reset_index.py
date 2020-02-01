new_pk = pk.loc[(pk['Type 1']=='Rock') | (pk['Type 2']=='Ice') & (pk["HP"] >70 ) ]

new_pk = new_pk.reset_index()

new_pk
