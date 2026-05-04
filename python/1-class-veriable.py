name='rajesh kumar'
print(type(name)) #string
number=10
print(type(number)) #integer
float_number=10.5
print(type(float_number)) #float
city=['delhi','mumbai','kolkata'] #list
print(type(city))
print(city) #list allows duplicate values
state=('delhi','mumbai','kolkata','kolkata') #tuple
print(type(state))
print(state) #tuple allows duplicate values
country={'delhi','mumbai','kolkata','kolkata'} #set
print(type(country)) #set
print(country) #set does not allow duplicate values

student={
        'name':'rajesh',
         'age':30,
         'city':'delhi'
         } #dictionary
print(type(student)) #dictionary
print(student) #dictionary allows duplicate values but keys must be unique

numberv=1100+10j #complex number
print(type(numberv)) #complex number
print(numberv)
print(numberv.real) #real part of complex number
print(numberv.imag) #imaginary part of complex number

a=10
b=11
print(id(a)) #memory address of a
print(id(b)) #memory address of b