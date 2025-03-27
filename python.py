sintaxis:
int(input())#reminder that input is ALWAYS a string value
print(f"text, {variableName}")#formmating Strings
listVariable = [value1, value2,value3] #can add or delete values, can hold more than 1 type
    #append(), sort(), remove(position), len(CollectionVariable)
tupleVariable = (value1,value2) #values from a tupple and immutable, cant be changed
setVariable = set() 
dicVariable = {"key1" : "value1", "key2": "value2"}
dicVariable["key"] = "value" #modifies / adds a entry to the dictionary

def FunctionNmae(parameter1,parameter2): #dont need to specify what types parameter are
    "code"
    
import pythonFile #if want to use a function will need to pythonFile.function(parameter)
from PythonFile import Function as newFunctionName #can be used as newFuncitonName(parameters)


------
OOP python
class ClassName(): #create a class
    def __init__(self, parameter1, parameter2) #function to initialize objects 
            self.variable1 = parameter1 #initialize inner variables (via parameters)
            self.variable2 = [] #variabel with a list (not parameter)
obj = ClassName(value1, value2) #create an object    

#overrideMethod in python
def overrideFunction(functionToO): #override is just a NAME not necesary
    def newFunction():
        #new code
        function()
        #new code
    return newFunction

@overrideFunction
def functionToO():
    print() #code

#lambda functions 
listOfDics.sort(key=lambda value: value["example"]) #TODO check later a better example

try:
    print() #code
except NameError: #can be anny kind of error (personalized too)
    print() #code
    sys.exit(1) #a way of ending the program, need to import sys