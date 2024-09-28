from interfaz import ventas
from interfaz import productos
from interfaz import clientes
def menu_modulo():
    print("1. Imprimir una copia de la factura ")
    print("2. Resumen de las facturas")
    print("3. Diagrama de barras")
    print("4. listado de productos comunes entre dos clientes")

def modulo():
    while True:
        menu_modulo()
        opcion = input("Digite una opcion ")
        match opcion:
            case "1":
             ventas()
             productos()
             clientes()

            case "2":
             pass
            case "3":
             pass

print(modulo())
