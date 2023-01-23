stairs = int(input("Enter how many stairs are: "))
result = []
cont = stairs
test_list = []

while sum(test_list) < stairs:

    if sum(test_list) + 2 < stairs:
        test_list.append(2)
    elif sum(test_list) + 1 <= stairs:
        test_list.append(1)

if test_list not in result:
    result.append(test_list)


            

    
