a = ['bear', 'tiger','pig']
for i in range(len(a)):
    print (i,a[i])

print range(10)


def test(a=1, b=2):
    print ('test fucntion')
    print (a)
    print (b)
    printListNote()

def printListNote():
    test = list(range(99))
    print(test.count(88))

test()
