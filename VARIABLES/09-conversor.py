temperatura=float(input("ingrese la temperatura:"))
escala=input("es Fahrenheit (F) o es Celsius(C)?:").lower()
 
if escala=="f":
    celsius=(temperatura-32)*5/9
    print(celsius)
elif escala=="c":    
    fahrenheit=temperatura*1.8+32
    print(fahrenheit)
else:
    print("escala incorrecta")    