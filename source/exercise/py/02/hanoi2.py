def hanoi(n,a,b):
    if n>0:
         hanoi(n-1,a,total[0])
         print "moving plate%s from %s to %s."%(n,a,b)
         hanoi(n-1,total[0],b)

n=int(raw_input('please input number of plates: '))

total=['a','b','c']
total.remove('a')
total.remove('b')

hanoi(n, 'a','b')
