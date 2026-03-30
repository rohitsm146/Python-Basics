first_name = "V"
last_name = "K"
full_name = first_name + " " + last_name
print(full_name) 

greeting = "Hello! " * 3
print(greeting)  

message = "  Hello, World!  "
print(message.strip())
message1 = "AaBbCcDd World"  
print(message1.upper())
print(message1.lower())  
print(message1.replace("World", "Python")) 

text = "Python"
print(text[0])  
print(text[2])  

text = "Python Programming"
print(text[0:6])  
print(text[:6])  
print(text[7:])  

text = input("Enter input: ")
print(text.upper())
print(text.lower())
print(text.strip())
 

text  =input("Enter input : ")
s = len(text.replace(" ", ""))
print("No of characters (excluding spaces) : ", s)