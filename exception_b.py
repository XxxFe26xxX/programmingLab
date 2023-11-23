
class CSVFile():
    
    def __init__(self,name):
        self.name = name
        #exception
        try:
            open(self.name, "r")
        except FileNotFoundError as notExist:
            print('Errore "{}"'.format(notExist))

    def get_data(self):
        data = []
        
        my_file = open(self.name, "r")
        next(my_file)
        for line in my_file:
            elements = line.split(',')
            elements[-1] = elements[-1].strip()
            data.append(elements)    
        return data

class NumericalCSVFile(CSVFile):
    
    def get_data(self):
        #super().get_data torna già data finito
        data = super().get_data()
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
    
mio_file = NumericalCSVFile('shampoo_sales_2.csv')
print(mio_file.get_data())