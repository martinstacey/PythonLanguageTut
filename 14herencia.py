class Humano:
    def __init__(self,edad):
        self.edad = edad
        
        
    def hablar(self,mensaje):
        print.self.edad
        print mensaje        
           
class IngSistemas(Humano):
    def__init__(self):
    print 'Hola'
    def programar(self,lenguaje):
        print 'voy a programar en', lenguaje
        
class LicDerecho(Humano):
    def programar(self,de):
        print 'Debo estudiar el caso de', de        
         
pedro = Ingsitemas()
raul = LicDerecho(27)

pedro.programar('python')
raul.estudiarCaso('Pedro')

pedro.hablar('Hola')
raul.hablar('Hola, Pedro')