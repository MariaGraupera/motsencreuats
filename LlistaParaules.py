def llegir_diccionari(nom_fitxer):
    with open(nom_fitxer, 'r', encoding='utf-8') as file:
        return {paraula.strip().lower() for paraula in file}

def comprovar_paraula(paraula, diccionari):
    return paraula.lower() in diccionari

# Exemple d'ús
if __name__ == "__main__":
    # Llegim el diccionari DIEC i creem el conjunt de paraules
    diccionari_diec = llegir_diccionari('catalan.dic')

    # Prova la funció amb algunes paraules
    paraula1 = "hola"
    paraula2 = "cotxe"
    paraula3 = "gos"

    print(f"{paraula1} es troba al diccionari DIEC: {comprovar_paraula(paraula1, diccionari_diec)}")
    print(f"{paraula2} es troba al diccionari DIEC: {comprovar_paraula(paraula2, diccionari_diec)}")
    print(f"{paraula3} es troba al diccionari DIEC: {comprovar_paraula(paraula3, diccionari_diec)}")
