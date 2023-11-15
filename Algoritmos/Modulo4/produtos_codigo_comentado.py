
def cadastrar_produtos(): #Função para cadastrar produtos e seus preços em um dicionário
    produtos = {} # Cria um dicionário vazio para armazenar os produtos
    n = int(input("Digite a quantidade de produtos a serem cadastrados: ")) # Solitica ao usuário a quantidade de produtos a serem cadastrados e armazena na variável n
    for i in range(n): # Repete a quantidade n vezes
        produto = input("Digite o nome do produto: ") # Solicita ao usuário o nome do produto e armazena na variável produto
        if produto in produtos: # Verifica se o produto já está no dicionário
            print("Produto já cadastrado!") # Caso positivo, a mensagem é mostrada ao usuário
        else:
            preco = float(input("Digite o preço do produto: ")) # Caso negativo, é solicitado o preço do produto e armazenado o valor na variavel preco
            produtos[produto] = preco # Adiciona o produto e o preço ao dicionário produtos{}
    return produtos # Retorna o dicionário de produtos

def buscar_preco(produtos): # Função para buscar o preço de um produto no dicionário
    while True: # Repete indefinidamente a variável produto
        produto = input("Digite o nome do produto que deseja buscar ou Fim para encerrar: ") # Solicita ao usuário o nome do produto ou Fim e armazena em produto
        if produto == 'Fim': # Verifica se o usuário digitou Fim
            break # Encerra o loop caso o usuário tenha digitado Fim
        elif produto in produtos: # Verifica se o produto está no dicionário produtos{}
            print(f"O preço do produto {produto} custa R$ {produtos[produto]}") # Caso positivo, mostra o preço do produto
        else:
            print("Produto não cadastrado!") # Caso negativo, informa ao usuário que o produto não foi cadastrado

def main(): # Define a função principal do programa
    produtos = cadastrar_produtos() # Chama a função para cadastrar produtos e obter o dicionário de produtos
    buscar_preco(produtos) # Chama a função para buscar preços usando o dicionário de produtos

if __name__ == "__main__": # Executa a função principal quando o programa é executado
    main()

