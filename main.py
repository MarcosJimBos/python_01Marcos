from servicios.clima import consultar_clima

def main():
    ciudad = input("Hola soy Marcos, introduce tu ciudad: ")
    info = consultar_clima(ciudad)

    if info:
        print(f"\nEl Clima en {ciudad}:")
        print(f"\tEn {ciudad} hace una temperatura de: {info['temperatura']} °C")
        print(f"\tLa sensación térmica es de: {info['sensacion']} °C")
        print(f"\tEsta es la Descripción: {info['descripcion']}")
    else:
        print("No se pudo obtener la información meteorológica.")

if __name__ == "__main__":
    main()
