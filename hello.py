print('hello world!')
x1=float(input('x1='))
y1=float(input('y1='))
x2=float(input('x2='))
y2=float(input('y2='))

while x1==x2 and y1==y2:
    print('tocke su na istom vertikalnom pravcu.unesi nove koordinate')
    x1=float(input('x1='))
    y1=float(input('y1='))
    x2=float(input('x2='))
    y2=float(input('y2='))

k=(y2-y1)/(x2-x1)
n=y1-(k*x1)
print("Jednadzba pravca koji prolazi kroz tocke ({}, {}) i ({}, {}) je: y = {}x + {}".format(x1,y1,x2,y2,k,n))



   

