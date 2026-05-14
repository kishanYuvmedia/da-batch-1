name,age,city,state='','','',''
def getInput():
    name=input('Enter Your name')
    age=input('Enter your age')
    city=input('Enter your city')
    state=input('Enter you state')
    return name,age,city,state

name,age,city,state=getInput()

def printvalue():
    print('Name',name)
    print('age',age)  
    print('city',city)  
    print('state',state)      

printvalue()