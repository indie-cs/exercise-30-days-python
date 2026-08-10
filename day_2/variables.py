# Day 2: 30 days of python programming

first_name = 'Jane'
last_name = 'Doe'
full_name = 'Ibrahim Maza'
country ='Algeria'
city='Cherchell'
age=45
year=2010
is_married=False
is_true = True
is_light_on = True
#first_name,last_name, full_name= 'Jane','Doe','Ibrahim Maza'


# Level 2
 

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))



# comparing the len of first name and last
if len(first_name)>len(last_name):
    print(first_name, ', the first name is longer')
else:
    print(last_name, ', the last name is longer')


# arithmetics
num_one=5
num_two=4
res_sum         = num_one+num_two
res_subs        = num_two-num_one
res_mult        = num_one*num_two
res_div         = num_one/num_two
res_mod         = num_two/num_one
res_pow         = num_one**num_two
floor_division  = num_one//num_two

print(res_sum)
print(res_subs)
print(res_mult)
print(res_div)
print(res_mod)
print(res_pow)
print(floor_division)

rad_circle=30
pi=3.14
area_of_circle=pi*(rad_circle**2)
circum_of_circle=2*pi*rad_circle

input('Radius :')
