fullName = input("Enter your full name: ")
age = int(input("Enter your age: "))
gender = input("Enter your possible gender options M, F, X: ")
heigth = float(input("Enter your height: "))

print(f"""
Hola, usuario {fullName}. ¿Cómo estás? Te saluda Python. 
Gracias por compartir tu edad {age}; no sabía que eres un humano de tipo {gender}.
""")