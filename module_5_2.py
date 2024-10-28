def getmatrix(n, m, value):
    matrix=[]
    for i in range(n):
        row=[]
        matrix.append(row)
        for j in range(m):
            row.append(value)

    return matrix
print(getmatrix(2, 2, 10))
print(range(12))