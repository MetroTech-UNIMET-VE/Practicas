def permutaciones(array):
    set_aux = set(array)
    if len(set_aux) == 1: 
        return 0
    lista_aux = []
    for i,number in enumerate(array):
        if i == 0:
            lista_aux.append(number)
        else:
            pass
        
def main():
    array = [3,3,3]
    print(permutaciones(array))

main()