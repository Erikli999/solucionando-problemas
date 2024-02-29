def intervalo(v):
   
    if 0 <= v <= 25:
        return('Intervalo [0,25]')

    elif 25 < v <= 50:
        return('Intervalo (25,50]')

    elif 50 < v <= 75:
        return('Intervalo (50,75]')

    elif 75 < v <= 100:
        return('Intervalo (75,100]')

    return('Fora de intervalo')

v = float(input())

print(intervalo(v))
