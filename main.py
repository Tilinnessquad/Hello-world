### Autor: Juan Londoño - Curso: 4D
### Funcion para ver el iva
def precio():
  p = input("Nombre producto: ")
  v = int(input("Valor del producto: "))
  u = int(input("Unidades del producto: "))
  ps = u*v
  i = ps*0.19
  pt = ps+i

  
  print("\n Producto : ", p, "\n", "Precio : ", v, "$", "\n", "Cantidad: ", u, "\n", "Subtotal: ", ps,"$", "\n", "Total: ", pt ,"$",)


precio()