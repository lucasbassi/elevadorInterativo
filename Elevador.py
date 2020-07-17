class Elevador:

    def __init__(self, capacidade, total_andar):
        self.__capacidade = capacidade
        self.__total_andar = total_andar
        self.__andar_atual = 0
        self.__pessoas = 0

    def entrar(self):
        if self.__pessoas == self.__capacidade:
            print('Não é possível entrar mais pessoas no elevador.\n'
                  'Sua capacidade máxima já foi atingida.')
        else:
            self.__pessoas += 1
            print('Entrou uma pessoa no elevador')

    def sai(self):
        if self.__pessoas == 0:
            print('O elevador está vazio\n'
                  'Não há pessoas para sair.')
        else:
            self.__pessoas -= 1
            print('Saiu uma pessoa do elevador')

    def sobe(self):
        if self.__andar_atual == self.__total_andar:
            print('O elevador já está na cobertura')
        else:
            self.__andar_atual += 1
            print('O elevador subiu um andar')

    def desce(self):
        if self.__andar_atual == 0:
            print('O elevador já está no terreo')
        else:
            self.__andar_atual -= 1
            print('O elevador desceu um andar')

    def get_andar_atual(self):
        return self.__andar_atual

    def get_total_andar(self):
        return self.__total_andar

    def get_pessoas(self):
        return self.__pessoas

    def get_capicidade(self):
        return self.__capacidade

    def set_capacidade(self, nova_capacidade):
        self.__capacidade = nova_capacidade
        print('Capacidade do elevador atualizada')

    def set_total_andar(self, novo_total):
        self.__total_andar = novo_total
        print('Total de andares atualizado')


while True:
    try:
        cap = int(input('Qual a capacidade máxima de pessoas no elevador? '))
        andares = int(input('Quantos andares há no prédio? '))
        elevador_criado = Elevador(cap, andares)
        break
    except ValueError:
        print('Valor incorreto')


while True:
    print('Escolha a ação:\n'
          '1- Entrar alguém\n'
          '2- Sair alguém\n'
          '3- Subir um andar\n'
          '4- Descer um andar\n'
          '5- Qual andar está\n'
          '6- Quantas pessoas há no elevador\n'
          '7- Alterar capacidade do elevador\n'
          '8- Mudar a quantia de andares do prédio\n'
          '9- Informações gerais sobre o elevador\n'
          '10- Sair')
    escolha = input()

    if escolha == '1':
        elevador_criado.entrar()
    elif escolha == '2':
        elevador_criado.sai()
    elif escolha == '3':
        elevador_criado.sobe()
    elif escolha == '4':
        elevador_criado.desce()
    elif escolha == '5':
        andar_atual = elevador_criado.get_andar_atual()
        if andar_atual == 0:
            print('O elevador está no terreo')
        else:
            print(f'O elevador está no {andar_atual}° andar')
    elif escolha == '6':
        pessoas = elevador_criado.get_pessoas()
        print(f'Há {pessoas} pessoa(s) no elevador')
    elif escolha == '7':
        nova_cap = int(input('Qual a nova capacidade? '))
        if nova_cap < elevador_criado.get_pessoas():
            print('Há mais pessoas no elevador do que a nova capacidade permite, não podemos atualizar'
                  'o valor')
        else:
            elevador_criado.set_capacidade(nova_cap)
    elif escolha == '8':
        novo_andar = int(input('Qual o novo total de andares? '))
        if novo_andar < elevador_criado.get_andar_atual():
            print('O elevador está mais alto do que a nova quantia de andar possui. '
                  'Não podemos atualizar o total de andares.')
        else:
            elevador_criado.set_total_andar(novo_andar)
    elif escolha == '9':
        cap = elevador_criado.get_capicidade()
        total = elevador_criado.get_total_andar()
        pessoas = elevador_criado.get_pessoas()
        andar = elevador_criado.get_andar_atual()
        print(f'Estão {pessoas} pessoa(s) no elevador, cujo a capacidade é {cap} pessoas\n'
              f'Ele está no {andar}° andar, sendo que no prédio há {total} andares')
    elif escolha == '10':
        print('Muito obrigado por utilizar o sistemas de elevador!')
        break
    else:
        print('Não há ações com este valor\n')
