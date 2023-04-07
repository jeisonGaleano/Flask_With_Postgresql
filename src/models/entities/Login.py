class Login():

    def __init__(self, usuario, contrasena=None) -> None:
        self.usuario = usuario
        self.contrasena = contrasena
    def to_JSON(self):
        return {
            'usuario': self.usuario,
            'contrasena': self.contrasena
        }