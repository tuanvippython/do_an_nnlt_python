import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

#Câu 4.1:
def do_thi_mat_yen_ngua(x,y):
  z = (x/3)**2 - (y/2)**2
  return z

def thuc_hien_ve_mat_yen_ngua():
  x = np.linspace(-10,10,500)
  y = np.linspace(-10,10,500)
  x, y = np.meshgrid(x, y)
  z = do_thi_mat_yen_ngua(x, y)
  fig, ax =plt.subplots(subplot_kw={"projection":"3d"})
  mat_yen_ngua = ax.plot_surface(x, y, z,cmap='PuBu',linewidth=0,antialiased=False)
  fig.colorbar(mat_yen_ngua, shrink=1,aspect=5)
  plt.show()


#Câu 4.2:
def do_thi_hyperbolic1(x,y):
  z1 = (((x/3)**2 + (y/5)**2 - 1)*4)**1/2
  return z1

def do_thi_hyperbolic2(x,y):
  z2 = -(((x / 3) ** 2 + (y / 5) ** 2 - 1) * 4) ** 1 / 2
  return z2

def thuc_hien_ve_mat_hyperbolic():
  x = np.linspace(-30, 30, 2000)
  y = np.linspace(-30, 30, 2000)
  x,y = np.meshgrid(x,y)
  z1 = do_thi_hyperbolic1(x,y)
  z2 = do_thi_hyperbolic2(x,y)
  fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
  mat_hyperbolic1 = ax.plot_surface(x, y, z1, cmap='PuBu', linewidth=0, antialiased=False)
  mat_hyperbolic2 = ax.plot_surface(x, y, z2, cmap='PuBu', linewidth=0, antialiased=False)
  fig.colorbar(mat_hyperbolic1, shrink=1, aspect=5)
  fig.colorbar(mat_hyperbolic2, shrink=1, aspect=5)
  plt.show()

#Câu 4.3
def do_thi_mat_cau1(x, y):
  z1 = 4 + (-(x + 2) ** 2 - (y - 1) ** 2 + 4) ** (1 / 2)
  return z1


def do_thi_mat_cau2(x, y):
  z2 = 4 - (-(x + 2) ** 2 - (y - 1) ** 2 + 4) ** (1 / 2)
  return z2


def thuc_hien_ve_mat_cau():
  x = np.linspace(-4, 0, 2000)
  y = np.linspace(-1, 3, 2000)
  x, y = np.meshgrid(x, y)
  z1 = do_thi_mat_cau1(x, y)
  z2 = do_thi_mat_cau2(x, y)
  fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
  mat_cau1 = ax.plot_surface(x, y, z1, cmap='PuBu', linewidth=0, antialiased=False)
  mat_cau2 = ax.plot_surface(x, y, z2, cmap='PuBu', linewidth=0, antialiased=False)
  fig.colorbar(mat_cau1, shrink=1, aspect=5)
  fig.colorbar(mat_cau2, shrink=1, aspect=5)
  plt.show()

#Caau4.4
def main():
  thuc_hien_ve_mat_yen_ngua()
  thuc_hien_ve_mat_hyperbolic()
  thuc_hien_ve_mat_cau()

if __name__ == '__main__':
    main()