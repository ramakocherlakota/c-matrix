from sympy import Matrix, zeros, diag, Rational
import sys

n = int(sys.argv[1])

def dump_matrix(m):
    print("<table border cellpadding=3>")
    for i in range(n):
        row = m.row(i)
        print("<tr>")
        for j in range(n):
            cell = row[j]
            print("<td align=right>{}</td>".format(cell))
        print("</tr>")
    print("</table>")

def rshift(row):
    newrow = row.col_insert(0, Matrix([0]))
    newrow.col_del(n)
    return newrow

def justone(i, j):
    if i==0 and j==0:
        return 1
    else:
        return 0

mat = Matrix(1, n, justone)

for j in range(n-1):
    addend1 = rshift(mat.row(j)) * Rational(1,j+1)
    addend2 = - mat.row(j) * Rational(j,j+1)
    sum = addend1 + addend2
    mat = mat.row_insert(j+1, sum)

imat = mat**(-1)

dump_matrix(mat)
print("<p>")
dump_matrix(imat)

