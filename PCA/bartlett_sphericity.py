from numpy import array, std, average, log, cov, sqrt
from scipy.stats.stats import pearsonr
from numpy import corrcoef
from numpy.linalg import det, inv
a = []
country = []
var_name = []
with open("countries.dat", "r") as inp:
    first_line = inp.readline()
    cols = first_line.split(",")
    for i in range(len(cols)):
        if i > 0:
            a.append([])
        var_name.append(cols[i])
    # inp.seek(0)  # Return reading to beginning of file
    for line in inp:
        col = line.split(",")
        for j in range(len(col)):
            if j == 0:
                country.append(col[j])
            else:
                if col[j] == "N/A" or col[j] == "N/A\n":
                    a[j-1].append(col[j])
                else:
                    a[j-1].append(float(col[j]))

data = array(a).transpose()
n = len(data[0])

# Standardisation procedure of the data. a --> b

sig = [0 for _ in range(n)]  # Standard deviation
av = [0 for _ in range(n)]  # Average
b = [[0 for _ in range(len(a[0]))] for _ in range(n)]

for i in range(n):
    sig[i] = std(a[i])
    av[i] = average(a[i])

for i in range(n):
    for j in range(len(a[0])):
        b[i][j] = (a[i][j] - av[i]) / sig[i]

# Correlation matrices with two identical functions.

mat1 = [[0 for _ in range(n)] for _ in range(n)]
mat2 = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        mat1[i][j] = corrcoef(b[i], b[j])[0]
        mat2[i][j] = pearsonr(b[i], b[j])[0]

mat_cov = cov(b)
# print mat_cov

partial_corr = inv(mat2)
print partial_corr
print
mat_partial = [[- partial_corr[i][j] / sqrt(partial_corr[i][i] * partial_corr[j][j]) for i in range(n)] for j in range(n)]
print mat_partial
# d = det(array(mat2))

p = len(a)
# nn = len(a[0])
# print float(p) / float(n - 1)
# x2 = - (nn - 1.0 - (2.0 * p + 5.0) / 6.0) * log(d)
# print x2
#  KMO Test
for i in range(p):
    sum1 = 0.0
    for j in range(p):
        if i != j:
            sum1 += mat2[i][j] ** 2.0

for i in range(p):
    sum2 = 0.0
    for j in range(p):
        if i != j:
            sum2 += mat_partial[i][j] ** 2.0

print sum1 / (sum1 + sum2)
