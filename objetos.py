class coche:
#definir la clase y darle caracteriaticas basicas
    def __init__(self,color,forma,ventanas,ruedas):
        self.color = color
        self.forma = forma
        self.ventanas = ventanas
        self.ruedes = ruedas
#instanciar la clase
f1=coche("verde","monoplaza","halo","lisas")
utilitario=coche("negro","monovolumen","normales","rugosas")

print(f1.color) 