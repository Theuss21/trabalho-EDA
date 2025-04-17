familia = []

def adicionar_membro(nome, idade, sexo, pai=None):
    membro = {
        'nome': nome,
        'idade': idade,
        'sexo': sexo,
        'filhos': []
    }
    
    if pai is None:
        familia.append(membro)
    else:
        pai_encontrado = buscar_membro(pai)
        if pai_encontrado:
            pai_encontrado['filhos'].append(membro)
        else:
            print(f"Erro: Pai '{pai}' não encontrado na família.")

def buscar_membro(nome, lista=None):
    if lista is None:
        lista = familia
        
    for membro in lista:
        if membro['nome'] == nome:
            return membro
        encontrado = buscar_membro(nome, membro['filhos'])
        if encontrado:
            return encontrado
    return None

def descendentes(nome):
    membro = buscar_membro(nome)
    if not membro:
        return []
    
    lista_descendentes = []
    for filho in membro['filhos']:
        lista_descendentes.append(filho['nome'])
        lista_descendentes.extend(descendentes(filho['nome']))
    
    return lista_descendentes

def antepassados(nome):
    membro = buscar_membro(nome)
    if not membro:
        return []
    
    lista_antepassados = []
    
    def buscar_pai(nome_alvo, lista_atual, lista_pais):
        for membro in lista_atual:
            for filho in membro['filhos']:
                if filho['nome'] == nome_alvo:
                    lista_pais.append(membro['nome'])
                    buscar_pai(membro['nome'], familia, lista_pais)
                    return
            buscar_pai(nome_alvo, membro['filhos'], lista_pais)
    
    buscar_pai(nome, familia, lista_antepassados)
    return lista_antepassados

familia = []
adicionar_membro("João", 70, "M")
adicionar_membro("Carlos", 50, "M", "João")
adicionar_membro("Pedro", 30, "M", "Carlos")
adicionar_membro("Lucas", 10, "M", "Pedro")

print("Antepassados de Lucas:", antepassados("Lucas"))