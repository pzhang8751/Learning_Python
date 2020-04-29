def MergeSort(x):
    if len(x) > 1:
        mid = len(x)//2
        L = x[:mid]
        R = x[mid:]

        MergeSort(L)
        MergeSort(R)

        a = b = c = 0

        while a < len(L) and b < len(R):
            if L[a] < R[b]:
                x[c] = L[a]
                a += 1
            else:
                x[c] = R[b]
                b += 1
            c += 1

        while a < len(L):
            x[c] = L[a]
            a += 1
            c += 1

        while b < len(R):
            x[c] = R[b]
            b += 1
            c += 1

        print(x)

MergeSort([12, 11, 16, 8, 9, 4, 13, 5, 12])
