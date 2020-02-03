# compile string source to code  
code_str = 'a=10\nb=20\nprint("Sum :",a+b)'  
code = compile(code_str, 'add.py','exec')  
print(type(code))  
exec(code)  

