import random
import os

'''
class No():
    def __init__(self, valor):
        self.valor = valor
        self.adress = None
        self.dir = None
        self.esq = None
        

class Arvore():
    def __init__(self):
        self.raiz = None
    

    def inorder(self, atual):
        if(atual != None):
            self.inorder(atual.esq)
            print("valor: ",atual.valor) 
            print("endereco: ",atual.adress,"\n")
            self.inorder(atual.dir)

    def preorder(self, atual):
        if(atual != None):
            print("valor: ",atual.valor)
            print("endereco: ",atual.adress,"\n")
            self.preorder(atual.esq)
            self.preorder(atual.dir)

    def posorder(self, atual):
        if(atual != None):
            self.posorder(atual.esq)
            self.posorder(atual.dir)
            print("valor: ",atual.valor)
            print("endereco: ",atual.adress,"\n")
    
    def inserir(self, atual, novo, adress):
        if atual != None:
            if novo.valor > atual.valor:
                adress = (adress*10)+1
                if atual.dir != None:
                    self.inserir(atual.dir, novo, adress)
                else:
                    novo.adress = adress
                    atual.dir = novo
            else:
                adress = adress*10
                if atual.esq != None:
                    self.inserir(atual.esq, novo, adress)
                else:
                    novo.adress = adress
                    atual.esq = novo
        else:
            arvore.raiz = novo
            arvore.raiz.adress = adress
        return "\nno inserido com sucesso\n"
    
    def buscar(self, atual, valor):
        if(atual == None):
            return "arvore vazia"
        if(atual.valor != valor):
            if (valor > atual.valor):
                if(atual.dir != None):
                    return self.buscar(atual.dir, valor)
                else:
                    return "Esse valor nao existe"
            else:
                if(atual.esq != None):
                    return self.buscar(atual.esq, valor)
                else:
                    return "Esse valor nao existe"
        else:
            return atual.adress
    
    def nomaximo(self, atual):
        if(atual == None):
            return "arvore vazia"
        if(atual.dir != None):
            return self.nomaximo(atual.dir)
        else:
            return atual.valor

    def nominimo(self, atual):
        if(atual == None):
            return "arvore vazia"
        if(atual.esq != None):
            return self.nominimo(atual.esq)
        else:
            return atual.valor

    def totalno(self, atual):
        if(atual == None):
            return 0
        else:
            if(atual.esq != None and atual.dir != None):
                return 1 + self.totalno(atual.esq) + self.totalno(atual.dir)
            elif(atual.esq != None and atual.dir == None):
                return 1 + self.totalno(atual.esq) 
            elif(atual.esq == None and atual.dir != None):
                return 1 + self.totalno(atual.dir)
            else:
                return 1

    def totalfolhas(self, atual):
        if(atual == None):
            return 0
        else:
            if(atual.esq != None and atual.dir != None):
                return 0 + self.totalfolhas(atual.esq) + self.totalfolhas(atual.dir)
            elif(atual.esq != None and atual.dir == None):
                return 0 + self.totalfolhas(atual.esq) 
            elif(atual.esq == None and atual.dir != None):
                return 0 + self.totalfolhas(atual.dir)
            else:
                return 1        

    def folhas(self, atual):
        def lista(valor):
            folhas.append(valor)
        if(atual == None):
            return "arvore vazia"
        else:
            if(atual.esq != None and atual.dir != None):
                return self.folhas(atual.esq) + self.folhas(atual.dir)
            elif(atual.esq != None and atual.dir == None):
                return self.folhas(atual.esq) 
            elif(atual.esq == None and atual.dir != None):
                return self.folhas(atual.dir)
            else:
                lista(atual.valor)
                return 1

    def pre(self, atual, valor):
        if(atual == None):
            return "arvore vazia"
        if(atual.valor != valor):
            if (valor > atual.valor):
                if(atual.dir != None):
                   return self.pre(atual.dir, valor)
                else:
                    return ("Esse valor nao existe")
            else:
                if(atual.esq != None):
                   return self.pre(atual.esq, valor)
                else:
                    return ("Esse valor nao existe")
        else:
            return self.altura(atual) - 1

    def nivel(self, atual, valor):
        if(atual == None):
            return "arvore vazia"
        if(atual.valor != valor):
            if (valor > atual.valor):
                if(atual.dir != None):
                    return 1 + self.nivel(atual.dir, valor)
                else:
                    return "Esse valor nao existe"
            else:
                if(atual.esq != None):
                    return 1 + self.nivel(atual.esq, valor)
                else:
                    return "Esse valor nao existe"
        else:
            return 0

    def altura(self, atual):
        if(atual.esq != None and atual.dir != None):
            direita = self.altura(atual.dir)
            esquerda = self.altura(atual.esq)
            if(direita > esquerda):
                return 1 + self.altura(atual.dir)
            else:
                return 1 + self.altura(atual.esq)
        elif(atual.esq != None and atual.dir == None):
            return 1 + self.altura(atual.esq) 
        elif(atual.esq == None and atual.dir != None):
            return 1 + self.altura(atual.dir)
        else:
            return 1

    def remover(self, atual, pai, alvo):
        if(atual == None):
            return "arvore vazia"
        #funções para repassar os valores de lugar
        def herda(alvo, pai, herdeiro):
            herdeiro.adress = alvo.adress
            if(pai != None):
                if(alvo.dir != herdeiro):
                    herdeiro.dir = alvo.dir
                if(alvo.esq != herdeiro):
                    herdeiro.esq = alvo.esq
                if(alvo.valor > pai.valor):
                    pai.dir = herdeiro 
                else:
                    pai.esq = herdeiro
            else:
                if(alvo.dir != herdeiro):
                    herdeiro.dir = alvo.dir
                if(alvo.esq != herdeiro):
                    herdeiro.esq = alvo.esq
                arvore.raiz = herdeiro
        
        def reendereca(no):
            if(no.dir != None):
                no.dir.adress = no.adress * 10 + 1
                reendereca(no.dir)
            if(no.esq != None):
                no.esq.adress = no.adress * 10
                reendereca(no.esq)

        def repoe(herdeiro, herdeiropai, repositor):
            repositor.adress = herdeiro.adress
            reendereca(repositor)
            if(herdeiro.valor > herdeiropai.valor):
                herdeiropai.dir = repositor 
            else:
                herdeiropai.esq = repositor
 
        # PROCURA O VALOR
        if(atual.valor != alvo):
            if (alvo > atual.valor):
                if(atual.dir != None):
                    self.remover(atual.dir, atual, alvo)
                else:
                    return "Esse valor nao existe"
            else:
                if(atual.esq != None):
                    self.remover(atual.esq, atual, alvo)
                else:
                    return "Esse valor nao existe"
        else:
            alvo = atual
        # DELETA
            if(alvo.dir != None):
                if(alvo.dir.esq != None):
                    herdeiro = alvo.dir.esq
                    herdeiropai = alvo.dir
                    digno = False
                    while (digno != True):
                        if(herdeiro.esq != None):
                            herdeiropai = herdeiro
                            herdeiro = herdeiro.esq
                        else:
                            digno = True
                    herdeiropai.esq = None
                    if(herdeiro.dir != None):
                        repoe(herdeiro, herdeiropai, herdeiro.dir)
                    herda(alvo, pai, herdeiro)
                else:
                    herdeiro = alvo.dir
                    herda(alvo, pai, herdeiro)
            elif(alvo.esq != None):
                if(alvo.esq.dir != None):
                    herdeiro = alvo.esq.dir
                    herdeiropai = alvo.esq
                    digno = False
                    while (digno != True):
                        if(herdeiro.dir != None):
                            herdeiropai = herdeiro
                            herdeiro = herdeiro.dir
                        else:
                            digno = True
                    herdeiropai.dir = None
                    if(herdeiro.esq != None):
                        repoe(herdeiro, herdeiropai, herdeiro.esq)
                    herda(alvo, pai, herdeiro)
                else:
                    herdeiro = alvo.esq
                    herda(alvo, pai, herdeiro)

            else:
                if(pai.valor > alvo.valor):
                    pai.esq = None
                else:
                    pai.dir = None


arvore = Arvore()



array = []
for i in range(0,15):
    array.append(i)

for i in range(0,15):
    valor = random.choice(array)
    array.remove(valor)
    no = No(valor)
    arvore.inserir(arvore.raiz, no, 1)


def digite():
    try:
        print("Digite o valor:")
        valor = input()
        valor = int(valor)
        return valor
    except:
        print("valor invalido")
        limpa()

def limpa():
    input("\n\n\ndigite enter para continuar...")
    os.system("cls")

while True:
    #os.system("cls")
    print("Digite uma opção:\n")
    print("(0) - Sair\n")
    print("(1) - Inserir no")
    print("(2) - Buscar posicao de um no")
    print("(3) - Percorrer arvore em ordem")
    print("(4) - Percorrer arvore pre ordem")
    print("(5) - Percorrer arvore pos ordem")
    print("(6) - Mostrar quantidade de nos")
    print("(7) - Mostrar quantidade de folhas")
    print("(8) - Mostrar quais nos sao folhas")
    print("(9) - Mostrar altura de um no")
    print("(10) - Mostrar nivel de um no")
    print("(11) - Remover no")
    
    folhas = []
    op = input()

    
    op = int(op)
    if(op < 0 or op > 11):
        print("opcao invalida")
    else:
        if op == 0:
            limpa()
            break
        elif op == 1:
            valor = digite()
            no = No(valor)
            print(arvore.inserir(arvore.raiz, no, 1))
            limpa()
        elif op == 2:
            valor = digite()
            print(f"Posicao de {valor}:")
            print(arvore.buscar(arvore.raiz, valor))
            limpa()
        elif op == 3:
            print("em ordem:\n")
            arvore.inorder(arvore.raiz)
            limpa()
        elif op == 4:
            print("pre ordem:\n")
            arvore.preorder(arvore.raiz)
            limpa()
        elif op == 5:
            print("pos ordem:\n")
            arvore.posorder(arvore.raiz)
            limpa()
        elif op == 6:
            print("Quantidade de nos:\n")
            print(arvore.totalno(arvore.raiz))
            limpa()
        elif op == 7:
            print("Quantidade de folhas:\n")
            print(arvore.totalfolhas(arvore.raiz))
            limpa()
        elif op == 8:
            print("Noses que sao folhas:\n")
            arvore.folhas(arvore.raiz)
            print(folhas)
            limpa()
        elif op == 9:
            valor = digite()
            print(f"Altura do no {valor}:")
            print(arvore.pre(arvore.raiz, valor))
            limpa()
        elif op == 10:
            valor = digite()
            print(f"Nivel do no {valor}:")
            print(arvore.nivel(arvore.raiz, valor))
            limpa()
        elif op == 11:
            valor = digite()
            arvore.remover(arvore.raiz, None, valor)
            limpa()
    
'''


class Vertice():
    def __init__(self, nome):
        self.nome = nome
        

class Aresta():
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2


class Grafo():
    def __init__(self):
        self.vertices = []
        self.arestas = []


    def verificaaresta(self, v1, v2):
        for i in range(0, len(self.arestas)):
            if self.arestas[i].v1.nome == v1:
                if self.arestas[i].v2.nome == v2:
                    return ("existe uma aresta entre os vertices inforamdos") 
            if self.arestas[i].v2.nome == v1:
                if self.arestas[i].v1.nome == v2:
                    return ("existe uma aresta entre os vertices inforamdos") 
        return ('nao existe uam aresta entre os vertices informados')

    
    def inserirvertice(self, nome):
        for i in range(0, len(self.vertices)):
            if(self.vertices[i].nome == nome):
                return ("ja existe um vertice com esse nome")
        vertice = Vertice(nome)
        self.vertices.append(vertice)
        return ("vertice criado com sucesso")


    def inseriraresta(self, v1, v2):
        string = self.verificaaresta(v1,v2)
        if(string != 'existe uma aresta entre os vertices inforamdos'):            
            v1valido = False
            for i in range (0, len(self.vertices)):
                if self.vertices[i].nome == v1:
                    vertice1 = self.vertices[i]
                    v1valido = True
                    break
            if (v1valido):
                v2valido = False
                for i in range (0, len(self.vertices)):
                    if self.vertices[i].nome == v2:
                        vertice2 = self.vertices[i]
                        v2valido = True
                        break
                if (v2valido):
                    aresta = Aresta(vertice1, vertice2)
                    self.arestas.append(aresta)
                else:
                    print(f'O vertice " {v2} " nao existe')
            else:
                print(f'O vertice " {v1} " nao existe')
            return ("aresta incluida com sucesso")
        else:
            return ("Ja "+string)
    

    def removearesta(self, v1, v2):
        for i in range(0, len(self.arestas)):
            if self.arestas[i].v1.nome == v1:
                if self.arestas[i].v2.nome == v2:
                    self.arestas.pop(i)
                    return("aresta removida com sucesso")
            if self.arestas[i].v2.nome == v1:
                if self.arestas[i].v1.nome == v2:
                    self.arestas.pop(i) 
                    return("aresta removida com sucesso")
        return ('nao existe uam aresta entre os vertices informados')
    
    def verticesadjacentes(self, nome):
        adjacentes = []
        for i in range(0, len(self.arestas)):
            if self.arestas[i].v1.nome == nome:
               adjacentes.append(self.arestas[i].v2.nome) 
            if self.arestas[i].v2.nome == nome:
               adjacentes.append(self.arestas[i].v1.nome)

        return adjacentes
    
    def grauvertice(self, nome):
        existe = False
        for i in range(0, len(self.vertices)):
            if(self.vertices[i].nome == nome):
                existe = True
                grau = 0
                for i in range(0, len(self.arestas)):
                    if self.arestas[i].v1.nome == nome:
                        grau += 1
                    if self.arestas[i].v2.nome == nome:
                        grau += 1


        if existe == False:
           return("nao existe um vertice com esse nome")
        else:
            return grau 
        
    
    def graumedio(self):
        qtd = len(self.vertices)
        if qtd > 0:
            grau = 0
            for i in range(0, len(self.vertices)):
                nome = self.vertices[i].nome
                for j in range(0, len(self.arestas)):
                    if self.arestas[j].v1.nome == nome:
                        grau += 1
                    if self.arestas[j].v2.nome == nome:
                        grau += 1
            return(grau/qtd)
        else:
            return 0

    def grauminimo(self):
        minimo = -1
        for i in range(0, len(self.vertices)):
            grau = 0
            nome = self.vertices[i].nome
            for j in range(0, len(self.arestas)):
                if self.arestas[j].v1.nome == nome:
                    grau += 1
                if self.arestas[j].v2.nome == nome:
                    grau += 1
            if minimo < 0:
                minimo = grau
            if grau < minimo:
                minimo = grau
        
        return minimo
    
    def graumaximo(self):
        maximo = -1
        for i in range(0, len(self.vertices)):
            grau = 0
            nome = self.vertices[i].nome
            for j in range(0, len(self.arestas)):
                if self.arestas[j].v1.nome == nome:
                    grau += 1
                if self.arestas[j].v2.nome == nome:
                    grau += 1
            if grau > maximo:
                maximo = grau
        return maximo



    def verificaconexo(self):
        qtd = len(self.vertices)
        if qtd > 0:
            lista1 = []
            lista2 = []
            conexos = 1 + self.conexo(self.vertices[0].nome, lista1, lista2)
            if qtd > conexos:
                print(qtd," :",conexos,"grafo nao conexo")
            else:
                print(qtd," :",conexos,"grafo conexo")
        else:
            return("nao exsitem vertices no grafo")
    
    def conexo(self, nome, lista1, lista2):
        print(lista2)
        
        '''
        verifica se ele ta na lista de verificados pra evitar q o grau dele seja resetado na lista 2
           nao esquece de perguntar se o laço encontrou um adjacente não verificado
        pq se ele não encontrou, vamos recorrer ao item da lista 2
        a lista 2 é uma matriz, contém nome e grau 

        percorre a lista, se o nome bater, decrementa
        logo depois exlui os zerados


        O erro é: se ele não acha ninguem, ele nao decrementa grau, ta errado isso

        '''

        print(f'{nome} entrou')

        verificado = False
        for j in range(0,len(lista1)):
            if(lista1[j] == nome):
                verificado = True
                break
        if verificado == False:
            print(f'{nome} nao eh verificado ainda')
            lista1.append(nome)
            grau = 0
            for i in range(0, len(self.arestas)):
                if self.arestas[i].v1.nome == nome:
                    grau += 1
                if self.arestas[i].v2.nome == nome:
                    grau += 1

            if grau > 1:
                print(f'{nome} tem grau {grau}')
                array = [nome, grau]
                lista2.append(array)


        encontrou = False
        for i in range(0, len(self.arestas)):
            if self.arestas[i].v1.nome == nome:
                print(f'{nome} tem como adjacente o {self.arestas[i].v2.nome}')
                verificado = False
                for j in range(0,len(lista1)):
                    if(lista1[j] == self.arestas[i].v2.nome):
                        verificado = True
                        break
                if verificado == False:
                    encontrou = True
                    print(f'o {self.arestas[i].v2.nome} nao eh verificado')
                    for k in range(0,len(lista2)):
                        if lista2[k][0] == nome:
                            lista2[k][1] -= 1
                            print(f'decrementa o grau de {nome}')
                            break
                    for k in range(0, len(lista2)):
                        if lista2[k][1] < 1:
                            print(f'{lista2[k][0]} tem grau zerado, portanto, vai ser retirado da lista2')
                            lista2.pop(k)
                    return 1 + self.conexo(self.arestas[i].v2.nome, lista1, lista2)

            if self.arestas[i].v2.nome == nome:
                print(f'{nome} tem como adjacente o {self.arestas[i].v1.nome}')
                verificado = False
                for j in range(0,len(lista1)):
                    if(lista1[j] == self.arestas[i].v1.nome):
                        verificado = True
                        break
                if verificado == False:
                    encontrou = True
                    print(f'o {self.arestas[i].v1.nome} nao eh verificado')
                    for k in range(0,len(lista2)):
                        if lista2[k][0] == nome:
                            lista2[k][1] -= 1
                            print(f'decrementa o grau de {nome}')
                            break
                    for k in range(0, len(lista2)):
                        if lista2[k][1] < 1:
                            print(f'{lista2[k][0]} tem grau zerado, portanto, vai ser retirado da lista2')
                            lista2.pop(k)
                    return 1 + self.conexo(self.arestas[i].v1.nome, lista1, lista2)
        
        if encontrou == False:
            print(f"{nome} nao encontrou nenhum adjacente nao verificado")
            for l in range(0, len(lista2)):
                if lista2[l][0] == nome:
                    lista2.pop(l)
                    print("entao ele foi retirado da lista 2")
                    break
            
        

        if(len(lista2) > 0):
            return 1 + self.conexo(lista2[0][0], lista1, lista2)
        
        return 0
               




    
                
    


                






grafo = Grafo()


nome = "uva"
grafo.inserirvertice(nome)


nome = "suco"
grafo.inserirvertice(nome)

print(grafo.inseriraresta("uva","suco"))
print(grafo.inseriraresta("uva","suco"))


nome = "banana"
grafo.inserirvertice(nome)

nome = "vitamina"
grafo.inserirvertice(nome)

nome = "couve"
grafo.inserirvertice(nome)

grafo.inseriraresta("banana","vitamina")

grafo.verificaaresta("banana","vitamina")

adjacentes = grafo.verticesadjacentes("banana")



grafo.grauvertice("banana")



grafo.removearesta("banana","vitamina")
grafo.inseriraresta("banana","vitamina")
grafo.inseriraresta("banana","uva")
grafo.inseriraresta("vitamina","suco")


grafo.grauvertice("banana")
grafo.grauvertice("uva")
grafo.grauvertice("vitamina")
grafo.grauvertice("suco")


grafo.graumedio()
grafo.grauminimo()

nome = "pera"
grafo.inserirvertice(nome)
grafo.inseriraresta("pera","uva")

grafo.graumaximo()

grafo.verificaconexo()
grafo.inseriraresta("vitamina","couve")
grafo.verificaconexo()







#print(grafo.vertices[0].nome)