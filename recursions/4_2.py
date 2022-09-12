def combinations(list):
    if list == []:
        return [[]]
    combine_list = []
    combine_list = loops(combinations(list[1:]), list[0])
    return combine_list
def loops(loop,list):
    if loop == []:
        return []
    combine_list = [loop[0],loop[0]+[list]]
    return loops(loop[1:],list) + combine_list
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
lists = []
for x in inp:
    x = x.split(' ')
    x = list(map(int, x))
    lists.append(x)
Llist = combinations(lists)
calulate(Llist)
