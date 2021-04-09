import random 

def calcul_pi(n):
  punts_cercle = 0 
  punts_total = 0 
  for _ in range(n):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    distance = x**2 + y**2
    if distance <= 1:
      punts_cercle += 1
    punts_total += 1 
  print(4 * punts_cercle/punts_total)
