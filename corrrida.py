python

import random
import time 

carro1 = 0
carro2 = 0
meta = 30

print("corrida de carros")
time.sleep(1)

while carro1 < meta and carro2 ?<? meta:
  carro1 += random.randint(1, 4)
  carro1 += random.randint(1, 4)

print("\ncarro 1: " + "_" * carro1 + "🏎️")
print("carro 2: " + "_" * carro2 + "🚗")

time.sleep(0.3)

if carro1 >= meta and carro2 >= meta:
  print("\nEMPATE!")
elif carro1 >= meta:
  print("\nCARRO 1 VENCEU")
else
  print("\nCARRO 2 VENCEU")
