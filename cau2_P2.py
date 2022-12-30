#Câu 2.1:
from sympy import symbols, Eq, solve

def giai_he_pt():
  x, y, z = symbols('x y z')
  eq1 = Eq(2*x - 5*y + z , -5)
  eq2 = Eq(4*x + 2*y - 2*z , 2)
  eq3 = Eq(x + y - z , 0)
  ketqua21 = solve((eq1,eq2,eq3),(x,y,z))
  print('ket qua cau 2.1:',ketqua21)

#Câu 2.2:
from sympy import *

def tinh_gioi_han():
  x = symbols('x')
  f = ((x**3 - 3*x**2)**(1/3) + sqrt(x**2 - 2*x))
  ketqua22 = limit (f,x,oo)
  print('ket qua cau 2.2:',ketqua22)

#Câu 2.3:
def tinh_dao_ham():
  x = symbols('x')
  f = (2*x-1)/(x+2)
  ketqua23 = diff(f,x)
  print('ket qua cau 2.3:',ketqua23)

#Câu 2.4:
def tinh_nguyen_ham():
  x = symbols('x')
  f = x / (x**2+1)
  ketqua24 = integrate(f,x)
  print('ket qua cau 2.4:',ketqua24)

#Câu 2.5:
import numpy as np
np.tan = tan
np.cos = cos
np.pi = pi

def tinh_tich_phan():
  x = symbols('x')
  f = (1-x*tan(x))/(x**2*cos(x)+x)
  ketqua25 = integrate(f,(x,(2*pi)/3,pi))
  print('ket qua cau 2.5:',ketqua25)

#Câu 2.6:
def main():
  giai_he_pt()
  tinh_gioi_han()
  tinh_dao_ham()
  tinh_nguyen_ham()
  tinh_tich_phan()

if __name__ == '__main__':
  main()