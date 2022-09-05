"""" <<<  กฤษฎาจำเป็นต้องเดินทางไกลเข้าไปในป่าเนื่องจากเป็นหลักสูตรของลูกเสือสามัญ  แต่กฤษฎาได้หลงทางเข้ามาในป่าลึก (เดินยังไงให้หลงครับเนี่ยย - -") หลังจากเดินไปสักพักกฤษฎาก็ได้สังเกตเห็นเลขบนต้นไม้แต่ละต้น ซึ่งเป็นตัวเลขที่แสดงความสูงของต้นไม้แต่ละต้น (มีหน่วยเป็นเมตร) กฤษฎาจึงคิดอะไรสนุกๆทำเพื่อแก้เบื่อโดยการเดินไปเรื่อยๆ และจำความสูงของต้นไม้แต่ละต้น และจะหันกลับมามอง ต้นไม้ที่เคยเดินผ่านไป >>>

****  ด้านบนจะเป็นเนื้อหาของ  < วันหนึ่งฉันเดินเข้าป่า   version  1 >  เผื่อบางคน Random ไม่ได้ครับ


หลังจากกฤษฎาเดินหลงป่ามาได้สักพักก็ได้ไปเจอเห็ดสีสันสวยงามจึงได้หยิบขึ้นมากิน  หลังจากกินเข้าไปทำให้กฤษฎามีอาการแปลกๆเกิดขึ้น  เนื่องจากเห็ดที่กินเข้าไปเป็นเห็ดพิษ  แต่กฤษฎาก็ยังคอยนับความสูงต้นไม้ไปเรื่อยๆเหมือนเดิม  ผลข้างเคียงจากเห็ดพิษก็ได้ส่งผลกระทบต่อการนับต้นไม้ของกฤษฎาเนื่องจากอาการหลอนประสาท ทำให้ต้นไม้ที่มีความสูงเป็นเลขคี่มีการเพิ่มความสูงมา 2 เมตร และต้นไม้เลขคู่ลดความสูงไป  1 เมตร ความสูงที่น้อยที่สุดคือ 1 เมตร

ให้น้องๆเขียนโปรแกรมเพื่อรับความสูงของต้นไม้ที่กฤาฎาได้เดินผ่าน  แล้วหาว่าเมื่อกฤษฎาหันหลังกลับมามองจะเห็นต้นไม้กี่ต้น

อธิบาย Input :  A  <Heights>  แสดงถึงความสูงของต้นไม้  ,  B  คือการหันหลังกลับมามอง , S  คือการโดนผลกระทบจากเห็ดพิษ

อธิบาย Test Case แรก : กฤษฎาจะเดินผ่านต้นไม้ความสูง  4   ก่อนแล้วตามด้วย  3   แล้วหันหลังกลับมามองจะเห็นต้นไม้ 2 ต้น ต่อมาเดินไปเจอต้นไม้สูง  5  กับ ต้นไม้สูง 8 ตามลำดับ  แล้วหันหลังกลับมามองจะเห็นแค่ต้นไม้ต้นเดียว  เนื่องจากต้น 8 เมตรบังต้นไม้ความสูง  4  3  และ  5 

โดยจะรับประกันว่าจะมีต้นไม้อย่างน้อย 1 ต้นและมีการหันกลับมาอย่างน้อย 1 ครั้ง

Enter Input : A 4,A 3,B,A 5,A 8,B
2
1

----------------------------------------------------------------------------

Enter Input : A 4,A 3,B,S,B,A 5,A 8,B
2
1
1

----------------------------------------------------------------------------

Enter Input : A 4,A 3,B,S,B,A 5,A 8,B,S,B
2
1
1
1

----------------------------------------------------------------------------

Enter Input : A 4,A 3,B,S,B,A 5,A 6,B,S,B
2
1
1
2




Enter Input : S,S,S,B,B,A 6,S,S,S,S,S,S,S,S,B
0
0
1

----------------------------------------------------------------------------

Enter Input : A 10,A 9,A 8,A 7,B,S,B,A 7,A 1,B,A 50,A 31,S,S,S,S,B
4
2
4
2

----------------------------------------------------------------------------

Enter Input : A 5,A 4,B,S,S,A 4,B
2
3

----------------------------------------------------------------------------

Enter Input : A 3,A 4,B,S,S,S,S,S,B
1
2




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
        if not self.isEmpty():
            return self.items[-1]
        else:
            return 1
    def isEmpty(self):
        return len(self.items) == 0 
stack = Stack()
stack_temp = Stack()
list = input('Enter Input : ').split(",")
last_number = None
lowless_number = None
counting = 0
for type_and_height in list:
    type_and_height = type_and_height.split(" ")
    type = type_and_height[0]
    if type == 'A':
        current_number = type_and_height[1]
        current_number = int(current_number)
        last_number = current_number
        stack.push(current_number)
    elif type == 'B':
        if stack.size() > 0:
            for i in range(0,stack.size()):
                if lowless_number == None:
                    lowless_number = stack.pop()
                    stack_temp.push(lowless_number)
                    counting += 1
                elif lowless_number < stack.peek():
                    counting += 1 
                    lowless_number = stack.pop()
                    stack_temp.push(lowless_number)
                    
                elif lowless_number >= stack.peek():
                    stack_temp.push(stack.pop())
            for i in range(0,stack_temp.size()):
                stack.push(stack_temp.pop())
                # stack_temp.push(stack.pop())
        print(counting)
        counting = 0
        lowless_number = None
    # elif type == 'S':
    #     for i in range(0,stack.size()):
    #         number = stack.pop()
    #         if number % 2 == 1:
    #             number += 2
    #             stack_temp.push(number)
    #         elif number % 2 == 0:
    #             number -= 1
    #             stack_temp.push(number)
    #     for i in range(0,stack_temp.size()):
    #         stack.push(stack_temp.pop())
        