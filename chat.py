import os

mensagens = []
nome = input("Nome: ")

while True:
    os.system('cls' if os.name == 'nt' else 'clear') # Pode limpar a tela de forma multiplataforma.
    
    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

        print("________________________________________")
    
    texto = input("Digite o texto: ")
    if texto == "fim":
        break

    mensagens.append({
        "nome": nome,
        "texto": texto
    })