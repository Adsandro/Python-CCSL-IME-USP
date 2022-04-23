def é_primo(k):
    primo = True    
    div = 2
    while k>div:   
        if k % div == 0:
            primo = False
        div = div + 1 
    return primo
def maior_primo(n):
    k = n        
    while k > 1 and é_primo(k)==False:
        k = k - 1
    return k
print(é_primo(100))
print(maior_primo(100))