########## Tuple session #########

a = (1,2,3)

b = (1,2,3,'MI','CSK')

type(a)
type(b)

# it is similar to list but tuple is immutable

a[1] = 4
#TypeError: 'tuple' object does not support item assignment

a[0:2]

######### Dictionary ##########

ipl = {}
type(ipl)

ipl = {
    'CSK':'Chennai Team',
    'MI':'Mumbai Team'
}

type(ipl)

ipl['CSK']
ipl['MI']

# adding elements to dictionary

ipl['RCB'] = 'Bangalore Team'

ipl

# overwrite the dictionary element

ipl['CSK'] = 'Chennai Super Kings'

ipl

# delete ket value from Dict

del ipl['RCB']

ipl

# dictionary within dictionary

ipl = {
    "CSK":{'Name':'Chennai Super Kings','Captain':'MSD'},
    "MI":{'Name':'Mumbai Indians','Captain':'Rohit'}
}

ipl
ipl['CSK']['Captain']

ipl.pop('CSK')
ipl

##########  Boolean ###############

1 == 1
1 == 2

1 == 1 or 1 == 2

1 == 1 and 1 == 2

'CSK' in ipl


