Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
... 
... MAX = 10**7
... 
... # Criba de Eratóstenes
... es_primo = [True] * (MAX + 1)
... es_primo[0] = es_primo[1] = False
... 
... for i in range(2, int(MAX**0.5) + 1):
...     if es_primo[i]:
...         for j in range(i*i, MAX + 1, i):
...             es_primo[j] = False
... 
... # arreglo acumulado para contar primos rápido
... pref = [0] * (MAX + 1)
... for i in range(1, MAX + 1):
...     pref[i] = pref[i-1] + (1 if es_primo[i] else 0)
... 
... # leer entrada
... t = int(input())
... for _ in range(t):
...     a, b = map(int, input().split())
