import compara_code as cd
import os

if __name__ == '__main__': 
    fptr = open(os.environ['OUTPUT_PATH'], 'w') 

    a = list(map(int, input().rstrip().split())) 
    b = list(map(int, input().rstrip().split()))

    result = cd.compareTriplets(a, b)
    print(result)
    fptr.write(' '.join(map(str, result))) 
    fptr.write('\n')
    fptr.close()
