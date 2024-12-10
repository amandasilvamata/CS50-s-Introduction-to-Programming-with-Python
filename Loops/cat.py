"""
i = 0
while i < 3 :
    print("meow")
    i += 1
    
"""

# Este código usa um loop `for` para percorrer a lista `[0, 1, 2]` e imprime "meow" três vezes, uma para cada elemento. A variável `i` assume valores, mas não é usada no corpo do loop.
'''
for i in [0, 1, 2]:
    print("meow")
'''

# O código usa um loop for com range(3) para repetir a palavra "meow" três vezes. O range(3) gera os valores 0, 1 e 2, que são usados para controlar a repetição, mas o valor de i não é utilizado diretamente no print. É uma maneira eficiente de executar ações repetitivas em Python.
'''
for i in range(3):
    print("meow")

'''

# O underscore _ em loops for em Python é usado quando você não precisa usar a variável que seria gerada pela iteração. Ele indica que o valor pode ser ignorado, deixando o código mais claro.
for _ in range(3):
    print("meow")
