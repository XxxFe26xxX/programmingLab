def sum_list(my_list):

    if(len(my_list)==0):
        return(None)
        
    return(sum(my_list))

my_list = [5,10,15]
print(sum_list(my_list))