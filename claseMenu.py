from ClaseManejadorViajerosFrecuentes import ManejadorViajerosFrecuentes
from ClaseViajeroFrecuente import ViajeroFrecuente

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.TEST,
                            '5':self.salir
                          }
    def opcion(self, unManejadorViajeros, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op=='1' or op=='2' or op=='3' or op == '5':
            func(unManejadorViajeros)
        else:
            func()
    def salir(self, unManejadorViajeros):
        if isinstance(unManejadorViajeros, ManejadorViajerosFrecuentes):
            unManejadorViajeros.guardar("viajerosfrecuentes.csv")
        print('Usted salio del programa')


    def opcion1(self, unManejadorViajeros):
        if isinstance(unManejadorViajeros, ManejadorViajerosFrecuentes):
            unManejadorViajeros.consultarCantidadMillas()


    def opcion2(self, unManejadorViajeros):
        if isinstance(unManejadorViajeros, ManejadorViajerosFrecuentes):
            unManejadorViajeros.acumularMillas()


    def opcion3(self, unManejadorViajeros):
        if isinstance(unManejadorViajeros, ManejadorViajerosFrecuentes):
            unManejadorViajeros.canjearMillas()
    
    
    def ejecutarMenu(self, unManejadorViajeros):
        if isinstance(unManejadorViajeros, ManejadorViajerosFrecuentes):
            opcion = "0"
            while opcion != "6":
                print("Ingrese la opcion deseada")
                print("[1] Consultar cantidad de millas dado un numero de viajero frecuente")
                print("[2] Acumular millas dado un numero de viajero Frecuente")
                print("[3] Canjear millas dado un numero de viajero Frecuente")
                print("[4] Ejecutar funcion test")
                print("[5] Salir")
                opcion = input("--> ")  
                self.opcion(unManejadorViajeros, opcion)

    def TEST(self):
        viajeroPrueba = ViajeroFrecuente(1292, "238645", "Lis", "Maradona", 5000)
        print("TEST".center(100, "-"))
        print(viajeroPrueba)
        print("".center(100, "-"))