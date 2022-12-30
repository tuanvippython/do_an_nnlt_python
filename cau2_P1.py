import random
random.seed(123)
#câu 2.1:
import random
random.seed(123)

n = abs(int(input('n=')))
a = 1.5
b = 4.5
def sinh_list_cac_so_thuc(n):
    x = [(b - a) * random.random() + a for i in range(n)]
    print('Các phần tử trong list', x)
    return x



#Câu 2.2:
y = [9,-2,-5,3,6,8,9]
def sap_xep_giam_dan(y):
    y1 = sorted(y,reverse=True)
    print('list giảm dần',y1)

def sap_xep_tang_dan(y):
    y2 = sorted(y, reverse=False)
    print('list tăng dần', y2)

sap_xep_tang_dan(y)


#Câu 2.3:
list = [9,-2,3,-7,8,-2,9]

def tim_vi_tri_n(list,n):
    if n in list:
        vi_tri = [i for i, z in enumerate(list) if z == n]
        print('vị trí của n là:', vi_tri)
    else:
        print("không tìm thấy giá trị n trong list")


#Câu 2.4:
import os
import pickle

def luu_tap_tin(list,ten_tap_tin):
    with open(os.path.join( ten_tap_tin), 'wb') as f:
        pickle.dump(list, f)
        print('Kết thúc chương trình lưu tập tin')

def luu_tap_tin(sap_xep_giam_dan,ten_tap_tin):
    with open(os.path.join( ten_tap_tin), 'wb') as f:
        pickle.dump(list, f)
        print('Kết thúc chương trình lưu tập tin')


#Câu 2.5
def main():
    sinh_list_cac_so_thuc(n)
    luu_tap_tin(list,'tuan.txt')
    sap_xep_giam_dan(y)
    luu_tap_tin(sap_xep_giam_dan,'tuan1.txt')
    tim_vi_tri_n(y, -2)


if __name__ == '__main__':
    main()



