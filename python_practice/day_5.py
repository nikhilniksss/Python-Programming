# list continues

sum_lst = [1,3,2,4,5,6,7]

sum_lst.sort()

alp_lst = ['C','B','A']

alp_lst.sort()

num_str = ['2','1','C','B','A']

num_str.sort()

num_str.index('C')

'1' in num_str
'5' in num_str

# list of list

lst_of_lst = [[1,2],[2,4],[5,6],['Nikhil','Kumar']]
len(lst_of_lst)

lst_of_lst[0]
lst_of_lst[0][1]
lst_of_lst[3]
lst_of_lst[3][0]

#### List copy

ipl = ['CSK',[1,2],'MI','RR',1,2]
ipl_1 = ipl

ipl.pop()
ipl
ipl_1

ipl_2 = ipl.copy()
ipl.pop()
ipl
ipl_1
ipl_2