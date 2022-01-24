import json

#name = input("Archivo con la descricion de la MT: ")
name= "M.json"
with open(name) as file:
    data = json.loads(open(name).read())
#name = input("Inserte la cadena de entrada")
string="010"

# Variables que representaran las propiedades de nuestra MT.
states = data["Estados"]
inputAlphabet = data["Entrada"]
beltAlphabet = data["Cinta"]
initialState = data["Inicial"]
white = str(data["Blanco"])
finalStates = data["Finales"]
transitions = data["Transiciones"]

#Diccionario que nos permitira representar la cinta de nuestra MT
belt = dict()

#Diccionario que nos permitira representar las trancisiones de nuestra MT
dictTransitions = dict()

# String que representa nuestro estado actual(al inicio el estado actual es el Inicial)
currentStatus = initialState

for transition in transitions:
    print(transition)
    first = (transition[0],transition[1])
    second = (transition[2],transition[3],transition[4])
    print(first, " = ",second)
    dictTransitions.setdefault(first,second)

print("Los estados de tu MT son: ", states, "\n"
        "El alfabeto de entrada de tu MT: ", inputAlphabet,"\n"
        "El alfabeto de la cinta de tu MT: ", beltAlphabet,"\n"
        "El estado inicial de tu MT: ", initialState,"\n"
        "El símbolo en blanco de la cinta: ", white,"\n"
        "El conjunto de estados finales de tu MT: ", finalStates,"\n"
        "La representacion de tus transiciones es la siguiente: ", dictTransitions,"\n")

print(type(transitions), "tipo de: ", transitions)

#Funcion que recibe una cadena y nos dice si esta formada por elementos del alfabeto
def filter(string, alphabet):
    answer = True
    for caracter in string:
        if caracter in alphabet:
            answer= True
        else:
            answer= False
    return answer

indexState = 1
#Funcion que nos permite pasar una cadena a nuestra cinta
def toBelt(belt, string):
    count = 0
    belt[count] = white
    count = count+1
    belt.setdefault(indexState, initialState)
    for caracter in string:
        count = count+1
        belt.setdefault(count, caracter)
        #belt = {count:caracter}
    count= count+1
    belt.setdefault(count,white)
    return belt

newState= "|q1|"
newCaracter = "1"
belt[indexState] = newState
aleer = indexState+1
belt[aleer] = newCaracter
str2 = belt[indexState]
indexState= indexState+1

str1 = belt[aleer]
aleer = aleer-1
belt[aleer]= str1
belt[indexState] = str2




print(beltAlphabet, type(beltAlphabet))
print(filter(string, beltAlphabet))
print(toBelt(belt, string))
dic = sorted(belt.keys())
print(dic)
str=""
for value in dic:
    str= str+(belt[value])
    #print(belt[value])
print(str)
#belt={count+1:caracter for caracter in string}
#print(type(data["Estados"]))
'''print("Estados: ", states, "\n ", input, "\n ", belt, "\n ", initialState, "\n ", white, "\n ", finalStates)
for state in states:
    print(state, "Tipo de: " ,type(state))
s=0
for transition in transitions:
    print("Transición ", s ," ;", transition)
    s = s+1'''

##print(transitions , "Tipo de: " ,transitions)
