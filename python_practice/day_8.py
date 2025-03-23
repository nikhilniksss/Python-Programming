############## loops #################

ipl = {
    'CSK':"Chennai Super Kings",
    'MI':"Mumbai Indians"
}

for i in ipl:
    print(i)
    print(ipl[i])

team1,team2 = ("CSK","MI")
team1
team2

# unpacking dictionary

print(ipl.items())

# using loop

for team,name in ipl.items():
    print(team)
    print(name)

# break 

ipl = ['CSK','MI','RCB']
for team in ipl:
    print(team)
    if team == 'MI':
        break

for team in ipl:
    if team == 'MI':
        break
    print(team)

# continue

ipl = ['CSK','MI','RCB']
for team in ipl:
    if team == 'MI':
        continue
    print(team)


# list comprehension

ipl = ['CSK','MI','RCB']
ipl_len = []
for team in ipl:
    ipl_len.append(len(team))
ipl_len

# using comprehension

ipl_len_com = [len(team) for team in ipl]

ipl_len_com_1 = [len(team) for team in ipl if len(team)>2]

# error handling or exception handling

a = 1/0 # divide by zero exception

# normal code
try:
    a = 1/2
    print(a)
except Exception as e:
    print(e)

# error code
try:
    a = 1/0
    print(a)
except Exception as e:
    print(e)

# finally block

try:
    print("This is try")
    a = 1/0
    print(a)
except Exception as e:
    print("This is except")
    print(e)
finally:
    print("This is finally block")

try:
    print("This is try")
    a = 1/1
    print(a)
except Exception as e:
    print("This is except")
    print(e)
finally:
    print("This is finally block")

# work with files or file handling

f = open("/Users/nick_mac/Desktop/python/namastepython/test.txt",'r')
f.read()

for line in f:
    print(line)
f.close()
f.closed

# it will automatically open and close the file
with open("/Users/nick_mac/Desktop/python/namastepython/test.txt",'r') as f:
    print(f.read())

f.closed

f = open("/Users/nick_mac/Desktop/python/namastepython/test.txt",'w')
f.write("This is overwritten text")
f.close()