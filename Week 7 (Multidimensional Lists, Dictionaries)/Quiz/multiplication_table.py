def multiplication_table(m):
    output=[]
    col = 0

    for rows in range(m):
        temp=[]
        col+=1
        row=col
        for columns in range(m):
            temp.append(row)
            row+=1
        output.append(temp)
    return output

m = 4
print(multiplication_table(m))
