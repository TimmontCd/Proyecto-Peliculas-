

def menu():

    
 
    opc = 0
    Peliculas = {'Tortugas_Ninja':' B'}
        
    while opc != 6:
        print("*" * 10)
        print("   MENU ")
        print("*" * 10)
        print("[1] SUBIR PELICULA")
        print("[2] MODIFICAR PELICULA")
        print("[3] ELIMINAR PELICULA")
        print("[4] BUSCAR CLASIFICACION")
        print("[5] IMPRIMIR PELICULAS")
        print("[6] SALIR")
        try:
           opc = int(input("Opcion: "))
        except ValueError: 
           print("Error en la opcion, RECUERDA SOLO USAR ENTEROS!")   
        print("*" * 10)
        if opc == 1:
           try:
            print("ALTA")
            AltaPelicula(Peliculas)
           except:
               print("Se ha producido un error, use los caracteres correctos.")
        elif opc == 2:
               print("CAMBIO ")
               NombrePelicula = input("Inserte Nombre de la pelicula: ")
               if NombrePelicula.istitle() == True :
                   CambioPelicula(Peliculas,NombrePelicula)
               else :
                    print("Volviendo al Menu Principal, NO CARACTERES VALIDOS")    
                    print("*" * 10)
           

        elif opc == 3:
               print("BAJA")
               NombrePelicula = input("Inserte Nombre de la pelicula: ")
               if NombrePelicula.istitle() == True :
                   BajaPelicula(Peliculas, NombrePelicula)
                   print("*" * 10)
               else :
                   print("Volviendo al Menu Principal, INSERTE SOLO LETRAS")    
                   print("*" * 10)
         
        elif opc == 4:
               print("BUSQUEDA")
               Busqueda = input("Ingrese Clasificacion a Buscar: ")
               if Busqueda.istitle() == True :
                  result = Peliculas
                  print( dict(filter(lambda x: x[1] == Busqueda, result.items())))
                  print("*" * 10)
               else :
                  print("Volviendo al Menu Principal, INSERTE SOLO LETRAS")    
                  print("*" * 10)
          
        elif opc == 5:
            print("IMPRESION DE PELICULAS!!")
            print(Peliculas)
            print("")
            input("Presione Enter para continuar...")

        elif opc == 6:
            print("Adios.")    
          
def AltaPelicula(Peliculas):
   try:  
      PeliculaNombre = input("Ingrese Nombre de la Pelicula: ")
      Clasificacion= input("Inserte Clasificacion: ")
      if PeliculaNombre.istitle():
         Peliculas.update({PeliculaNombre:Clasificacion})
         print("")   
         print("Pelicula Guardada de manera CORRECTA!") 
         return Peliculas
      else:
         raise Exception  
   except:
         print("No se guardo el registro, ERROR EN EL FORMATO DEL TITULO") 
   else:
        print("")   
        print("Pelicula Guardada de manera CORRECTA!")    

def CambioPelicula(Peliculas,NombrePelicula):
 try: 
    if NombrePelicula in Peliculas:
       PeliculaNombre = input("Ingrese Nuevo NOMBRE de la Pelicula: ")
       Clasificacion= input("Inserte Clasificacion: ")
       if PeliculaNombre.istitle()==True:
          Peliculas.update({PeliculaNombre:Clasificacion})
          print("")   
          print("Pelicula Modificada de manera CORRECTA!") 
          return Peliculas
       else:
          raise Exception  
    else: 
          print("No se encontro la pelicula")
          return Peliculas   
 except:       
       print("No se guardo el registro, ERROR EN EL FORMATO DEL TITULO") 

def BajaPelicula(Peliculas, NombrePelicula):
    if NombrePelicula in Peliculas:
       Peliculas.pop(NombrePelicula)
       print("Eliminacion Correcta")
       return Peliculas
    else :
          print("No se encontro la pelicula") 
          return Peliculas



if __name__ == "__main__" :
      menu()
