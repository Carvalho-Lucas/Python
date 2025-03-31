#Bloco de código executado se condição for verdadeira.


# Operadores AND -> Todas as condições devem ser verdadeiras.

if True and True:
     print("Bloco AND Executado!!")

if True and False:
    print("Bloco AND não Executado!!")

if False and False:
    print("Bloco AND não Executado!!")

# Operadores OR, quando apenas um dos operadores for verdadeiro, toda a condição/resposta é verdadeira.

if True or False:
    print("Bloco OR Executado!!!")

if True or True:
    print("Bloco OR Executado!!")


if False or True:
    print("Bloco OR Executado!!!")

if False or False:
    print("Bloco OR não Executado!!")


# A expressão not ativo inverte o valor de ativo. Se ativo for True, então not ativo é False, e vice-versa.
ativo = True

if not ativo:
    print("Variável 'ativo' é falsa!")
else:
    print("Variável 'ativo' é verdadeira!")
