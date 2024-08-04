import math
def find_next_square(sq):
    if int(math.sqrt(sq)) != math.sqrt(sq):
        #"alt" x = sq**0.5 
        #return -1 if x % 1 else (x+1)**2
        output = -1
    else:   
        output =int((math.sqrt(sq)+1)**2)
    print (output)
    return output
find_next_square(144)