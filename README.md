
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
        """Muestra el catálogo completo con categorías y productos."""
        for categoria, productos in self.productos.items():
            print(f'Categoría: {categoria} | Productos: {", ".join(productos) if productos else "Ninguno"}')

# Ejemplo de uso:
catalogo = CatalogoTienda()

# Agregar productos
catalogo.agregar_producto('Electrónica', 'Teléfono')
catalogo.agregar_producto('Electrónica', 'Televisor')
catalogo.agregar_producto('Ropa', 'Camisa')
catalogo.agregar_producto('Alimentos', 'Pan')

# Mostrar catálogo
catalogo.mostrar_catalogo()

# Buscar un producto
catalogo.buscar_producto('Camisa')

# Eliminar un producto
catalogo.eliminar_producto('Electrónica', 'Televisor')

# Mostrar catálogo después de la eliminación
catalogo.mostrar_catalogo()