def sum_csv(my_file):
    somma = 0
    i = 0

    with open(my_file, "r"):
        for line in my_file:
            elements =  line.split(',')
            if elements[0] != 'Date':
                
                for i in range(elements):
                    value = elements[i]
                    somma = somma + value

my_file = "shampoo_sales.csv"
print(sum_csv(my_file))