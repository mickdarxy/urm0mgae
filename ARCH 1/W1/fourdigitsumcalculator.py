#request input
input_numbers = input()

#int and string
string_numbers = ""
calc_finalresult = 0

for i in input_numbers:
    
    
    if not string_numbers:
        string_numbers += i
    else: 
        string_numbers += "+" + i 
        
    calc_finalresult = calc_finalresult + int(i)    
    
print(f"{string_numbers}={calc_finalresult}")    