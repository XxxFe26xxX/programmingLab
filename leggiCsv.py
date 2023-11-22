
def sum_csv(my_file):
    somma = 0
    
    with open(my_file, "r") as my_file: #R apre file col permesso di sola lettura READ
        #next(my_file)  #salta la prima riga dove c'è DATE,SALES
        for line in my_file:
            elements = line.split(',')
            #Controlla se nella lista elements ci sono almeno 2 elementi
            if elements[0] != 'Date' and len(elements) > 1:  
                    #float perchè ci sono valori con la virgola
                    #elements[0] contiene le date
                    #elements[1] contiene I VALORI
                    somma = somma + float(elements[1])
    #finisce il ciclo           
    #ritorno somma dopo che avrà dentro di essa tutti i valori sommati
    return somma

my_file = "shampoo_sales.csv"
print(sum_csv(my_file))

