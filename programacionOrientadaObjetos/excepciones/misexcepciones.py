class excepcion1(Exception):
    pass
    def error(self):
        try:
            raise excepcion1("Algo salio mal")
        except excepcion1 as e:
            print(f"Mi error dice {e}")
    