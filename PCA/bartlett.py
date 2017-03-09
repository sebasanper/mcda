from numpy import log, var, sqrt

country = []
var_name = []
# with open("countries.dat", "r") as inp:
#     a = []
#     first_line = inp.readline()
#     cols = first_line.split(",")
#     for i in range(len(cols)):
#         if i > 0:
#             a.append([])
#         var_name.append(cols[i])
#     # inp.seek(0)  # Return reading to beginning of file
#     for line in inp:
#         col = line.split(",")
#         for j in range(len(col)):
#             if j == 0:
#                 country.append(col[j])
#             else:
#                 if col[j] == "N/A" or col[j] == "N/A\n":
#                     a[j-1].append(col[j])
#                 else:
#                     a[j-1].append(float(col[j]))

with open("diameters.dat", "r") as inp:
    num = 1
    a = [[] for _ in range(10)]
    for line in inp:
        col = line.split()
        if float(col[1]) == float(num):
            a[num - 1].append(float(col[0]))
        else:
            a[num].append(float(col[0]))
            num += 1

print a

k = len(a)
n = [len(a[i]) for i in range(len(a))]
S = [var(a[i]) for i in range(len(a))]

sum1 = 0.0
for i in range(k):
    sum1 += (n[i] - 1.0) * log(S[i])

N = 0.0
for i in range(k):
    N += n[i]

Sp = 0.0
for i in range(k):
    Sp += (n[i] - 1.0) * S[i]
Sp /= N - k

sum2 = 0.0
for i in range(k):
    sum2 += 1.0 / (n[i] - 1.0) - 1.0 / (N - k)

x2 = ((N - k) * log(Sp) - sum1) / (1.0 + (sum2) / (3.0 * (k - 1.0)))

print k
print n
print N
print S
print Sp
print x2