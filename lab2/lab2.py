import math

def check_pnr(checkPnr):
    viktPrn = checkPnr.copy()
    vProdukter(viktPrn)
    sum = vSumma(viktPrn)
    sum -= checkPnr[9]
    rounded = math.ceil((sum/10)) * 10
    Rest = rounded - sum  # kontroll
    return bool(Rest == checkPnr[9])
   

def vProdukter(viktPrn):
        for i in range(len(viktPrn)-1):
            if (i + 1) % 2 == 0:
                viktPrn[i] = viktPrn[i] * 1
            else:
                viktPrn[i] = viktPrn[i] * 2

def vSumma(viktPro):
    sOfPrnmr = '' .join(map(str, viktPro)) # make list into string
    sum = 0
    for siffror in str(sOfPrnmr): 
        sum += int(siffror)
    
    
    return sum
 
print(check_pnr([7, 4, 0, 2, 1, 7, 4, 8, 2, 0]))




