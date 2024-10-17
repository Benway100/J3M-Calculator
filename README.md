class CatalogoTienda:
    def __init__(self):
        # Inicializamos el catálogo con algunas categorías (filas) y productos vacíos (columnas)
        self.categorias = ['Electrónica', 'Ropa', 'Alimentos', 'Libros']
        self.productos = {categoria: [] for categoria in self.categorias}
    
    def agregar_producto(self, categoria, producto):
        """Agrega un producto a una categoría específica."""
        if categoria in self.productos:
            self.productos[categoria].append(producto)
            print(f'Producto "{producto}" agregado a la categoría "{categoria}".')
        else:
            print(f'La categoría "{categoria}" no existe.')

    def eliminar_producto(self, categoria, producto):
        """Elimina un producto de una categoría específica."""
        if categoria in self.productos:
            try:
                self.productos[categoria].remove(producto)
                print(f'Producto "{producto}" eliminado de la categoría "{categoria}".')
            except ValueError:
                print(f'El producto "{producto}" no se encuentra en la categoría "{categoria}".')
        else:
            print(f'La categoría "{categoria}" no existe.')

    def buscar_producto(self, producto):
        """Busca un producto en todas las categorías y devuelve su ubicación."""
        for categoria, productos in self.productos.items():
            if producto in productos:
                print(f'Producto "{producto}" encontrado en la categoría "{categoria}".')
                return categoria
        print(f'El producto "{producto}" no se encontró en ninguna categoría.')
        return None

    def mostrar_catalogo(self):
        """Muestra el catálogo en formato de matriz, con categorías y productos."""
        # Determinamos el máximo número de productos en cualquier categoría
        max_productos = max(len(productos) for productos in self.productos.values())

        # Encabezado de las columnas
        print(f"{'Categoría':<15}", end='')
        for i in range(1, max_productos + 1):
            print(f"Producto {i:<10}", end='')
        print()  # Salto de línea para el encabezado

        # Mostrar cada categoría y sus productos como una fila de la "matriz"
        for categoria, productos in self.productos.items():
            print(f"{categoria:<15}", end='')
            for i in range(max_productos):
                if i < len(productos):
                    print(f"{productos[i]:<12}", end='')  # Imprimir producto si existe
                else:
                    print(f"{'':<12}", end='')  # Espacio en blanco si no hay producto
            print()  # Salto de línea al final de cada categoría

# Ejemplo de uso:
catalogo = CatalogoTienda()

# Agregar productos
catalogo.agregar_producto('Electrónica', 'Teléfono')
catalogo.agregar_producto('Electrónica', 'Televisor')
catalogo.agregar_producto('Ropa', 'Camisa')
catalogo.agregar_producto('Ropa', 'Pantalones')
catalogo.agregar_producto('Alimentos', 'Pan')
catalogo.agregar_producto('Alimentos', 'Leche')

# Mostrar catálogo en formato de matriz
catalogo.mostrar_catalogo()