from entity import User
class UserController:
    def __init__(self):
        # Almacenamos los usuarios en un diccionario {nombre: objeto_user}
        self._users = {}

    def add_user(self, name, age, hobby):
        """Crea un nuevo usuario y lo añade a la colección."""
        if name in self._users:
            print(f"Error: El usuario '{name}' ya existe.")
            return False
        
        try:
            new_user = User(name, age, hobby)
            self._users[name] = new_user
            print(f"Usuario '{name}' creado con éxito.")
            return True
        except ValueError as e:
            print(f"Error al crear usuario: {e}")
            return False

    def get_user(self, name):
        """Busca y retorna un objeto usuario por su nombre."""
        return self._users.get(name, "Usuario no encontrado.")

    def list_all_users(self):
        """Muestra todos los usuarios registrados."""
        if not self._users:
            print("No hay usuarios en la lista.")
        else:
            print("--- Lista de Usuarios ---")
            for user in self._users.values():
                print(f"Nombre: {user.name} | Edad: {user.age} | Hobby: {user.hobby}")

    def remove_user(self, name):
        """Elimina un usuario de la colección."""
        if name in self._users:
            del self._users[name]
            print(f"Usuario '{name}' eliminado.")
        else:
            print(f"No se pudo eliminar: '{name}' no existe.")