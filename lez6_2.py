
class CSVFile():

    def __init__(self, name):
        # Setto il nome del file
        self.name = name
        #
        if not isinstance(name, str):
            raise TypeError('Nome del file deve essere una stringa')
        self.name = name
        
        # Provo ad aprirlo e leggere una riga
        self.can_read = True
        try:
            #provo ad aprirlo
            my_file = open(self.name, 'r')
            #provo a leggere la prima riga
            my_file.readline()
        except Exception as e:
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(e))
        
    
    def get_data(self, start=1, end=10):
        
        data = []

        my_file = open(self.name, "r")
        #
        for _ in range(start):
            next(my_file)
        for _ in range(start, end+1):
        #  
            line = my_file.readline()
            elements = line.split(',')
            elements[-1] = elements[-1].strip()
            data.append(elements)    
        return data

class NumericalCSVFile(CSVFile):

    def get_data(self, start, end):
        #super().get_data torna già data finito
        data = super().get_data(start, end)
        # elements è ottenuto sempre dallo split
        for elements in data:
            #exception 2
            try:
                if not elements[-1].isnumeric():
                    #raise non va bene
                    raise Exception("Errore")
            except Exception as e:
                print('Errore "{}"'.format(e))
            #fine exception 2
            elements[-1] = float(elements[-1])  
        return data
        
mio_file = CSVFile('shampoo_sales_2.csv')
print(mio_file.get_data())