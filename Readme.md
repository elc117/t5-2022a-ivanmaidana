# Python Orientado a Objetos

Eu observei que a programação orientada a objetos em python é bastante semelhante a de java, com algumas diferenças como na sintaxe, onde em python
eu não preciso tipar as variáveis mas java eu preciso tipar. No caso de herança múltipla o java não dá suporte, mas no python é suportado no caso de 
ocorrer o temido "Diamond of Death", o python irá chamar o método da primeira class herdado da esquerda pra direita:

Ex:<br>

     class English(object):
        def greet(self):
          print(“Hi!”)
          
     class Portuguese(object):
       def greet(self):
         print(“Oi!”)
         
     class Bilingual(English, Portuguese):
       pass
       
     if __name__ == ‘__main__’:
      Bilingual().greet()
      
Neste caso, o impasse ocorrerá quando o método greet() for chamado. Esse método será chamado da class Bilingual que herda propriedades tanto da class English 
e da class Portuguese, para não ocorrer o "Diamond of Death" o python irá chamar o método da class English, pois ele foi herdado primeiro na class Bilingual.

Observei que a função construtora no python e diferente do que em java pois ela tem a seguinte sintaxe:<br>

    def __init__(self):
Se fosse em java a função construtora da class iria ter o nome da class, mas no python ela terá o nome de init, o self equivale ao this em java.
No python as variáveis das classes são geralmente declaradas diretamente dentro das funções construtoras, já em java elas são declaradas antes, a função 
construtora apenas estabelece os seus primeiros valores. 

## Conclusão
Essas foram as principais diferenças que eu notei entre a orientação a objetos nas duas linguagens. Concluo que qualquer das duas linguagens são muito
poderosas e com vários recursos e que orientação a objetos deixa o código mais organizado e legível.

## Referências:

*[Python Orientado a Objetos](https://www.treinaweb.com.br/blog/orientacao-a-objetos-em-python)<br>
*[Herança Multipla](https://medium.com/rafaeltardivo/python-e-heran%C3%A7a-m%C3%BAltipla-como-funciona-876db0449efe)

