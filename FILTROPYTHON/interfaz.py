def clientes():
    with open("/home/camper/Escritorio/FILTROPYTHON/clientes.txt", "r") as fd:
     for i in fd:
        i = [i.split]
        i = str(i)  
        print(i)     
        
def productos():
   with open("/home/camper/Escritorio/FILTROPYTHON/productos.txt", "r") as fd:
     for i in fd:
        print (i)

def ventas():
   with open("/home/camper/Escritorio/FILTROPYTHON/ventas.txt", "r") as fd:
     for i in fd:
        print (i)
clientes()