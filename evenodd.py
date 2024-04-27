
if __name__ == '__main__':
    n = int(input().strip())
def weird_ness(n):
    if(n%2 != 0):
        print("weird")
    else:
        if(n>=2 and n<=5):
            print("not weird")
        elif(n>=6 and n<=20):
            print("weird")
        elif(n%2==0 and n>=20):
            print("not weird")