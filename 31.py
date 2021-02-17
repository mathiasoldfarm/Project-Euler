def count_sums(soints, n_coins, amount ): 
    if amount == 0: 
        return 1
  
    if amount < 0 or (n_coins <= 0 and amount >= 1): 
        return 0; 

    return count_sums( coins, n_coins - 1, amount ) + count_sums( coins, n_coins, amount-coins[n_coins-1] )

coins = [1,2,5,10,20,50,100,200]
print(count_sums(coins, len(coins), 200))

