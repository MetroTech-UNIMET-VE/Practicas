dict_letters = {
    "M":1000,
    "D":500,
    "C":100,
    "L":50,
    "X":10,
    "V":5,
    "I":1
}

number = input("Enter romanos number:")
result = 0
ignore = False
for i,letter in enumerate(number):
    if i == 0:
        result += dict_letters.get(letter)
    else:
        if not ignore:
            if i + 1  < len(number) and dict_letters.get(letter) < dict_letters.get(number[i+1]):
                result += dict_letters.get(number[i+1]) - dict_letters.get(letter)  
                ignore = True
            else:
                result += dict_letters.get(letter)
                ignore = False 
        else:
            ignore = False 

        
print(result)

