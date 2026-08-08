import math

# Day 1 - 30DaysOfPython Challenge
print(3+4)  # addition(+)
print(3-4)  # substraction(-)
print(4*3)  # multiplication(*)
print(3/4)  # division(/)
print(4/3)  # division(/)
print(3**4) # exponential(**)
print(4**3) # exponential(**)
print(3%4)  # modulus(%)
print(3//4) # Floor division operator(//)
print(4%3)  # modulus(%)
print(4//3) # Floor division operator(//)

# Writing strings
print('Jane')    # Your name
print('Doe')     #Your family name
print('Algeria') # My country
print('I am enjoying 30 days of python')

# Checking data types
print(type(10))             
print(type(9.8))            
print(type(3.14))           
print(type(4-4j))           
print(type(['Asabeneh', 'Python', 'Finland']))             
print(type('Jane'))   
print(type('Doe'))   
print(type('Algeria'))   


### Exercise level 3

# Write an example of different Python data types
print(type(("Cat","dog","horse")))        #tuple
print(type({"Cat","dog", "horse"}))     #set
print(type({"Name":"Jane", "age":30}))  #dict
print(type(True))                       #bool


# Find an Euclidean distance between (2,3) and (10,8) 

## formula : racine carrée de (p1-q1)²+(p2-q2)²
print('For two points (2,3) and (10,8)')
print('(2-10)**2 = ', (2-10)**2)
print('(3-8)**2 = ', (3-8)**2)
print('(2-10)**2 + (3-8)**2 = ', (2-10)**2 + (3-8)**2)
print('La distance Euclidéenne entre les deux points (2,3) et (10,8) est : ')

print('((2-10)**2 + (3-8)**2)**0.5 =', ((2-10)**2 + (3-8)**2)**0.5)

print('math.sqrt((2-10)**2 + (3-8)**2) =', math.sqrt((2-10)**2 + (3-8)**2))
print('pow(((2-10)**2 + (3-8)**2),0.5) =', pow(((2-10)**2 + (3-8)**2),0.5))
