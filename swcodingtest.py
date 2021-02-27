def main():
    x = list(input())
    cnt = 0
    for i in range(n):
        if x[i] == '(':
            cnt += 1
        else:
            cnt += -1
    if cnt == 0:
        print('YES')
    else:
        print('NO')

if __name__=="__main__":
    main()