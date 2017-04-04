start = 9
end = 10
wc = 0
initial = 1

def getExp(n):
    return 2 ** n

def genMatrix(max = 10):
    """ return Result Matrix, 0 return all combination of Result """
    matrix = []
    for i in range(getExp(start), getExp(end)):
        # print(str(bin(i)))
        matrix.append(str(bin(i))[-end+1:])
        # print(matrix[j])
        max -= 1
        if max == 0:
            break
    return matrix

def payout():
    return

def genMatrix1(max = 10):
    """ return Result Matrix, 0 return all combination of Result """
    digit = len(bin(max-1))-2
    # print(digit)
    matrix = [str(bin(m))[2:].zfill(digit) for m in range(max)]
    return matrix

def winChance(matrix, winSignal):
    winMatrix = [m for m in matrix if winSignal in m]
    return winMatrix

def calcProfit(row):
    profit = 0
    amount = 0
    for char in row:
        amount = stake(char)
        print(amount)
        if char == "1":
            profit += amount
        else:
            profit -= amount
        # print(profit)


def stake(result = None, lastStake = 1):
    if result == None:
        return initial
    

def tStrategy01():
    return None

def bStrategy01():
    """ Martingale """
    """ https://en.wikipedia.org/wiki/Martingale_(probability_theory) """

# def stake(r):
#     global wc, s
#     if r == "1":
#         if wc == 0:
#             wc += 1
#             s = 1
#             return s

#         if wc < 2:
#             wc += 1
#             s *= 2
#         else:
#             wc = 0
#             s = 1
#     else:
#         wc = 0
    
#     return s


def predict(row = None):
    print(row)
    if row:
        calcProfit(row)
    else:
        for row in genMatrix(1):
            calcProfit(row)

if __name__ == "__main__":
    # predict()
    # predict("101010101")
    # predict("110101011")
    m = genMatrix1(getExp(12))
    print(len(m))
    print(len(winChance(m, "001")))


    
# -6.18
# +6.28

# 0.94
# 1.88
# 3.77

# 000       -1-1-1                  =-1-1-1
# 001       -1-1+0.94               =-1-1+0.94
# 010       -1+0.94-2               =-1+0.94-2
# 011       -1+0.94+1.88            =-1+0.94+1.88
# 100       0.94-2-2                =0.94-2-2
# 101       0.94-2+1.88             =0.94-2+1.88
# 110       0.94+1.88-1             =0.94+1.88-1
# 111       0.94+1.88+0.94          =0.94+1.88+0.94

# 0000      -1-1-1-1               =-1-1-1-1           
# 0001      -1-1-1+0.94            =-1-1-1+0.94        
# 0010      -1-1+0.94-2            =-1-1+0.94-2        
# 0011      -1-1+0.94+1.88         =-1-1+0.94+1.88     
# 0100      -1+0.94-2-2            =-1+0.94-2-2        
# 0101      -1+0.94-2+1.88         =-1+0.94-2+1.88     
# 0110      -1+0.94+1.88-1         =-1+0.94+1.88-1     
# 0111      -1+0.94+1.88+0.94      =-1+0.94+1.88+0.94  
# 1000      0.94-2-2-2             =0.94-2-2-2         
# 1001      0.94-2-2+1.88          =0.94-2-2+1.88      
# 1010      0.94-2+1.88-4          =0.94-2+1.88-4      
# 1011      0.94-2+1.88+3.77       =0.94-2+1.88+3.77   
# 1100      0.94+1.88-1-1          =0.94+1.88-1-1      
# 1101      0.94+1.88-1+0.94       =0.94+1.88-1+0.94   
# 1110      0.94+1.88+0.94-2       =0.94+1.88+0.94-2   
# 1111      0.94+1.88+0.94+1.88    =0.94+1.88+0.94+1.88

# 00000      -1-1-1-1-1                =-1-1-1-1-1              
# 00001      -1-1-1-1+0.94             =-1-1-1-1+0.94           
# 00010      -1-1-1+0.94-2             =-1-1-1+0.94-2           
# 00011      -1-1-1+0.94+1.88          =-1-1-1+0.94+1.88        
# 00100      -1-1+0.94-2-2             =-1-1+0.94-2-2           
# 00101      -1-1+0.94-2+1.88          =-1-1+0.94-2+1.88        
# 00110      -1-1+0.94+1.88-1          =-1-1+0.94+1.88-1        
# 00111      -1-1+0.94+1.88+0.94       =-1-1+0.94+1.88+0.94     
# 01000      -1+0.94-2-2-2             =-1+0.94-2-2-2           
# 01001      -1+0.94-2-2+1.88          =-1+0.94-2-2+1.88        
# 01010      -1+0.94-2+1.88-4          =-1+0.94-2+1.88-4        
# 01011      -1+0.94-2+1.88+3.77       =-1+0.94-2+1.88+3.77     
# 01100      -1+0.94+1.88-1-1          =-1+0.94+1.88-1-1        
# 01101      -1+0.94+1.88-1+0.94       =-1+0.94+1.88-1+0.94     
# 01110      -1+0.94+1.88+0.94-2       =-1+0.94+1.88+0.94-2     
# 01111      -1+0.94+1.88+0.94+1.88    =-1+0.94+1.88+0.94+1.88  
# 10000      0.94-2-2-2-2              =0.94-2-2-2-2            
# 10001      0.94-2-2-2+0.94           =0.94-2-2-2+0.94         
# 10010      0.94-2-2+0.94-2           =0.94-2-2+0.94-2         
# 10011      0.94-2-2+0.94+1.88        =0.94-2-2+0.94+1.88      
# 10100      0.94-2+0.94-2-2           =0.94-2+0.94-2-2         
# 10101      0.94-2+0.94-2+1.88        =0.94-2+0.94-2+1.88      
# 10110      0.94-2+0.94+1.88-1        =0.94-2+0.94+1.88-1      
# 10111      0.94-2+0.94+1.88+0.94     =0.94-2+0.94+1.88+0.94   
# 11000      0.94+1.88-1-1-1           =0.94+1.88-1-1-1         
# 11001      0.94+1.88-1-1+0.94        =0.94+1.88-1-1+0.94      
# 11010      0.94+1.88-1+0.94-2        =0.94+1.88-1+0.94-2      
# 11011      0.94+1.88-1+0.94+1.8      =0.94+1.88-1+0.94+1.8    
# 11100      0.94+1.88+0.94-2-2        =0.94+1.88+0.94-2-2      
# 11101      0.94+1.88+0.94-2+1.88     =0.94+1.88+0.94-2+1.88   
# 11110      0.94+1.88+0.94+1.88-1     =0.94+1.88+0.94+1.88-1   
# 11111      0.94+1.88+0.94+1.88+0.94  =0.94+1.88+0.94+1.88+0.94