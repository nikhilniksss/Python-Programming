# string

city = "bangalore"
city[0]

city[4]

# reverse indexing
city[-4]

# slicing 
city[0:5]

len(city)

city[2:]

print(city[-4:-1])

city[::-1]

# strings are immutable - cannot be changed

city[1] = 'u'

# method of string
city.capitalize()
city.format()
city.casefold()
city.upper()
city.startswith('ba')
city.startswith('BA')
city.startswith('Mum')
city.upper().startswith('BA')
city.count('a')

## String concatenation

name = 'nikhil'
age = 32
type(age)

print(name+' '+'lives in bangalore and his age is'+' '+age)
print(f"{name} lives in bangalore and his age is {age}")

#take input from user

company = input()
print(f"I work in {company}")

company = "Nvidia"
print(company*2)

num = "12.4"
print(int(num))
print(int(float(num)))