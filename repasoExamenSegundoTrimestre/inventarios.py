import random
def productos():
    productos = []
    elementos_supermercado = ["Leche", "Pan", "Huevos", "Arroz", "Pasta", "Aceite de cocina", "Harina", "Azucar", "Sal", "Pimienta", "Queso", "Yogur", "Cereales", "Cafe", "Te", "Mermelada", "Salsa de tomate", "Salsa de soja", "Vinagre", "Mayonesa", "Ketchup", "Mostaza", "Mantequilla", "Jamon", "Pollo", "Carne de res", "Pescado", "Lechuga", "Tomates", "Zanahorias", "Manzanas", "Platanos", "Naranjas", "Papas", "Cebollas", "Ajo", "Aguacates", "Pepinos", "Espinacas", "Champiñones", "Calabacines", "Zanahorias", "Brocoli", "Guisantes", "Maiz", "Frijoles", "Panecillos", "Galletas", "Patatas fritas", "Refrescos", "Agua embotellada", "Zumos de frutas", "Vino"]
    with open("inventario.txt", "w+") as file:
        veces = int(input("¿Cuántos elementos quieres meter? "))
        for i in range(veces):
            codigo = random.randint(1000,9999)
            nombre = random.choice(elementos_supermercado)
            cantidad = random.randint(1,500)
            precio = random.randint(1,20)
            productos.append({"codigo": codigo, "nombre": nombre, "cantidad": cantidad, "precio": precio})

        productos.sort(key=lambda x: x["codigo"])

        for producto in productos:
            file.write(f"{producto['codigo']},{producto['nombre']},{producto['cantidad']},{producto['precio']},-1")

productos()