arr = [1, 3, 4, 65, 45, 12]


def search(x):
    for i in range(len(arr)):

        if arr[i] == x:
            print(i)
            break

    else:
        print("not in arr")

search()

