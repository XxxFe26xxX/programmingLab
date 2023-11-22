
class CSVFile():
    
    def __init__(self,name):
        
        self.name = name

    def get_data(self):
        data = []
        
        my_file = open(self.name, "r")
        next(my_file)
        for line in my_file:
            elements = line.split(',')
            elements[-1] = elements[-1].strip()
            data.append(elements)    
        return data

mio_file = CSVFile('shampoo_sales.csv')
print(mio_file.get_data())