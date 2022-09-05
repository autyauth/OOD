"""" ให้รับ Input เป็น  Infix  และแสดงผลลัพธ์ออกมาเป็น  Postfix   โดยจะมี Operator  5  แบบ  ได้แก่  +   -   *   /   ^



class Stack:

    def __init__(self):

    def push(self, value):

    def pop(self):

    def size(self):

    def isEmpty(self):

inp = input('Enter Infix : ')

S = Stack()

print('Postfix : ', end='')

### Enter Your Code Here ###

while not S.isEmpty():

    print(S.pop(), end='')

print()

a+b
a+b*c
a*b+c
a+b*c-d
a+b*c-(d/e+f)*g
A+(B*C-(D/E^F)*G)*H
K+L-M*N+(O^P)*W/U/V*T+Q
G+A+(U-R)^I

"""
class Stack:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    def push(self, value):
        self.items.append(value)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return len(self.items) == 0
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]     
    def lesser_operator(self,operetor):
        try:
            if self.precedence[operetor] <= self.precedence[self.peek()]:
                return True
            else:
                return False
        except KeyError:
                return False
    def x(self):
        while not self.isEmpty():
            print(self.pop(), end='')
     
inp = input('Enter Infix : ')
# inp = 'a+b*c'
stack = Stack()

print('Postfix : ', end='')

for word in inp:
    if word in "+-*/()^":
        if stack.isEmpty():
            stack.push(word)
            continue
        if word == '(':
            stack.push(word)
        elif word == ")":
            while not stack.isEmpty() and stack.peek() != '(':
                print(stack.pop(), end = "")
            if not stack.isEmpty() and stack.peek() != '(':
                continue
            else:
                stack.pop()
        else:
            while not stack.isEmpty() and stack.lesser_operator(word):
                if word == '^' and stack.items[-1] == word:
                    break
                print(stack.pop(),end = "") 
            # for x in range(0,stack.size()):   
            #     if stack.lesser_operator(word):
            #         print(stack.pop(),end = "")
            stack.push(word)    
    else:
        print(word,end='')            
stack.x()
print()