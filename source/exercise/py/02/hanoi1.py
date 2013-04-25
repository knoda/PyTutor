def hanoi(n,a,b,c):
    if n>0:
         hanoi(n-1,a,c,b)
         print "moving plate%s from %s to %s."%(n,a,b)
         hanoi(n-1,c,b,a)

n=int(raw_input('please input number of plates: '))

hanoi(n, 'a','b','c')
