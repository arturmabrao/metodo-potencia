from numpy import ones, matrix, zeros
import os


def reinicia():
    os.system('cls' if os.name == 'nt' else 'clear')

# Menu: executa / encerra
def menu(): 
    print('\n\nPara executar envie qualquer caracter.\nCaso queira encerrar envie 0 ou o campo vazio: ')
    resp = input('\nEscolha um opçao:  ')
    return resp

# Definição da matriz, de 2 x 2 ate 10 x 10
def cria_matriz():
    respm = input('\nPara usar uma matriz 6x6 pré-definida envie 0. \nPara criar a sua, de ordem entre 2 e 10, envie qualquer outro caractere: ')
    verifica = 0
    if respm == '0':
      matriz = zeros((6,6))
      matriz[0][0]=1
      matriz[0][1]=2
      matriz[0][2]=3
      matriz[0][3]=4
      matriz[0][4]=5
      matriz[0][5]=6
      matriz[1][0]=7
      matriz[1][1]=8
      matriz[1][2]=9
      matriz[1][3]=10
      matriz[1][4]=11
      matriz[1][5]=12
      matriz[2][0]=13
      matriz[2][1]=14
      matriz[2][2]=15
      matriz[2][3]=16
      matriz[2][4]=17
      matriz[2][5]=18
      matriz[3][0]=19
      matriz[3][1]=20
      matriz[3][2]=21
      matriz[3][3]=22
      matriz[3][4]=23
      matriz[3][5]=24
      matriz[4][0]=25
      matriz[4][1]=26
      matriz[4][2]=27
      matriz[4][3]=28
      matriz[4][4]=29
      matriz[4][5]=30
      matriz[5][0]=31
      matriz[5][1]=32
      matriz[5][2]=33
      matriz[5][3]=34
      matriz[5][4]=35
      matriz[5][5]=36
    else:
      while True:
          tam = int(input('\n\nInforme a Dimensao da Matriz ente 2 e 10:  '))

          if tam > 1 and tam < 11:
              break
          else:
              print('\nOpção inválida. Por favor, escolha uma ordem para sua matriz, entre 2 e 10.')
              verifica=-1

      reinicia() 

      matriz = zeros((tam,tam))
      linha = 0
      
      print(f'Monte sua matriz {tam}x{tam}')
      while linha < tam:  
          for coluna in range(tam): 
              num = int((input(f'\nEntre o valor da [{linha+1}][{coluna+1}] da matriz:  ')))
              matriz[linha][coluna]  = int(num)

          linha += 1

    return matriz


# Maior elemento de um array
def maior_elemento(elementos):
    for i in range(len(elementos)):
      if elementos[i] < 0:
        elementos[i] *= -1

    return max(elementos)

# Checa método de parada
def check_margem(c1, c2):
    c1 *= 1000000
    c2 *= 1000000
    c1 = int(c1[0])
    c2 = int(c2[0])
    if c1 == c2:
      return True

    return False
    
#  Método de potência
def metodo_potencia(matriz):

    colunas = len(matriz)
    matriz_iteracao = ones((colunas, 1))
    cc1 = [0]
    cc2 = [0]
    av = [0]
    i = 0

    # Iterações do método
    while True:
      i += 1
      cc1 = av.copy()
      matriz_iteracao = matriz * matriz_iteracao
      av = maior_elemento(matriz_iteracao)
      cc2 = av.copy()
      matriz_iteracao = matriz_iteracao*(1/av)
      # Chama verificação de parada das iterações
      if check_margem(cc1, cc2) or i > 999:
        break
 
    
    return av, i


# Executa fluxo
def main():
    print(f'\n\n{"-"*90}')
    
    resp = menu()   
    reinicia()  

    # Analisa resposta ao menu 
    if resp == '0' or resp == '':
        print(f'\n\n{"-"*26} Execução Encerrada {"-"*26}\n\n')
        exit(0)
    else:
        matriz = matrix(cria_matriz()) 

        print(f'\n\n{"-"*25}  Matriz de Escolhida {"-"*25}\n\n')
        print(matriz)
        autovalor, iteracoes = metodo_potencia(matriz)
        if iteracoes == 1000:
          iteracoes = "quantidade máxima, 1000"

        print(f'\n\n{"-"*30}  AutoValor {"-"*30}\n')
        print(f'λ:  {autovalor}')
        print(f'\nObtivemos este autovalor \n realizando: {iteracoes} iterações.')

        reinicia()

        main() 


# Inicia execução-

if __name__ == '__main__': 
    main()