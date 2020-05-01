#You have n fair coins and you flip them all at the same time. Any that come up tails you set aside. The ones that come up heads you flip again.
# How many rounds do you expect to play before only one coin remains?

num_rounds = 0
def flipCoin(n):
    global num_rounds
    num_rounds +=1
    heads =  n/2
    tails = n/2
    if heads <= 1:
        return num_rounds
    else:
        flipCoin(heads)
flipCoin(2)
print(num_rounds)
