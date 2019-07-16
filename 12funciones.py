def mi_funcion(num1=0,num2=0):
    print num1+num2

mi_funcion(2,3)

def mi_funcion2(cad,v=2):
    print cad*v

mi_funcion2('pamelachu',5)

def mi_funcion3(cad,v=2,*algomas):
    print cad*v
    for cadena in algomas:
        print cadena * v
mi_funcion3('pamelachu',5,'que fuef ',' ques de vos ve ')

def mi_funcion4(cad,v=2,**algomas):
    print cad*v
    for cadena in algomas:
        print cadena * v
        print algomas['cadenaextra']
        print algomas['cadenademas']
mi_funcion4('pamelachu',5,cadenaextra = 'hola')
