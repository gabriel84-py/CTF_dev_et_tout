a = 10
b = 5

try:
    resultat = a / b
except NameError as e:
    print(e)
except ZeroDivisionError:
    print('Vous divizez par 0 la atchung')
except TypeError:
    print('mauvais type')
else:
    print(resultat)
finally:
    print('bloc EAFP passé')