import random
import time

def w(seconds=2):
    time.sleep(seconds)

    

def tabuada_jogo():
    # Inicializa a variável pontos com zero
    pontos = 0

    
    

    # Recebe a quantidade de perguntas que serão feitas
    num_perguntas = int(input("Vamos testar seus conhecimentos na tabuada? \n Quantas perguntas você deseja responder? "))
    w()
    # Armazena as perguntas já feitas
    perguntas_feitas = []
    
    
    # Faz as perguntas
    for i in range(num_perguntas):
        # Sorteia dois números inteiros aleatórios entre 3 e 9
        x = random.randint(3, 9)
        y = random.randint(3, 9)
        
        # Verifica se a pergunta já foi feita
        while (x, y) in perguntas_feitas:
            x = random.randint(3, 9)
            y = random.randint(3, 9)
        
        # Adiciona a pergunta à lista de perguntas já feitas
        perguntas_feitas.append((x, y))
        
        # Calcula o resultado da pergunta
        resultado = x * y
        
        # Recebe a resposta do jogador
        resposta = int(input("Quanto é {} x {}? ".format(x, y)))
        
        # Verifica se a resposta está correta
        if resposta == resultado:
            print("Correto!")
            # Adiciona 1 ponto ao jogador
            pontos += 1
        else:
            print("Incorreto.")
            print("A resposta correta era {}.".format(resultado))
        w(0)    
    # Exibe a pontuação final do jogador
    print("Você fez {} pontos de {} perguntas.".format(pontos, num_perguntas))

if __name__ == '__main__':
    tabuada_jogo()


    #melhorias
    #falta corrigir a introdução, a explicação está invertida
    #falta o computador mostrar a resposta quando o usuário errar
    #falta o jogo dar a opção de reiniciar somente com as opções erradas

    #avançado:
    #adicionar um cronômetro e calcular quanto tempo o usuário demora para responder cada questão

