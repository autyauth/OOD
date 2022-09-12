"""""
“เปอร์เกต์” เป็นอาหารแสนอร่อยที่ใครๆก็รู้จักกัน และแน่นอนว่าส่วนผสมย่อมเป็นสิ่งที่ต้องพิถีพิถันอย่างยิ่ง

คุณมีส่วนผสมทั้งหมด N ชนิด แต่ละชนิดจะมีความเปรี้ยว S และความขม B เมื่อนำส่วนผสมมารวมกัน ความเปรี้ยว ลัพธ์ จะได้จากผลคูณของค่าความเปรี้ยวของทุกชนิดที่ใช้ ในขณะที่ความขมลัพธ์ จะได้จากผลบวกของความขมของ ทุกชนิดที่ใช้ ส่วนผสมที่ใช้นั้น

เปอร์เกต์ที่อร่อยที่สุดนั้น จะมีผลต่างค่าความเปรี้ยวลัพธ์และค่าความขมลัพธ์ของส่วนผสมทั้งหมดน้อยที่สุด และเรา จำเป็นต้องใช้ส่วนผสมอย่างน้อย 1 ชนิด

โจทย์ จงเขียนโปรแกรมเพื่อหาค่าผลต่างของความเปรี้ยวลัพธ์และความขมลัพธ์ของส่วนผสม ที่น้อยที่สุด



******* อธิบาย input

โดยส่วนผสมแต่ละชนิดจะแบ่งด้วย comma ( ' , ' ) โดยในแต่ละส่วนผสม จะมีจำนวนเต็มสองจำนวน S และ B คือค่าความเปรี้ยวและค่าความขมของ ส่วนผสมชนิดนั้น



******* รับประกันว่าสำหรับทุกข้อมูลนำเข้า เมื่อนำส่วนผสมทุกชนิดแล้ว จะได้ค่าความเปรี้ยวลัพธ์และความขมลัพธ์ ไม่เกิน 1,000,000,000

Enter Input : 3 10
7

Enter Input : 3 8,5 8
1

Enter Input : 1 7,2 6,3 8,4 9
1

"""
def combinations(list):
    # print(list)
    if list == []:
        return [[]]
    combine_list = []
    loop = combinations(list[1:])
    # ไว้เก็บlist ที่จับคู่แต่ละแบบ
    for comb in loop: # ไว้ตัดทีละแต่ใน lists ออก
        combine_list += [comb, comb + [list[0]]]
        # เป็นการเพิ่ม comb เข้าไปใน combine_list โดยจะใส่ทั้ง [comb] และ [comb, list[0]]
        # print()
        # print(list)
        # print("loop: ",loop)
        # print("comb: ",comb)
        # print("combine_list: ",combine_list)
    return combine_list

def loops(loop):
    if loop == None:
        return []
    loops[loop[1:]]
    return loop[0]
""""
Enter Input : 1 2 3
['1', '2', '3']
['2', '3']
['3']
[]

['3']
loop:  [[]]
comb:  []
combine_list:  [[], ['3']]

['2', '3']
loop:  [[], ['3']]
comb:  []
combine_list:  [[], ['2']]

['2', '3']
loop:  [[], ['3']]
comb:  ['3']
combine_list:  [[], ['2'], ['3'], ['3', '2']]

['1', '2', '3']
loop:  [[], ['2'], ['3'], ['3', '2']]
comb:  []
combine_list:  [[], ['1']]

['1', '2', '3']
loop:  [[], ['2'], ['3'], ['3', '2']]
comb:  ['2']
combine_list:  [[], ['1'], ['2'], ['2', '1']]

['1', '2', '3']
loop:  [[], ['2'], ['3'], ['3', '2']]
comb:  ['3']
combine_list:  [[], ['1'], ['2'], ['2', '1'], ['3'], ['3', '1']]

['1', '2', '3']
loop:  [[], ['2'], ['3'], ['3', '2']]
comb:  ['3', '2']
combine_list:  [[], ['1'], ['2'], ['2', '1'], ['3'], ['3', '1'], ['3', '2'], ['3', '2', '1']]
"""

def calulate(list):
    multi = 1
    sum = 0
    output = None
    list = list[1:]
    for x in list:
        for y in x:
            multi *= int(y[0])
            sum += int(y[1])
            if output == None:
                output = abs(multi - sum)
                continue
            if output >= abs(multi - sum):
                output = abs(multi - sum)
        multi = 1
        sum = 0
    print(output)

inp = input('Enter Input : ').split(',')
# lists = []
# for x in inp:
#     x = x.split(' ')
#     x = list(map(int, x))
#     lists.append(x)
# Llist = combinations(lists)
x = combinations(inp)
print(x)
# print(Llist)
# calulate(Llist)

