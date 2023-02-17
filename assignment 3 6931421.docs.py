import numpy as np
L=12#length of beam in meters
w=10#intensity of load in KN/m
#question a
#bending moment(M)
#shear force (V)
x=0	
M=(w*(-6*x**2 + 6*L*x-L**2))/12
V=w*(L/2-x)
print(M)
print(V)
#x=L=10
x=L
M=(w*(-6*x**2 +  6*L*x-L**2))/12
V=w*(L/2-x)
print(M)
print(V)
#question b
#when M=0 the expression is x**2-Lx+L**2/6=0
#from the expression
a=1
b=-L
c=L**2/6
#using the almighty formular the two roots are
discriminant=b**2-4*a*c
root_1b=(-b + np.sqrt(discriminant))/2*a
root_2b=(-b - np.sqrt(discriminant))/2*a
print('(b)The point of contraflexure are{0} and{1}'.format(root_1b,root_2b))
#question c
#when V=0 x=L
print('(c)the point at which V=0 is {}'.format(x))
#question d
p=0
s=0.01
q=L+s
x=np.arange(p,q,s)
M=(w*(-6*x**2 + 6*L*x-L**2))/12
print('(d) using the initialized variable,the bending moment at each step in the array is {0}'.format(M))
#question e
V=w*(L/2-x)
print('(e)the shear force for each step along the span is {}'.format(V))
#question f
#let the absolute value of the bending moment array be AM
#also let the minimum AM be m_AM
AM=abs(M)
m_AM=min(AM)
#when the bending moment is m_AM we get an expression x**2 -Lx + (L**2/6)+(2*m_AM)/w=0
#from the expression
a=1
b=-L
C=(L**2/6)+(2*m_AM)/w
#using the almighty formula the roots are
discriminant=b**2-4*a*c
root_1f=(-b + np.sqrt(discriminant))/2*a
root_2f=(-b - np.sqrt(discriminant))/2*a
print('(f)the point along L at which the absolute values of the bending moment array is minimum are{0} and{1}'.format(root_1f,root_2f))
#question g
#let the relative errors be r_e
r_e1=((root_1b-root_1f)/root_1b*100)
r_e2=((root_2f-root_2b)/root_2f*100)
print('(g)the relative errors between estimated points of contraflexure are {0}% and{1}%'.format(r_e1,r_e2))
#question h
#let the maximum bending moment be max_M and the minimum bending moment be min_M
#for the maximum
max_M=max(M)
#when the bending moment is max_M, we get an expression x**2 -Lx +(L**2/6)+(2*max_M)/w=0
a=1
b=-L
c=(L**2/6)+(2*max_M)/w
#using the almighty formula the two roots are
discriminant=b**2 -4*a*c
root_1=(-b + np.sqrt(discriminant))/2*a
root_2=(-b -np.sqrt(discriminant))/2*a
print('(h.1) the points at which the maximum bending moment occur are{0} and{1}'.format(root_1,root_2))
#for the minimum
min_M=min(M)
#when the bending moment is min_M,we grt an expression
#x**2 - Lx + (L**2//6)+(2*min_M)/w=0
a=1
b=-L
c=(L**2//6)+(2*min_M)/w
#using the almighty formula the two roots are

discriminant=b**2 -4*a*c
root_1=(-b -np.sqrt(discriminant))/2*a
root_2=(-b -np.sqrt(discriminant))/2*a
print('(h.2)the points at which the minimum bending moment occur are{0} and {1}'.format(root_1,root_2))
#index number 6931421
#github username is angelaB01
      




                                                      




      
