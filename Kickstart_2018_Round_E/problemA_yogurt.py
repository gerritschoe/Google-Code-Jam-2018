#f = open("test_input.txt",'r')
#output=open("test_output_generated.txt",'w')
#f = open("A-small-practice.in",'r')
#output=open("A-small-practice_output.txt",'w')
f = open("A-large-practice.in",'r')
output=open("A-large-practice_output.txt",'w')

input = f.readline
t = int(input()) # number of cases

for cnum in range(1, t + 1):
    N, K = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    #A = [int(n) for n in input().split(" ")]
    A = input().strip().split()
    A = list(map(int, A))
    A = sorted(A)
    #print('A = ', A)
    eaten = 0
    for i in range(max(A)):
        if A == []:
            break
        checkFirst = False
        while checkFirst == False:
            if A[0] == i:
                A.pop(0)
            else:
                checkFirst = True
        for j in range(K):
            if A == []:
                break
            A.pop(0)
            eaten = eaten + 1
    ans = eaten
    #print("Case #%d: %d" % (cnum, ans))
    print("Case #%d: %d"%(cnum,ans),file=output)

f.close()
output.close()
print('Input file closed:',f.closed)
print('Output file closed:',output.closed)
