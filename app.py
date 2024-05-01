def girl_or_boy(nombre_usuario):
    nombre_usuario = nombre_usuario.lower()
    conteo_letras = {}
    for letra in nombre_usuario:
        if letra in conteo_letras:
            conteo_letras[letra] += 1
        else:
            conteo_letras[letra] = 1

    cantidad_letras = len(conteo_letras)

    if cantidad_letras % 2 != 0:
        return "¡ITS A BOY!"
    else:
        return "¡ITS A GIRL!"


print(girl_or_boy("fabian"))