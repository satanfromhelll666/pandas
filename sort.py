pk.sort_values(['Name'], ascending=True) # sort all data ascending order

pk.sort_values(['Name'], ascending=False)#sort all data desending order

# we can take maltuiple value

pk.sort_values(['Name','HP'],ascending = [1,0]) #1 = true and 0 = false

pk['Total'] = pk['HP'] + pk['Attack'] + pk['Defense'] + pk['Sp. Atk'] + pk['Sp. Def'] + pk['Speed']

pk.head(5)#create a columnb named Total all the sum of parameter 

pk['Total'] = pk.iloc[:,4:10].sum(axis=1) #here add a total columb total add 4 to 9 columnb and axis = 1 means create a columnb if it axis =  0 it will create a row


