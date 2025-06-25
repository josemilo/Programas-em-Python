Grifinória = 0
Corvinal = 0
LufaLufa = 0
Sonserina = 0

print('==============')
print(' Chapeu seletor')
print('==============')

print(' Q1) Você gosta da noite ou da manhã?')
print(' 1) noite')
print(' 2) manhã')

responder = int(input('Qual a sua resposta (1-2): '))

if responder == 1:
   Grifinória += 1
   Corvinal += 1
elif responder == 2:
   LufaLufa += 1
   Sonserina += 1
else:
   print('Entrada errada.')
  

  #~~~~~~~~~~~~ pergunta 2 ~~~~~~~~~#

print('Q2) Quando eu morrer, quero que as pessoas lembrem de mim como:')
print('1) Bom')
print('2) Òtimo')
print('3) Sábio')
print('4) Audacioso')

responder = int(input('Qual a sua resposta?: (1-4)'))
if responder == 1:
     LufaLufa += 2
elif responder == 2: 
     Sonserina += 2
elif responder == 3:    
     Corvinal += 2
elif responder == 4:
     Grifinória += 2
else:
      print ('Entrada errada.') 




  #~~~~~~~~~~ pergunta 3 ~~~~~~~~ 

print('Q3) Que tipo de instrumento agrada mais o seu ouvido?:') 

print('1) O violão') 
print('2) O trompete') 
print('3) O piano') 
print('4) O Tambor') 

responder = int(input('Qual a sua resposta? (1-4):'))

if responder == 1:
     Sonserina += 4
elif responder == 2:
     LufaLufa += 4
elif responder == 3:
     Corvinal += 4
elif responder == 4:
     Grifinória += 4
else:
     print('Entrada errada.')   

print('Grifinória:',Grifinória)
print('LufaLufa:'  ,LufaLufa) 
print('Corvinal: ' ,Corvinal)
print('Sonserina:' ,Sonserina) 

     # Bonus 
mais_pontos = max(Grifinória,LufaLufa,Corvinal,Sonserina)   

if Grifinória == mais_pontos:
  print(' 🦁 Grifinoria!')
elif Corvinal == mais_pontos:
  print(' 🦅 Corvinal!')
elif LufaLufa == mais_pontos:
  print('🦡 Lufa-Lufa!')
else:
  print('🐍 Sonserina!')
