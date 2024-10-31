def get_triangle(n, value):
    triangle = []
    for i in range(n):
        row = []
        triangle.append(row)

        for j in range(i+1):
            row.append(value)

    return triangle
print(get_triangle(5, 10))

