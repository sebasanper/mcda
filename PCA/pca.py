from numpy import array, std, average
from scipy.stats.stats import pearsonr
from numpy import corrcoef
from matplotlib.mlab import PCA

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
    for j in range(i, n):
        mat1[i][j] = corrcoef(a[i], a[j])[0]
        mat2[i][j] = pearsonr(a[i], a[j])[0]

print "\n======= PEARSON CORRELATION COEFFICIENT SCIPY===========\n"
s = [[str(e) for e in row] for row in mat1]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = ' '.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print '\n'.join(table)

print "======= PEARSON CORRELATION COEFFICIENT NUMPY ===========\n"
s = [[str(e) for e in row] for row in mat2]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = ' '.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print '\n'.join(table)

# Execute PCA
results = PCA(data, standardize=True)
print
print "======= EIGENVALUES ===========\n"
eigen = results.s / float(len(a[0]))
print eigen
print
print "======= PERCENTAGE OF VARIANCE ===========\n"
perc = results.fracs * 100.0
print perc
with open("percentage.dat", "w") as outperc:
    k = 0
    for i in perc:
        k += 1
        outperc.write("{1:d} {0:f} {2:f}\n".format(i, k, eigen[k-1]))
print
print "======= CUMULATIVE PERCENTAGE ===========\n"
cumul = []
suma = 0.0
for i in perc:
    suma += i
    cumul.append(suma)
print cumul
print
print "======= WEIGHTS OF PRINCIPAL COMPONENTS ===========\n"
print -results.Wt
print
print "======= PRINCIPAL COMPONENTS ===========\n"
z = [[0 for _ in range(len(data))] for _ in range(n)]
for i in range(n):
    for k in range(len(data)):
        sum2 = 0.0
        for j in range(n):
            sum2 += -results.Wt[i][j] * b[j][k]
        z[i][k] = sum2
print z
print

with open("plot_countries.dat", "w") as output:
    for i in range(len(a[0])):
        output.write("{0:s} {1:f} {2:f} {3:f} {4:f}\n".format(country[i], z[0][i] - min(z[0]) / (max(z[0]) - min(z[0])), z[1][i] - min(z[1]) / (max(z[1]) - min(z[1])), z[0][i], z[1][i]))

PCA1 = [[0 for _ in range(n)] for _ in range(n)]
print "======= CORRELATION BETWEEN VARIABLES AND PRINCIPAL COMPONENTS ===========\n"
for l in range(n):
    for j in range(n):
        PCA1[l][j] = pearsonr(b[j], z[l])[0]
    print PCA1[l]
print

print "======= VALUES OF COMMUNALITY ===========\n"
for i in range(n):
    print PCA1[0][i] ** 2.0 + PCA1[1][i] ** 2.0

print "======= FACTOR SCORES ===========\n"
cos = []
for h in range(2):
    cos.append([])
    for j in range(len(a[0])):
        norm = 0.0
        for i in range(n):
            norm += b[i][j] ** 2.0
        cos[h].append(z[h][j] ** 2.0 / norm)
print "\t======Cos^2_1============"
print cos[0]
print
print "\t======Cos^2_2============"
print cos[1]
print

QL = []
for i in range(len(cos[0])):
    QL.append(cos[0][i] + cos[1][i])
print "\t======QL============"
print QL
print
CTR = []
for h in range(2):
    CTR.append([])
    for j in range(len(a[0])):
        CTR[h].append(z[h][j] ** 2.0 / float(len(a[0])) / eigen[h] * 100.0)

print "\t======CTR1============"
print CTR[0]
print
print "\t======CTR2============"
print CTR[1]
print
