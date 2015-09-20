## Power System Load Flow Analysis by Lynn Powell
import numpy as np
#Formulation of Ybus by singular transformation method for an IEEE 14 bus
#system
#         |  From |  To   |   R     |   X     |     B/2  |  X'     |
#         |  Bus  | Bus   |  pu     |  pu     |     pu   | TAP (a) |
linedata = np.array([
            [1,     2,      0.01938,  0.05917,   0.0264,        1],
            [1,     5,      0.05403,  0.22304,   0.0246,        1],
            [2,     3,      0.04699,  0.19797,   0.0219,        1],
            [2,     4,      0.05811,  0.17632,   0.0170,        1],
            [2,     5,      0.05695,  0.17388,   0.0173,        1],
            [3,     4,      0.06701,  0.17103,   0.0064,        1],
            [4,     5,      0.01335,  0.04211,   0.0,           1],
            [4,     7,      0.0,      0.20912,   0.0,       0.978],
            [4,     9,      0.0,      0.55618,   0.0,       0.969],
            [5,     6,      0.0,      0.25202,   0.0,       0.932],
            [6,    11,      0.09498,  0.19890,   0.0,           1],
            [6,    12,      0.12291,  0.25581,   0.0,           1],
            [6,    13,      0.06615,  0.13027,   0.0,           1],
            [7,     8,      0.0,      0.17615,   0.0,           1],
            [7,     9,      0.0,      0.11001,   0.0,           1],
            [9,    10,      0.03181,  0.08450,   0.0,           1],
            [9,    14,      0.12711,  0.27038,   0.0,           1],
            [10,   11,      0.08205,  0.19207,   0.0,           1],
            [12,   13,      0.22092,  0.19988,   0.0,           1],
            [13,   14,      0.17093,  0.34802,   0.0,           1]])
#linedata = np.rec.fromrecords(linedata, dtype = {'names': ['from', 'to', 'R', 'X', 'B', 'tap'], 
#         'formats': ['<i4', '<i4', '<f8', '<f8', '<f8', '<f8']})

frombus = linedata[:,0]
tobus = linedata[:,1]
R = linedata[:,2]               # Resistance, R...
X = linedata[:,3]               # Reactance, X...
B = 1j*linedata[:,4]            # Ground Admittance, B/2...
a = linedata[:,5]               # Tap setting value..
Z = R+1j*X                      # z matrix...
y = 1./Z
busvec = np.unique(np.concatenate((frombus,tobus)))
buses = len(busvec) # No. of buses...
elements = len(frombus)                   # No. of elements...
Yprimitive = np.zeros((elements+buses,elements+buses), complex)
A=np.zeros((elements+buses,buses))
np.fill_diagonal(A,1)           #Calculation of Incidence matrix 
for i in np.arange(elements):
    A[buses:,][i,np.where(busvec==frombus[i])] = 1
    A[buses:,][i,np.where(busvec==tobus[i])] = -1

for i in np.arange(elements):
    Yprimitive[buses+i,buses+i] = y[i]/a[i]
    Yprimitive[frombus[i],frombus[i]] = Yprimitive[frombus[i],frombus[i]]+B[i]+(1-a[i])*y[i]/a[i]**2
    Yprimitive[tobus[i],tobus[i]] = Yprimitive[tobus[i],tobus[i]]+B[i]+(a[i]-1)*y[i]/a[i]**2
Y = np.dot(A.T,np.dot(Yprimitive,A))

##Reference System
##The system base quantities are VA<sub>base</sub> = 100 MVA and V<sub>base</sub> = 132 kV

import numpy as np
vabase = 100.
vbase = 132.
loaddata = np.array([
                     [1,  0,  0],
                     [2, 40, 20],
                     [3, 25, 15],
                     [4, 40, 20],
                     [5, 50, 20]])

linedata = np.array([
                     [1,  2,  0.05,  0.11,  0.02],
                     [1,  3,  0.05,  0.11,  0.02],
                     [1,  5,  0.03,  0.08,  0.02],
                     [2,  3,  0.04,  0.09,  0.02],
                     [2,  5,  0.04,  0.09,  0.02],
                     [3,  4,  0.06,  0.13,  0.03],
                     [4,  5,  0.04,  0.09,  0.02]])

frombus = linedata[:,0]
tobus = linedata[:,1]
R = linedata[:,2]               
X = linedata[:,3]               
B = 1j*linedata[:,4]             
Z = R+1j*X          
y = 1./Z
slack = 1
busvec = np.unique(np.concatenate((frombus,tobus)))
buses = len(busvec) 
elements = len(frombus)                   
Yprimitive = np.zeros((elements+buses,elements+buses), complex)
A=np.zeros((buses+elements,buses),complex)
np.fill_diagonal(A,1)   
for i in np.arange(elements):
    A[buses:,][i,np.where(busvec==frombus[i])] = 1
    A[buses:,][i,np.where(busvec==tobus[i])] = -1   

for i in np.arange(elements):
    Yprimitive[buses+i,buses+i] = y[i]+B[i]/2.
    Yprimitive[frombus[i],frombus[i]] = Yprimitive[frombus[i],frombus[i]]
    Yprimitive[tobus[i],tobus[i]] = Yprimitive[tobus[i],tobus[i]]
#Y = np.dot(A.T,np.dot(Yprimitive,A))
Y = np.dot(np.dot(A.T,Yprimitive),A)
print Y

#Direct method of Ybus formation
Y = np.zeros((buses,buses),complex)
b = np.zeros((buses,buses),complex)

for i in np.arange(elements):
    Y[np.where(frombus[i]==busvec),np.where(tobus[i]==busvec)] = Y[np.where(frombus[i]==busvec), \
                                                                   np.where(tobus[i]==busvec)]-y[i]
    Y[np.where(tobus[i]==busvec),np.where(frombus[i]==busvec)] = Y[np.where(frombus[i]==busvec), \
                                                                   np.where(tobus[i]==busvec)]
    b[np.where(frombus[i]==busvec),np.where(tobus[i]==busvec)] = b[np.where(frombus[i]==busvec), \
                                                                   np.where(tobus[i]==busvec)]+B[i]/2.
    b[np.where(tobus[i]==busvec),np.where(frombus[i]==busvec)] = b[np.where(frombus[i]==busvec), \
                                                                   np.where(tobus[i]==busvec)]
for i in np.arange(buses):
    for j in np.arange(i+1,buses):
        Y[i,i] = Y[i,i]-Y[i,j]+b[i,j]
    for j in np.arange(i):
        Y[i,i] = Y[i,i]-Y[i,j]+b[i,j]
print Y

##Jacobi Method

Yaa = Y[1:buses,1:buses]
Yab = Y[0:buses-1,0]
Ybb = Y[0,-1]
Yeq = Yaa - np.dot(Yab,np.dot(1/Ybb,Yab.T)) #Kron reduction
print Yeq

np.delete(Y[:,2],2).sum() #verify a few calculations

ld = -1*np.conj(loaddata[:,1]+1j*loaddata[:,2])/vabase
vg = np.ones(buses,complex)
b = np.divide(ld,np.conj(vg))
b, np.conj(vg), np.arange(1,buses)

v = vg
for k in np.arange(5):
    b = np.divide(ld,np.conj(v))
    v = np.append((1+0j),[(b[i]-np.dot(np.delete(Y[:,i],i),np.delete(v,i)))/Y[i,i] for i in np.arange(1,buses)])
    print v[1:]

##Gauss-Seidel Method
S = (-loaddata[:,1]-1j*loaddata[:,2])/vabase
v = np.ones(buses,complex)

for i in range(4):
    for k in range(buses):
        if k == slack-1:
            v[k] = 1+0j
        else:
            y=Y[k,k]
            my = np.ma.array(Y[k,:],mask=False)
            mv = np.ma.array(v,mask=False)
            my.mask[k]=True
            mv.mask[k]=True
            v[k] = (np.conj(S[k])/np.conj(v[k])-np.ma.dot(my,mv))/y
            my = np.ma.array(Y[k,:],mask=False)
            mv = np.ma.array(v,mask=False)
    print v[1:]

##Successive Over-relaxation
print "\n"
print "Successive Over-relaxation"
S = (-loaddata[:,1]-1j*loaddata[:,2])/vabase
v = np.ones(buses,complex)
w = 1.2
maxi = 25
tol = 1.0e-7
i = 0

while i < maxi:
    vo = np.copy(v) #copy of the last voltage array
    for k in range(buses):
        if k == slack-1:
            v[k] = 1+0j
        else:
            ykk = Y[k,k]
            vkold = v[k]
            my = np.ma.array(Y[k,:],mask=False)
            mv = np.ma.array(v,mask=False)
            my.mask[k]=True
            mv.mask[k]=True
            v[k] = (np.conj(S[k])/np.conj(v[k])-np.ma.dot(my,mv))/ykk
            my = np.ma.array(Y[k,:],mask=False)
            mv = np.ma.array(v,mask=False)
            v[k] = (1-w)*vkold+(w*v[k])
    print v[1:]
    if np.linalg.norm(v-vo) <= tol:
        print "Convergence reach in % iterations" % i
        break
    else:
        i += 1
#print "Maximum iterations exceeded"

##Z-Matrix: Block Substitution Method
print "\n"
print "Z-Matrix: Block Substitution Method"
Yr = Y[1:,1:]
Z = np.linalg.inv(Yr)
v = np.ones(buses,complex)
C = np.dot(Z,np.dot(Yr,v[1:]))
print Yr