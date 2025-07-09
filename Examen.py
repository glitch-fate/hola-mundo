#productos (modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video])
productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

#stock (modelo: [precio, stock])
stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 2],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2],
    'UWU131HD': [349990, 1],
    'FS1230HD': [249990, 0]
}

def stock_marca(marca):
    """Muestra el stock"""
    marca_lower = marca.lower()
    total_stock = 0
    
    print(f"""
╔═══════════════════════════╗
  Stock para marca {marca.capitalize()}   
╚═══════════════════════════╝
""")
    for modelo, datos in productos.items():
        if datos[0].lower() == marca_lower:
            if modelo in stock:
                print(f"Modelo {modelo}: {stock[modelo][1]} unidades")
                total_stock += stock[modelo][1]
    
    print(f"Stock total: {total_stock} unidades")

def busqueda_precio(p_min, p_max):
    """Busca notebooks en un rango de precios con stock disponible"""
    resultados = []
    
    for modelo, datos in stock.items():
        precio = datos[0]
        if datos[1] > 0 and p_min <= precio <= p_max:
            marca = productos[modelo][0]
            resultados.append(f"{marca}-{modelo}")
    
    if resultados:
        resultados.sort()
        print("""
╔═══════════════════════════╗
║   Notebooks encontrados   ║
╚═══════════════════════════╝
""")
        for item in resultados:
            print(item)
    else:
        print("\nNo hay notebooks en ese rango de precios.")

def actualizar_precio(modelo, p):
    """Actualiza el precio"""
    if modelo in stock:
        stock[modelo][0] = p
        return True
    else:
        return False

def main():
    """Menu principal"""
    while True:
        
        print("""
╔════════════════════════════╗
║       MENU PRINCIPAL       ║
║ 1.- Stock Marca            ║
║ 2.- Busqueda por precio    ║
║ 3.- Actualizar Precio      ║           
║ 4.- Salir                  ║
╚════════════════════════════╝
""")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            marca = input("Ingrese la marca a consultar: ")
            stock_marca(marca)
        
        elif opcion == "2":
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    if p_min > p_max:
                        print("El precio mínimo no puede ser mayor al máximo!")
                        continue
                    busqueda_precio(p_min, p_max)
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")
        
        elif opcion == "3":
            while True:
                modelo = input("Ingrese el modelo a actualizar: ")
                try:
                    nuevo_precio = int(input("Ingrese el nuevo precio: "))
                    if actualizar_precio(modelo, nuevo_precio):
                        print("Precio actualizado!!")
                    else:
                        print("El modelo no existe!!")
                except ValueError:
                    print("El precio debe ser un valor entero!")
                
                continuar = input("¿Desea actualizar otro precio? (si/no): ").lower()
                if continuar != "si":
                    break
        
        elif opcion == "4":
            print("Programa finalizado.")
            break
        
        else:
            print("Debe seleccionar una opción válida!!")

if __name__ == "__main__":
    main()


