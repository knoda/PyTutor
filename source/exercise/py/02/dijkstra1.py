import sys

N=8
M=9999

a=[[0,0,0,0,0,0,0,0,0],
   [0,0,1,7,2,M,M,M,M],
   [0,1,0,M,M,2,4,M,M],
   [0,7,M,0,M,M,2,3,M],
   [0,2,M,M,0,M,M,5,M],
   [0,M,2,M,M,0,1,M,M],
   [0,M,4,2,M,1,0,M,6],
   [0,M,M,3,5,M,M,0,2],
   [0,M,M,M,M,M,6,2,0]]

leng=[M]*(N+2)
v=[0]*(N+2)

start=int(raw_input('Input start number: '))
    
leng[start]=0

for j in range(1,N+1):
    min=M;
    for k in range(1,N+1):
        if v[k]==0 and leng[k]<min:
            p=k
            min=leng[k]
    v[p]=1

    if min==M:
        print'graph is not connected.'
        sys.exit()

    for k in range(1,N+1):
        if leng[p]+a[p][k] < leng[k]:
            leng[k]=leng[p]+a[p][k]

for j in range(1,N+1):
    print "%d -> %d : %d" %(start,j,leng[j])
                        
