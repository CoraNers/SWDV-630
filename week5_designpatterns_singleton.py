class PizzaSystemLogger(object): 
    _instance = None 

    def __new__(cls): 
        if cls._instance == None: 
            cls._instance = object.__new__(cls) 
        else:
            print('PizzaSystemLogger is already instantiated.  Singleton, so we cant recreate it')
        return cls._instance

    def __log__(self, whatToLog):
        print(whatToLog)

logger = PizzaSystemLogger()
print(logger)
logger.__log__('Test logging')

# should not work since PizzaSystemLogger is a Singleton
logger2 = PizzaSystemLogger()