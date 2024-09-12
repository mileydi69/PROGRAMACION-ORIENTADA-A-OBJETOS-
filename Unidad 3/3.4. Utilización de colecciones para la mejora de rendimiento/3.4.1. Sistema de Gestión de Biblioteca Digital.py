# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn
        self._datos_inmutables = (self.autor, self.titulo)  # Tupla inmutable para autor y título

    def __str__(self):
        return f"'{self.titulo}' de {self.autor} - Categoría: {self.categoria}, ISBN: {self.isbn}"

# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
        else:
            print(f"El usuario {self.nombre} no tiene el libro '{libro.titulo}' prestado.")

    def listar_libros_prestados(self):
        if not self.libros_prestados:
            return f"El usuario {self.nombre} no tiene libros prestados."
        return [str(libro) for libro in self.libros_prestados]

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios = {}  # Diccionario de usuarios, con el ID de usuario como clave
        self.historial_prestamos = {}  # Historial de préstamos por usuario

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido a la biblioteca.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            libro_removido = self.libros.pop(isbn)
            print(f"Libro '{libro_removido.titulo}' eliminado de la biblioteca.")
        else:
            print(f"No se encontró un libro con ISBN {isbn} en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario {usuario.nombre} registrado exitosamente.")
        else:
            print(f"El ID de usuario {usuario.id_usuario} ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario_baja = self.usuarios.pop(id_usuario)
            print(f"Usuario {usuario_baja.nombre} dado de baja.")
        else:
            print(f"No se encontró un usuario con ID {id_usuario}.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros.pop(isbn)
            usuario.prestar_libro(libro)
            self.historial_prestamos[id_usuario] = self.historial_prestamos.get(id_usuario, []) + [libro]
            print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
        else:
            print("Error: Usuario o libro no disponible.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.devolver_libro(libro)
                    self.libros[isbn] = libro
                    print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
                    return
            print(f"El usuario {usuario.nombre} no tiene prestado el libro con ISBN {isbn}.")
        else:
            print("Error: Usuario no encontrado.")

    def buscar_libro(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if criterio == "titulo" and valor.lower() in libro.titulo.lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.autor.lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() == libro.categoria.lower():
                resultados.append(libro)
        return resultados if resultados else f"No se encontraron libros con {criterio} '{valor}'."

# Función para probar el sistema de gestión de la biblioteca
def pruebas_biblioteca():
    # Crear una biblioteca
    biblioteca = Biblioteca()

    # Añadir libros a la biblioteca
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "1234567890")
    libro2 = Libro("1984", "George Orwell", "Distopía", "0987654321")
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)

    # Registrar usuarios
    usuario1 = Usuario("Sebastian Escobar", "U001")
    usuario2 = Usuario("Yurani Tenorio", "U002")
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar libros
    biblioteca.prestar_libro("U001", "1234567890")
    biblioteca.prestar_libro("U002", "0987654321")

    # Listar libros prestados por usuario
    print(usuario1.listar_libros_prestados())
    print(usuario2.listar_libros_prestados())

    # Devolver libros
    biblioteca.devolver_libro("U001", "1234567890")
    biblioteca.devolver_libro("U002", "0987654321")

    # Buscar libros
    print("Buscar por título '1984':", biblioteca.buscar_libro("titulo", "1984"))
    print("Buscar por autor 'Gabriel García Márquez':", biblioteca.buscar_libro("autor", "Gabriel García Márquez"))
    print("Buscar por categoría 'Novela':", biblioteca.buscar_libro("categoria", "Novela"))

# Ejecutar pruebas
pruebas_biblioteca()
