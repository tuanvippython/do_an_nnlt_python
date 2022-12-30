#Câu 1.1:
import numpy as np

def cau1_1():
    np.random.seed(123)
    x = int(input('Gia tri x:'))
    A = np.random.randint(-5, 5, 15).reshape((3, 5))
    print('ma trận A:', A)
    print('giá trị của tích x*A:', x * A)

#Câu 1.2:
def cau1_2():
    A = np.random.randint(-5, 5, 15).reshape((3, 5))
    print('Ma trận A :', A)
    B = np.random.randint(-10, 10, 15).reshape((3, 5))
    print('Ma trận B :', B)
    print('giá trị ma trận A*B:',A * B)
    A_chuyenvi = A.T
    print('Ma trận A chuyển vị là:',A_chuyenvi)
    C = np.dot(A_chuyenvi, B)
    print('giá trị của ma trận A_chuyenvi * B :',C)

#Câu 1.3:
def main():
    cau1_1()
    cau1_2()

if __name__ == '__main__':
  main()


