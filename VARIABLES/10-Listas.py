lenguajes=["Python","Ruby", "PHP","Javascript","Java"]
#indice       0       1      2         3         4 
print(lenguajes[0]) # de esta manera se solicita un indice en espcial correspondiente al dato
lenguajes[1]="HTML" # cuando quiero cambiar algun dato de la lista, cambiamos el valor del indice 1 "Rubi" por "HTML"
print(lenguajes)
print(lenguajes[-1]) #imprime el ultimo esta manera es una solicitud DESCENDENTE
print(lenguajes[-2]) #imprime el antepenultimo y asi sucesivamente dependiendo del dato que solicite 
#RECORDEMOS que hemos cambiado el valor del indice 1 "Rubi" por "HTML"
print(lenguajes[1:3])#imprime los elementos que queremos seleccionar "de donde : hasta donde", 
      #el 1 significa desde donde queremos que empiece : y el 3 hasta donde queremos que muestre, 
      # no va a incluir el valor 3 porque ese es el limite de busqueda.
print(lenguajes[:3])# de esta manera quiere decir que va a incluir desde el indice cero :3 por mas
                    #que no este escrito queda implicito
print(lenguajes[1:])#igualmente de esta manera, va a mostrar desde el indice indicado hasta el final,
#ya que al no tener un parametro de busqueda final, se sobreentiende que quiere que muestre los valores hasta el final                  
      