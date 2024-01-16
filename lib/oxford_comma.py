def oxford_comma(items):
    my_string = None
    if len(items) <= 2:
        my_string = ' and '.join(items) 
    elif len(items) == 3:        
        my_string = ', '.join(items[0:2]) + f', and {items[2]}'
    else:
        my_string = ', '.join(items[:-1]) +  f", and {items[-1]}"  
    return my_string
