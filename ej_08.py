'''Escribe un programa que muestre por consola el resultado de la siguiente
operación (10+3) * (6+6), ¿qué sucede si realizas la misma operación pero sin
los paréntesis?'''
numero1=10
numero2=3
subtotal1=int(numero1+numero2)
numero3=6
numero4=6
subtotal2=int(numero3+numero4)
total=int(subtotal1*subtotal2)

print("el resultado de la ecuacion(10+3)*(6+6)con parentesis es",total)
numero5=10
numero6=3
numero7=6
numero8=6
total2=int(numero5+numero6*numero7+numero8)
print("el total de la escuacion sin parentesis es",total2)
numero9=10
numero10=3
numero11=6
numero12=6
subt=int(numero10*numero11)
total2=int(numero9+subt+numero12)
print("el total de la escuacion sin parentesis es",total2)