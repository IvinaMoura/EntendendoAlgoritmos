"""Problema de busca: 

* Algoritmo estudado: Pesquisa binária.
Entrada: Lista ordenada de elementos.
Se o elemento estiver na lista a busca retorna sua localização, caso contrário retorna None.
Com a pesquisa binária, você chuta um número intermediário e elimina metade dos números restantes a cada vez. 
Ideia: elimine metade dos números a cada tentativa com a pesquisa binária.

**Para uma lista de n números, a pesquisa binária precisa de log(2)n para retornar o valor correto.**
- Sempre é log na base 2, então uma pesquisa binária com 1.024 elementos = log(2)1024 == 10. Para uma lista de 1024 elementos 
necessário verificar no MÁXIMO dez deles."""
""" lista = [0,1,2,3,4,5,6,7,8,9]
item_escolhido = 5
baixo = 0
alto= len(lista)-1

# a cada tentativa você testa para o elemento central
meio = (baixo+alto)/2
chute = lista[meio]
# chute = 4 < item_escolhido = 5 
if chute < item_escolhido:
    baixo = meio + 1 """

def busca_binaria(lista, item_escolhido):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo+alto) // 2
        chute = lista[meio]

        if chute == item_escolhido:
            return meio
        if chute > item_escolhido:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

minha_lista = [1,3,5,7,9]
print(busca_binaria(minha_lista,3)) # 1
print(busca_binaria(minha_lista,-1)) # None