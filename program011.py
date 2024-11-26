def calculator(operation,num1,num2):
    switcher={
            "Add":num1+num2,
            "Sub":num1-num2,
            "Multiply":num1*num2,
            "Divide":num1/num2 
            }
    return switcher.get(operation,('Invalid operation'))
print(calculator("Add",(10,5)))
print(calculator("Sub",(10,5)))
print(calculator("Multiply",(10,5)))
print(calculator("Divide",(10,5)))