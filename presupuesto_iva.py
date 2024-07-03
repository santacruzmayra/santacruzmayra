#Enunciado:
    #Para el departamento de facturación:
   # A. Ingresar tres precios de productos y mostrar la suma de los mismos.
   # B. Ingresar tres precios de productos y mostrar el promedio de los mismos.
    #C. ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).```

# Una vez finalizado el TP, Comparte el código en los foros 👇
print("ingrese el nombre del producto1")
producto1=(input())
print("ingrese el valor de ",producto1)
producto1_v=int(input())
print("ingrese el nombre del producto2" )
producto2=(input())
print("ingrese el valor del",producto2)
producto2_v=int(input())
print("ingrese el nombre del producto3")
producto3=(input())
print("ingrese el valor del",producto3)
producto3_v= int(input())

total=producto1_v + producto2_v + producto3_v
promedio= total /3
mas_iva=(total*21)/100
print("el importetotal delosproductos es",total) 
print("elpromeditototal de los productos es",promedio)
print("el importe total mas iva es",mas_iva)
