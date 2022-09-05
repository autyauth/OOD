""""ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ STACK ในการแก้ปัญหา



A  <value>  ให้นำ value ไปใส่ใน STACK และทำการแสดงผล Size ปัจจุบันของ STACK

P                 ให้ทำการแสดงผลของvalueที่อยู่ท้ายสุดและindexของvalueนั้นจากนั้นทำการ Pop_Stack ถ้าหากไม่มี value อยู่ใน Stack ให้แสดงผลเป็น  -1

*** ในตอนสุดท้ยถ้าหากใน Stack ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty

Enter Input : A 10,A 20,A 30,A 40,P,P
Add = 10 and Size = 1
Add = 20 and Size = 2
Add = 30 and Size = 3
Add = 40 and Size = 4
Pop = 40 and Index = 3
Pop = 30 and Index = 2
Value in Stack = 10 20

-------------------------------------------------------------------------------

Enter Input : A 10,A 20,A 30,A 40,P,A 50,A 60,P,P,P,P,P,P
Add = 10 and Size = 1
Add = 20 and Size = 2
Add = 30 and Size = 3
Add = 40 and Size = 4
Pop = 40 and Index = 3
Add = 50 and Size = 4
Add = 60 and Size = 5
Pop = 60 and Index = 4
Pop = 50 and Index = 3
Pop = 30 and Index = 2
Pop = 20 and Index = 1
Pop = 10 and Index = 0
-1
Value in Stack = Empty

-------------------------------------------------------------------------------

Enter Input : P,A 99,P,P,A 88,P,P,A 12,A 13,A 86
-1
Add = 99 and Size = 1
Pop = 99 and Index = 0
-1
Add = 88 and Size = 1
Pop = 88 and Index = 0
-1
Add = 12 and Size = 1
Add = 13 and Size = 2
Add = 86 and Size = 3
Value in Stack = 12 13 86

"""

class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop() 
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items

def print_pop_push(i):
    stack = Stack()
    for item in i:
        items = item.split()
        if items[0] == 'A':
            stack.push(items[1])
            s = 'Add = ' + items[1] + ' and Size = ' + str(stack.size())
        elif items[0] == 'P':
            if stack.size() >= 1:
                s = 'Pop = '+ stack.pop() + ' and Index = '+str(stack.size())
            else:
                s = '-1'
        else:
            continue
        print(s)
    if stack.size() > 0:
        print('Value in Stack = ',end = "")
        for x in stack.peek():
            print(x, end = " ")
    else:
        print('Value in Stack = Empty')
    
items = input('Enter Input : ').split(",")
# print(items)
print_pop_push(items)
