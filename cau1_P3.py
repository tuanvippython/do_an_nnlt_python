import pickle
import os

#1
class NhanVien:
    def __init__(self, fullname, age, salary):
        self.hoten = fullname
        self.tuoi = age
        self.luong = salary

    def __str__(self):
        message = '[ho ten:' + self.hoten + ';tuoi:' \
                  + str(self.tuoi) + ';luong:' \
                  + str(self.luong) + ']'
        return message

    def __gt__(self, other):
        return self.tuoi > other.tuoi

    def __ge__(self, other):
        return self.tuoi >= other.tuoi

    def __lt__(self, other):
        return self.tuoi < other.tuoi

    def __le__(self, other):
        return self.tuoi <= other.tuoi

    def __eq__(self, other):
        return self.tuoi == other.tuoi

    def __ne__(self, other):
        return self.tuoi != other.tuoi



#2
def list_nhan_vien(listnv):
  while True:
    fullname = input('Tên nhân viên (nhập "End" để kết thúc): ')
    if fullname == 'End':
      break

    age = int(input('Tuổi nhân viên: '))
    salary = int(input('Lương nhân viên: '))
    nv = NhanVien(fullname, age, salary)
    listnv.append(nv)

#3
def list_nv(listnv):
    for i, nv in enumerate(listnv):
        print('Tên nhân viên:',nv.hoten)
        print('Tuổi nhân viên:',nv.tuoi)
        print('Lương nhân viên:',nv.luong)


#4
def sap_xep_nhan_vien(nv):
    giam_dan = sorted(nv, reverse=True)
    print(giam_dan)
    for item in giam_dan:
        print(item)

#5
def luu_list_nhan_vien(nv):
    ten_tap_tin = 'tuan.txt'
    path = 'C:/Users/ADMIN/Documents'
    with open(os.path.join(path,ten_tap_tin), 'wb') as f:
        pickle.dump(nv, f)

def doc_list_nhan_vien(nv):
    ten_tap_tin = 'tuan.txt'
    path = 'C:/Users/ADMIN/Documents'
    with open(os.path.join(path, ten_tap_tin), 'rb') as f:
        pickle.load(f)



def main():
    danh_sach_nhan_vien = []
    list_nhan_vien(danh_sach_nhan_vien)
    list_nv(danh_sach_nhan_vien)
    sap_xep_nhan_vien(danh_sach_nhan_vien)
    luu_list_nhan_vien(danh_sach_nhan_vien)
    doc_list_nhan_vien(danh_sach_nhan_vien)

if __name__ =='__main__':
    main()
