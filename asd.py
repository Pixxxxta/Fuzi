def f(x, p, S):
    if x >= 140 or p > 4:
        return p == 4
    # Если S пока 0, то есть суперхода еще не делали
    # Значит можно его сделать и он стоит в вариантах хода
    # Когда мы делаем супер ход, мы x не меняем, а просто S увеличиваем на 1 и теперь супер ход нельзя будет сделать
    if S == 0:
        return f(x+1, p+1, 1) or f(x+2, p+1, 2) or f(x*3, p+1, 3)
    elif S == 1:
        return f(x+2, p+1, 2) or f(x*3, p+1, 3)
    elif S == 2:
        return f(x+1, p+1, 1) or f(x*3, p+1, 3)
    elif S == 3:
        return f(x+1, p+1, 1) or f(x+2, p+1, 2)
print('19 номер') 
for i in range(1, 140):
    if f(i, 1, 0):
        print(i)
        break
    
    
    
print('20 номер')        
def f(x, p, S):
    if x >= 20 or p > 4:
        return p == 4
    if p % 2 == 1:   
        if S == 0:
            return f(x*2, p+1, S) or f(x+2, p+1, S) or f(x, p+1, S+1)
        else:
            return f(x*2, p+1, S) or f(x+2, p+1, S)
    else:
        if S == 0:
            return f(x*2, p+1, S) and f(x+2, p+1, S) and f(x, p+1, S+1)
        else:
            return f(x*2, p+1, S) and f(x+2, p+1, S)
for i in range(1, 20):
    if f(i, 1, 0):
        print(i)


print('21 номер')    
        
def f(x, p, S):
    if x >= 20 or p > 7:
        return p == 7 or p == 3 or p == 5
    if p % 2 == 0:   
        if S == 0:
            return f(x*2, p+1, S) or f(x+2, p+1, S) or f(x, p+1, S+1)
        else:
            return f(x*2, p+1, S) or f(x+2, p+1, S)
    else:
        if S == 0:
            return f(x*2, p+1, S) and f(x+2, p+1, S) and f(x, p+1, S+1)
        else:
            return f(x*2, p+1, S) and f(x+2, p+1, S)
for i in range(1, 20):
    if f(i, 1, 0):
        print(i)