# def sum(a,b):
#     print("sum:",a+b)

# sum(1,2)
# sum(10,60)
# sum(10,80)

#1. without return value without parameter

def printreport():
    print("report generated")

printreport()

#2. without return value with parameter

def printName(name):
    print("name:",name)

printName("python")
printName("java")

#3. with return value without parameter

def todaytask():
    return ["python","java","javascript"]

tasklist= todaytask()
print(tasklist)

#4. with return value with parameter
def calculatearea(radius):
    area=3.14*radius*radius
    return area

areaofcircle=calculatearea(5)
print("area of circle:",type(areaofcircle),areaofcircle)