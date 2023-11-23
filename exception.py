
my_file = open('/tmp.txt', 'w')
my_string = 'ciao mulo'

try:
    my_file.write(my_string)
except Exception as e:
    print('Errore di scrittura del file: "{}" '.format(e))
else:
    print('Successo')

finally:
    my_file.close()