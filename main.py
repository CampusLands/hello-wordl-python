#  > Mayor
#  < Menor
#  >= Mayor igual
#  <= Menor igual
#  == igual
#  != Diferente
#  !==  No identico
# 
# Estos operador de comparacion 
# devuelven una afirmacion boleana si se cumple o no 'True' 'False'

age = int(input("Ingrese su edad: ")) # 20
#   20 == 18
#     False
if age == 18:
    print("El mayor de edad")
#  20 == 20
#    True
elif age == 20:
    print("El mayor de edad y nosabia que tienes 20")
else:
    print("Nose :( lo que eres")