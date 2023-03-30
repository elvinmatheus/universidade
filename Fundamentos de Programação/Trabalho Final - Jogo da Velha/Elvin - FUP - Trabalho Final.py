#Discente: Elvin Matheus Sousa da Silva
#Matricula: 497516

def matriz(lins, cols, val_inic):
     m = [[val_inic] * cols for _ in range(lins)]
     return m

v = matriz(3,3," ")
jogador = [None] * 2
placar = [0,0,0]
     
#Procedimento para layout do jogo da velha
def jogodavelha():
  print('----------------')
  print('   A   B   C ')
  print('1 ',v[0][0],'|',v[0][1],'|',v[0][2],' 1')
  print('  ---+---+---')
  print('2 ',v[1][0],'|',v[1][1],'|',v[1][2],' 2')
  print('  ---+---+---')
  print('3 ',v[2][0],'|',v[2][1],'|',v[2][2],' 3')
  print('   A   B   C ')
  print('----------------')

#Escolha dos simbolos por cada jogador
def simbolo():
  jogador[0] = str(input('Jogador 1, escolha um simbolo entre X ou O para comecar a jogar: ')).upper()
  if jogador[0] == 'X':
    print('Jogador 1, você escolheu',jogador[0])
    jogador[1] = 'O'
    print('Jogador 2, o seu simbolo é',jogador[1])
  elif jogador[0] == 'O':
    print('Jogador 1, você escolheu',jogador[0])
    jogador[1] = 'X'
    print('Jogador 2, o seu simbolo é',jogador[1])
  else:
    print('Simbolo não aceito.')
    simbolo()
 
#Procedimento para continuar
def continuar():
  continuar = str(input('Desejas continuar? S/N: '))
  if continuar == 'S' or continuar == 's' or continuar == 'sim' or continuar == 'SIM':
    for i in range(3):
      for j in range(3):
        v[i][j] = " "
    jogo()
  if continuar == 'N' or continuar == 'n' or continuar == 'nao' or continuar == 'NAO': 
    print('Saindo...')
    quit()

#Procedimento para o placar
def p(x):
  print('----------------')
  print('PLACAR')
  if x == 0:
    placar[0] = placar[0] + 1
    print('Jogador 1: {}'.format(placar[0]))
    print('Jogador 2: {}'.format(placar[1]))
    print('Empate: {}'.format(placar[2]))
    print('----------------')
  if x == 1:
    placar[1] = placar[1] + 1
    print('Jogador 1: {}'.format(placar[0]))
    print('Jogador 2: {}'.format(placar[1]))
    print('Empate: {}'.format(placar[2]))
    print('----------------')
  if x == 8:
    placar[2] = placar[2] + 1
    print('Jogador 1: {}'.format(placar[0]))
    print('Jogador 2: {}'.format(placar[1]))
    print('Empate: {}'.format(placar[2]))
    print('----------------')
  continuar()
  
#Entrada de valores na matriz do jogo da velha
def entrada(a):
  jogada = a
  while jogada < 9:
    k = jogada % 2
    e = str(input('Jogador {}, entre com a posicao em que desejas marcar um simbolo: '.format(k+1))).upper()
    for ch in e:
      if ch != ',' and ch.isalpha():
        coordenada_x = ch
      elif ch.isdigit():
        coordenada_y = ch
###Verifica se a entrada eh adequada
    if coordenada_x != 'A' and coordenada_x != 'B' and coordenada_x != 'C':
      print('Entrada nao aceita. Insira uma entrada valida.')
      entrada(jogada)
    elif coordenada_x == 'A':
      j = 0
    elif coordenada_x == 'B':
      j = 1
    elif coordenada_x == 'C':
      j = 2
    if coordenada_y != '1' and coordenada_y != '2' and coordenada_y != '3':
      print('Entrada nao aceita. Insira uma entrada valida.')
      entrada(jogada)
    elif coordenada_y == '1':
      i = 0
    elif coordenada_y == '2':
      i = 1
    elif coordenada_y == '3':
      i = 2
    
    #Atribui o simbolo ao elemento da matriz e 'marca' no jogo da velha
    v[i][j] = jogador[k]
    jogodavelha()

    #Condicoes de vitoria iminente
    if jogada == 4:
      if v[0][0] == v[2][2] == v[0][2] != ' ' and v[1][1] == ' ':
        print('Nao ha mais movimentos disponiveis. Jogador {} venceu!'.format(k+1))
        p(k)
        quit()
      if v[0][0] == v[2][2] == v[2][0] != ' ' and v[1][1] == ' ':
        print('Não ha mais movimentos disponiveis. Jogador {} venceu!'.format(k+1))
        p(k)
        quit()
      if v[0][0] == v[2][0] == v[0][2] != ' ' and v[1][1] == ' ':
        print('Não ha mais movimentos disponiveis. Jogador {} venceu!'.format(k+1))
        p(k)
        quit()
      if v[2][0] == v[2][2] == v[0][2] != ' ' and v[1][1] == ' ':
        print('Não ha mais movimentos disponiveis. Jogador {} venceu!'.format(k+1))
        p(k)
        quit()
      if v[2][0] == v[2][2] == v[1][1] != ' ' and v[0][0] == v[0][2] == ' ':
        print('Não ha mais movimentos disponiveis. Jogador {} venceu!'.format(k+1))
        p(k)
        quit()
      if v[0][2] == v[2][2] == v[1][1] != ' ' and v[0][0] == v[2][0] == ' ':
        print('Não ha mais movimentos disponiveis. Jogador {} venceu!'.format(k+1))
        p(k)
        quit()
      if v[0][0] == v[2][0] == v[1][1] != ' ' and v[2][2] == v[0][2] == ' ':
        print('Não ha mais movimentos disponiveis. Jogador {} venceu!'.format(k+1))
        p(k)
        quit()
      if v[0][0] == v[0][2] == v[1][1] != ' ' and v[2][2] == v[2][0] == ' ':
        print('Não ha mais movimentos disponiveis. Jogador {} venceu!'.format(k+1))
        p(k)
        quit()
    
    #Demais condiçoes de vitoria
    if jogada >= 4:
      for i in range(3):
        if v[i][0] == v[i][1] == v[i][2] != ' ':
          print('Jogador {} venceu!'.format(k+1))
          p(k)
          quit()
        if v[0][i] == v[1][i] == v[2][i] != ' ':
          print('Jogador {} venceu!'.format(k+1))
          p(k)
          quit()
      if v[0][0] == v[1][1] == v[2][2] != ' ':
        print('Jogador {} venceu!'.format(k+1))
        p(k)
        quit()
      if v[0][2] == v[1][1] == v[2][1] != ' ':
        print('Jogador {} venceu!'.format(k+1))
        p(k)
        quit()
    if jogada == 8:
      print('Empatou!')
      p(jogada)
    jogada = jogada + 1

def jogo():
  print(' JOGO DA VELHA')
  jogodavelha()
  simbolo()
  entrada(0)
  
jogo()
