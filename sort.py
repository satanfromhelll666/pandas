pk.sort_values(['Name'], ascending=True) # sort all data ascending order

pk.sort_values(['Name'], ascending=False)#sort all data desending order

# we can take maltuiple value

pk.sort_values(['Name','HP'],ascending = [1,0]) #1 = true and 0 = false

pk['Total'] = pk['HP'] + pk['Attack'] + pk['Defense'] + pk['Sp. Atk'] + pk['Sp. Def'] + pk['Speed']

pk.head(5)#create a columnb named Total all the sum of parameter 
