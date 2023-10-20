# You're considering a $100 bet with your friend. If n consecutive fair coin flips result in all heads, then
# you win - else your friend wins. Your friend agrees to let you attempt the bet as many times as you'd
# like. Assuming you attempt the bet x times, what's the probability that you'll win the bet at least
# once? As well, what should your winning payout ($100, $200, etc) be to ensure that you at least
# break even given unlimited attempts of the bet?
# Write a function which takes in the number of consecutive coin flips (n) and the number of bet
# attempts (x) and returns a list containing:
# • Firstly, the probability that you win the bet at least once
# • Secondly, your required winning payout
# Note:  
# • You can assume a fair coin.
# • You shouldn't use any libraries.
# • Your output values will automatically be rounded to the fourth decimal.

#sol 

def repeating_heads(n, x):
    # Write your code here.
    bet_size = 100   # bet amount 100$
    heads_chance = 1/2 # change of getting head
    trial_win_chance = heads_chance ** n # chance of getting head n time 
    trial_lose_chance = 1 - trial_win_chance # chance of losing n times
    repeated_trial_lose_chance = trial_lose_chance ** x # change of lose in x attempt
    repeated_trial_win_chance = 1 - repeated_trial_lose_chance # chance of win in x attempt
    break_even_point = bet_size / repeated_trial_win_chance # break even winning amount 
    return [repeated_trial_win_chance * 100, break_even_point]