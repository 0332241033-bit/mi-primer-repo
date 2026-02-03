class User:
    def __init__(self, name, age, hobby):
        # Usamos los setters para validar/asignar desde el inicio
        self.name = name
        self.age = age
        self.hobby = hobby

    # --- Property para NAME ---
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # --- Property para AGE ---
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("La edad no puede ser negativa")
        self._age = value

    # --- Property para HOBBY ---
    @property
    def hobby(self):
        return self._hobby

    @hobby.setter
    def hobby(self, value):
        self._hobby = value