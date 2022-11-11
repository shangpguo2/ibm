n = eval(input())
dataset = []
for i in range(n):
    dataset.append(input().split())

errorCodes = []
for data in dataset:
    if data[1] == "false":
        errorCodes.append(data[2])
if len(errorCodes) != 0:
    print("No")
    print(" ".join(errorCodes))
else:
    print("Yes")

