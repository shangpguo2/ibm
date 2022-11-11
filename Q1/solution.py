def string(s, n):
    s = s.replace("S","1").replace("M","2").replace("L","3")
    s = s.split(" ")
    for i in range(n):
        if s[i][-1] == "1":
            s[i] = s[i].replace("X", "0")
        elif s[i][-1] == "3":
            s[i] = s[i].replace("X", "4")
    return s

def main():
    N = eval(input())
    shop = input()
    shop = string(shop, N)
    shop.sort()
    M = eval(input())
    if M > N:
        print("No")
        return
    cost = input()
    cost = string(cost, M)
    cost.sort()
    p, q = 0, 0
    while q < M and p < N:
        if cost[q] > shop[p]:
            p += 1
            continue
        p+=1
        q+=1
    if q != M:
        print("No")
        return
    print("Yes")

if __name__ == "__main__":
    main()