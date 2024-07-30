https://www.interviewbit.com/problems/loops-and-jump-statements/

def main():
    N = int(input())
    # YOUR CODE GOES HERE
    for i in range(1, N):
        
        if(i % 2 == 1):
            
            print(i)
        
    return 0

if __name__ == '__main__':
    main()
