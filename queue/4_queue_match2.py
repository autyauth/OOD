""""
สมมติว่านักศึกษาแอบชอบคนๆหนึ่งอยู่ โดยที่นักศึกษาและคนๆนั้นจะมีกิจกรรมและสถานที่ที่ไปแตกต่างกันในแต่ละวัน
ให้นักศึกษาเขียนโปรแกรมที่จะหาว่าสิ่งที่นักศึกษาและคนๆนั้นทำในแต่ละวันจะทำให้ได้คบกันหรือไม่ โดยใช้ Queue

กิจกรรม                                       สถานที่
0 = กินข้าว(Eat)                           0 = ร้านอาหาร(Res.)
1 = เล่นเกม(Game)                      1 = ห้องเรียน(ClassR.)
2 = ทำโจทย์ datastruc(Learn)      2 = ห้างสรรพสินค้า(SuperM.)
3 = ดูหนัง(Movie)                        3 = บ้าน(Home)

โดยการรับ Input จะประกอบด้วย

กิจกรรม:สถานที่(ของนักศึกษาและของคนๆนั้น) โดยในแต่ละวันจะคั่นด้วยเครื่องหมาย ,

เช่น วันที่ 1 นักศึกษาไปกินข้าวที่ร้านอาหาร และ คนๆนั้นไปนั่งทำโจทย์ datastruc ที่ร้านอาหาร 
       วันที่ 2 นักศึกษาไปเล่นเกมที่บ้าน และ คนๆนั้นไปดูหนังที่ห้างสรรพสินค้า
จะได้ว่า 0:0 2:0,1:3 3:2

***มีการคิดคะแนนดังนี้***

·       กิจกรรมเดียวกันแต่คนละสถานที่         +1

·       สถานที่เดียวกันแต่ทำกิจกรรมต่างกัน    +2

·       กิจกรรมเดียวกันและสถานที่เดียวกัน    +4

·       ไม่เหมือนกันเลย                                   - 5

หากมีคะแนนมากกว่าหรือเท่ากับ 7 จะถือว่าได้คบกัน แต่ถ้าคะแนนน้อยกว่า 7 แต่มากกว่า 0 เป็นคนคุย น้อยกว่านั้นถือว่าเป็นได้แค่เพื่อน

โดยในแต่ละขั้นตอนให้แสดงผลดังตัวอย่าง


Enter Input : 0:0 2:0,1:3 3:3,2:1 2:1
My   Queue = 0:0, 1:3, 2:1
Your Queue = 2:0, 3:3, 2:1
My   Activity:Location = Eat:Res., Game:Home, Learn:ClassR.
Your Activity:Location = Learn:Res., Movie:Home, Learn:ClassR.
Yes! You're my love! : Score is 8.

-----------------------------------------------------------------------------------------

Enter Input : 2:1 2:1
My   Queue = 2:1
Your Queue = 2:1
My   Activity:Location = Learn:ClassR.
Your Activity:Location = Learn:ClassR.
Umm.. It's complicated relationship! : Score is 4.

-----------------------------------------------------------------------------------------

Enter Input : 0:1 2:3,3:2 3:2
My   Queue = 0:1, 3:2
Your Queue = 2:3, 3:2
My   Activity:Location = Eat:ClassR., Movie:SuperM.
Your Activity:Location = Learn:Home, Movie:SuperM.
No! We're just friends. : Score is -1.

-----------------------------------------------------------------------------------------

Enter Input : 3:3 1:3,0:0 1:1,2:2 3:3,0:3 0:1
My   Queue = 3:3, 0:0, 2:2, 0:3
Your Queue = 1:3, 1:1, 3:3, 0:1
My   Activity:Location = Movie:Home, Eat:Res., Learn:SuperM., Eat:Home
Your Activity:Location = Game:Home, Game:ClassR., Movie:Home, Eat:ClassR.
No! We're just friends. : Score is -7.

"""

class Queue:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def enQueue(self, item):
        self.items.append(item)
    def deQueue(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return len(self.items) == 0
def matching(eachDay):
    activity = {'0': 'Eat', '1': 'Game', '2': 'Learn', '3': 'Movie'}
    location = {'0':':Res.', '1': ':ClassR.' , '2' : ':SuperM.', '3':':Home'}
    my_queue = Queue()
    your_queue = Queue()
    point = 0
    i = 0
    j = 1
    str_my_queue = ''
    str_your_queue = ''
    str_my_Activity_Location = ''
    str_your_Activity_Location = ''
    for activity_and_place in eachDay:
       
        activity_and_place = activity_and_place.split(" ")
        # initialize 
        # กิจกรรมกับกิจกรรม เอามาแบ่งของเรากับคู่ของเรา
        my_activity_and_place1 = activity_and_place[0]
        your_activity_and_place1 = activity_and_place[1]

        #print str output
        # ไว้สำหรับปริ้นข้อความออก โดยเอากิจกรรมมาใส่ของแต่ละคน
        str_my_queue += my_activity_and_place1 
        str_your_queue += your_activity_and_place1 
        
        
        my_activity_and_place2 = my_activity_and_place1.split(":")
        my_activity = my_activity_and_place2[0]
        my_place = my_activity_and_place2[1]

        
        your_activity_and_place2 = your_activity_and_place1.split(":")
        your_activity = your_activity_and_place2[0]
        your_place = your_activity_and_place2[1]

        str_my_Activity_Location += activity[my_activity] + location[my_place]
        str_your_Activity_Location += activity[your_activity] + location[your_place]
        if j < (len(eachDay)):
            str_my_Activity_Location += ', '
            str_your_Activity_Location += ', '
        if j < (len(eachDay) ):
            str_my_queue += ', '
            str_your_queue += ', '
        
        # print(len(eachDay))
        j+=1
        # print(len(your_activity_and_place2))
        # print(eachDay )
        for item in my_activity_and_place2:
            item = int(item)
            my_queue.enQueue(item)
        for item in your_activity_and_place2:
            item = int(item)
            your_queue.enQueue(item)

        
        
    while i <= my_queue.size()-1:
        if my_queue.items[i] == your_queue.items[i] and my_queue.items[i+1] == your_queue.items[i+1]: 
            point += 4
        elif my_queue.items[i] != your_queue.items[i] and my_queue.items[i+1] != your_queue.items[i+1]:
            point -= 5
        elif my_queue.items[i] == your_queue.items[i]:
            point += 1
        elif my_queue.items[i+1] == your_queue.items[i+1]:
            point +=2
        i += 2
    print('My   Queue = ' + str_my_queue)
    print('Your Queue = ' + str_your_queue)
    print('My   Activity:Location = '+ str_my_Activity_Location)
    print('Your Activity:Location = '+str_your_Activity_Location)
    if point >= 7:
        print('Yes! You\'re my love! : Score is '+str(point)+'.')
    elif point > 0 and point < 7:
        print('Umm.. It\'s complicated relationship! : Score is '+str(point)+'.')    
    else:
        print('No! We\'re just friends. : Score is '+str(point)+ '.')
    
matching(input('Enter Input : ').split(","))