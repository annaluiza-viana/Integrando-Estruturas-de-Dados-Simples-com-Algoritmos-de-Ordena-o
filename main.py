# Estado global (um único vetor "dados" para as três estruturas)
dados = None        # vetor que representa a estrutura
tipo = None         # "pilha", "fila" ou "circular"
tamanho = 0         # capacidade do vetor
# Controles de cada estrutura
topo = -1           # pilha: índice do topo
inicio = 0          # fila / fila circular: índice do primeiro elemento
fim = 0             # fila: próxima posição livre
qtd = 0             # fila circular: quantidade de elementos


# Funções auxiliares de entrada
def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def ler_opcao(mensagem):
    return input(mensagem).strip()


# Criação da estrutura
def criar_estrutura(novo_tipo):
    global dados, tipo, tamanho, topo, inicio, fim, qtd
    n = ler_inteiro("Informe o tamanho da estrutura: ")
    if n <= 0:
        print("O tamanho deve ser maior que zero.")
        return
    dados = [None] * n
    tipo = novo_tipo
    tamanho = n
    topo = -1
    inicio = 0
    fim = 0
    qtd = 0
    print(f"{novo_tipo.capitalize()} criada com tamanho {n}.")


def estrutura_ativa(tipo_esperado):
    if dados is None or tipo != tipo_esperado:
        if dados is not None:
            print(f"A estrutura atual é uma {tipo}. "
                  f"Crie uma {tipo_esperado} primeiro (isso substituirá a atual).")
        else:
            print("Crie a estrutura primeiro.")
        return False
    return True


# PILHA
def push(valor):
    global topo
    if topo == tamanho - 1:
        print("Pilha cheia (overflow)!")
        return
    topo += 1
    dados[topo] = valor
    print(f"Valor {valor} empilhado.")


def pop():
    global topo
    if topo == -1:
        print("Pilha vazia (underflow)!")
        return
    valor = dados[topo]
    dados[topo] = None
    topo -= 1
    print(f"Valor {valor} desempilhado.")

# FILA
def enfileirar(valor):
    global fim
    if fim == tamanho:
        print("Fila cheia!")
        return
    dados[fim] = valor
    fim += 1
    print(f"Valor {valor} enfileirado.")


def desenfileirar():
    global inicio
    if inicio == fim:
        print("Fila vazia!")
        return
    valor = dados[inicio]
    dados[inicio] = None
    inicio += 1
    print(f"Valor {valor} removido da fila.")

# FILA CIRCULAR
def enfileirar_circular(valor):
    global qtd
    if qtd == tamanho:
        print("Fila circular cheia!")
        return
    pos = (inicio + qtd) % tamanho
    dados[pos] = valor
    qtd += 1
    print(f"Valor {valor} enfileirado na posição {pos}.")


def desenfileirar_circular():
    global inicio, qtd
    if qtd == 0:
        print("Fila circular vazia!")
        return
    valor = dados[inicio]
    dados[inicio] = None
    inicio = (inicio + 1) % tamanho
    qtd -= 1
    print(f"Valor {valor} removido da fila circular.")


def armazenar(t):
    if not estrutura_ativa(t):
        return
    valor = ler_inteiro("Informe o valor a ser armazenado: ")
    if t == "pilha":
        push(valor)
    elif t == "fila":
        enfileirar(valor)
    else:
        enfileirar_circular(valor)


def extrair(t):
    if not estrutura_ativa(t):
        return
    if t == "pilha":
        pop()
    elif t == "fila":
        desenfileirar()
    else:
        desenfileirar_circular()


def elementos_logicos():
    if tipo == "pilha":
        return list(range(0, topo + 1))
    if tipo == "fila":
        return list(range(inicio, fim))
    return [(inicio + i) % tamanho for i in range(qtd)]


def imprimir(t):
    if not estrutura_ativa(t):
        return
    print(f"\nVetor 'dados' completo: {dados}")
    valores = [dados[i] for i in elementos_logicos()]
    if t == "pilha":
        print(f"Conteúdo da pilha (base -> topo): {valores}")
    else:
        print(f"Conteúdo da {t} (início -> fim): {valores}")
    if not valores:
        print("(estrutura vazia)")


# Algoritmos de ordenação 
def bubble_sort(v):
    n = len(v)
    for i in range(n - 1):
        trocou = False
        for j in range(n - 1 - i):
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
                trocou = True
        if not trocou:
            break


def selection_sort(v):
    n = len(v)
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            if v[j] < v[menor]:
                menor = j
        if menor != i:
            v[i], v[menor] = v[menor], v[i]


def insertion_sort(v):
    for i in range(1, len(v)):
        chave = v[i]
        j = i - 1
        while j >= 0 and v[j] > chave:
            v[j + 1] = v[j]
            j -= 1
        v[j + 1] = chave


def ordenar(algoritmo):
    indices = elementos_logicos()
    valores = [dados[i] for i in indices]
    if len(valores) < 2:
        print("É necessário ter pelo menos 2 elementos para ordenar.")
        return
    print(f"Antes : {valores}")
    algoritmo(valores)
    for i, v in zip(indices, valores):
        dados[i] = v
    print(f"Depois: {valores}")
    print(f"Vetor 'dados': {dados}")


# Menus

def menu_estrutura(t):
    nome = {"pilha": "PILHA", "fila": "FILA", "circular": "FILA CIRCULAR"}[t]
    while True:
        print(f"\n {nome} ")
        print("1 - Criar estrutura")
        print("2 - Armazenar valor")
        print("3 - Extrair valor")
        print("4 - Imprimir conteúdo")
        print("5 - Voltar ao menu anterior")
        op = ler_opcao("Escolha: ")
        if op == "1":
            criar_estrutura(t)
        elif op == "2":
            armazenar(t)
        elif op == "3":
            extrair(t)
        elif op == "4":
            imprimir(t)
        elif op == "5":
            return
        else:
            print("Opção inválida.")


def menu_ordenacao():
    if dados is None:
        print("\nNenhuma estrutura foi criada ainda. "
              "Escolha primeiro PILHA, FILA ou FILA CIRCULAR no menu principal.")
        return
    while True:
        print(f"\nORDENAR (estrutura atual: {tipo})")
        print("1 - Bubble Sort")
        print("2 - Selection Sort")
        print("3 - Insertion Sort")
        print("4 - Voltar ao menu anterior")
        op = ler_opcao("Escolha: ")
        if op == "1":
            ordenar(bubble_sort)
        elif op == "2":
            ordenar(selection_sort)
        elif op == "3":
            ordenar(insertion_sort)
        elif op == "4":
            return
        else:
            print("Opção inválida.")


def menu_principal():
    while True:
        print("\nMENU PRINCIPAL")
        print("1 - PILHA") #LIFO: último a entrar, primeiro a sair
        print("2 - FILA") #FIFO: primeiro a entrar, primeiro a sair
        print("3 - FILA CIRCULAR") #depois da última posição, volta-se para a posição 0
        print("4 - ORDENAR")
        print("5 - SAIR")
        op = ler_opcao("Escolha: ")
        if op == "1":
            menu_estrutura("pilha")
        elif op == "2":
            menu_estrutura("fila")
        elif op == "3":
            menu_estrutura("circular")
        elif op == "4":
            menu_ordenacao()
        elif op == "5":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu_principal()