with open("image.png", "rb") as image:
    f = image.read()
    try:
        formato = f[1:4].decode("utf-8")
        print("IMAGEM {}: {}".format(formato, "Sim" if formato=="PNG" else "Não"))
        print("LARGURA: {}".format(int.from_bytes(f[16:20], "big")))
        print("ALTURA: {}".format(int.from_bytes(f[20:24], "big")))
    except UnicodeDecodeError:
        print("IMAGEM: NÃO")
