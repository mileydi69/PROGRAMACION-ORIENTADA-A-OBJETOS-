# Clase Libro
# representa un libro en la biblioteca
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Utilizamos una tupla para almacenar el título y el autor como atributos inmutables
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} por {self.info[1]} (ISBN: {self.isbn}, Categoría: {self.categoria})"

# Clase Usuario
# representa a un usuario de la biblioteca
class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        # Lista de libros actualmente prestados al usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"

# Clase Biblioteca
# gestiona libros, usuarios y préstamos
class Biblioteca:
    def __init__(self):
        # Diccionario de libros disponibles, clave: ISBN, valor: objeto Libro
        self.libros_disponibles = {}
        # Diccionario de usuarios registrados, clave: user_id, valor: objeto Usuario
        self.usuarios_registrados = {}
        # Conjunto para asegurar IDs de usuario únicos
        self.ids_usuarios = set()

    # Añadir un libro a la biblioteca
    def añadir_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro '{libro.info[0]}' añadido a la biblioteca.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya existe en la biblioteca.")

    # Quitar un libro de la biblioteca
    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            eliminado = self.libros_disponibles.pop(isbn)
            print(f"Libro '{eliminado.info[0]}' eliminado de la biblioteca.")
        else:
            print(f"No se encontró un libro con ISBN {isbn}.")

    # Registrar un nuevo usuario
    def registrar_usuario(self, usuario):
        if usuario.user_id not in self.ids_usuarios:
            self.usuarios_registrados[usuario.user_id] = usuario
            self.ids_usuarios.add(usuario.user_id)
            print(f"Usuario '{usuario.nombre}' registrado exitosamente.")
        else:
            print(f"El ID de usuario {usuario.user_id} ya está en uso.")

    # Dar de baja a un usuario
    def dar_baja_usuario(self, user_id):
        if user_id in self.ids_usuarios:
            usuario = self.usuarios_registrados.pop(user_id)
            self.ids_usuarios.remove(user_id)
            print(f"Usuario '{usuario.nombre}' dado de baja.")
        else:
            print(f"No se encontró un usuario con ID {user_id}.")

    # Prestar un libro a un usuario
    def prestar_libro(self, isbn, user_id):
        if isbn in self.libros_disponibles:
            if user_id in self.ids_usuarios:
                libro = self.libros_disponibles.pop(isbn)
                usuario = self.usuarios_registrados[user_id]
                usuario.libros_prestados.append(libro)
                print(f"Libro '{libro.info[0]}' prestado a {usuario.nombre}.")
            else:
                print(f"Usuario con ID {user_id} no está registrado.")
        else:
            print(f"Libro con ISBN {isbn} no está disponible.")

    # Devolver un libro a la biblioteca
    def devolver_libro(self, isbn, user_id):
        if user_id in self.ids_usuarios:
            usuario = self.usuarios_registrados[user_id]
            # Buscar el libro en la lista de libros prestados del usuario
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros_disponibles[isbn] = libro
                    print(f"Libro '{libro.info[0]}' devuelto por {usuario.nombre}.")
                    return
            print(f"El usuario '{usuario.nombre}' no tiene el libro con ISBN {isbn}.")
        else:
            print(f"Usuario con ID {user_id} no está registrado.")

    # Buscar libros por título
    def buscar_por_titulo(self, titulo):
        resultados = []
        for libro in self.libros_disponibles.values():
            if titulo.lower() in libro.info[0].lower():
                resultados.append(libro)
        print(f"Búsqueda de título '{titulo}': {len(resultados)} resultados.")
        for libro in resultados:
            print(libro)

    # Buscar libros por autor
    def buscar_por_autor(self, autor):
        resultados = []
        for libro in self.libros_disponibles.values():
            if autor.lower() in libro.info[1].lower():
                resultados.append(libro)
        print(f"Búsqueda de autor '{autor}': {len(resultados)} resultados.")
        for libro in resultados:
            print(libro)

    # Buscar libros por categoría
    def buscar_por_categoria(self, categoria):
        resultados = []
        for libro in self.libros_disponibles.values():
            if categoria.lower() == libro.categoria.lower():
                resultados.append(libro)
        print(f"Búsqueda de categoría '{categoria}': {len(resultados)} resultados.")
        for libro in resultados:
            print(libro)

    # Listar libros prestados a un usuario
    def listar_libros_prestados(self, user_id):
        if user_id in self.ids_usuarios:
            usuario = self.usuarios_registrados[user_id]
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(libro)
        else:
            print(f"Usuario con ID {user_id} no está registrado.")

# Pruebas del sistema de biblioteca

# Crear instancia de la biblioteca
mi_biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "1234567890")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Novela", "0987654321")
libro3 = Libro("La Ciudad y los Perros", "Mario Vargas Llosa", "Novela", "1122334455")

# Añadir libros a la biblioteca
mi_biblioteca.añadir_libro(libro1)
mi_biblioteca.añadir_libro(libro2)
mi_biblioteca.añadir_libro(libro3)

# Crear usuarios
usuario1 = Usuario("Lorena Encarnacion", "user001")
usuario2 = Usuario("Victoria Chalar", "user002")

# Registrar usuarios
mi_biblioteca.registrar_usuario(usuario1)
mi_biblioteca.registrar_usuario(usuario2)

# Prestar libros
mi_biblioteca.prestar_libro("1234567890", "user001")
mi_biblioteca.prestar_libro("0987654321", "user002")

# Listar libros prestados a un usuario
mi_biblioteca.listar_libros_prestados("user001")

# Devolver libros
mi_biblioteca.devolver_libro("1234567890", "user001")

# Buscar libros por título
mi_biblioteca.buscar_por_titulo("ciudad")

# Buscar libros por autor
mi_biblioteca.buscar_por_autor("Cervantes")

# Buscar libros por categoría
mi_biblioteca.buscar_por_categoria("Novela")

# Quitar un libro de la biblioteca
mi_biblioteca.quitar_libro("1122334455")

# Dar de baja a un usuario
mi_biblioteca.dar_baja_usuario("user002")
