import time
def buttonup(elevatorposition):
    call = [[],[[],[],[],[]]]
    call = concatenate(input("What floors is the elevator being called by: "),0,call)
    elevengine(call,elevatorposition)
def elevengine(call,elevatorposition):
    i,j,c,d = 0,0,0,0
    while j < len(call[1][0]):
        call = removeacross(call)
        call = remove_duplicate(call)
        if i < len(call[1][2]) and call[1][2][i] < call[1][0][j]:
            elevatorposition,call,i = up(2,i,elevatorposition,call)
        else:
            elevatorposition,call,j = up(0,j,elevatorposition,call)
    while c < len(call[1][3]):
        elevatorposition,call,c = up(3,c,elevatorposition,call)
        call = remove_duplicate(call)
    if len(call[1][1]) > 0:
        call = remove_duplicate(call)
        down(elevatorposition,call)
def concatenate(destination, elevatorposition,call):
    if "," in destination:
        evaluation = sorted(list(map(int, destination.split(","))))
        destination = sorted(call)
        for items in evaluation:
            if elevatorposition == 0:
                destination[1][0] += [items]
            if items > elevatorposition and items < max(call[1][0]):
                destination[1][2] += [items]
            if items < elevatorposition:
                destination[1][1] += [items]
            if items > elevatorposition and items > max(call[1][0]):
                destination[1][3] += [items]
    else:
        items = int(destination)
        destination = call
        if elevatorposition == 0:
            destination[1][0] += [items]
        if items > elevatorposition and items < max(call[1][0]):
            destination[1][2] += [items]
        if items < elevatorposition:
            destination[1][1] += [items]
        if items > elevatorposition and items > max(call[1][0]):
            destination[1][3] += [items]
    return destination
def up(z,a,elevatorposition,call):
    for items in range(elevatorposition + 1, call[1][z][a] + 1):
        time.sleep(1)
        print("Reached Floor " + str(items))
    elevatorposition = call[1][z][a]
    print("Doors opening")
    time.sleep(1)
    if z == 0:
        print("People Entering")
        time.sleep(1)
        call = concatenate(input('What floors do the people want to go to: '), elevatorposition, call)
        print("Doors closing")
        print(call)
    else:
        print("People Exiting")
        time.sleep(1)
        print("Doors Closing")
    a += 1
    return elevatorposition,call,a
def down(elevatorposition,call):
    call[1][1] = sorted(call[1][1], reverse=True)
    for items in call[1][1]:
        for position in range(elevatorposition-1,items-1,-1):
            print('Reached Floor: ' + str(position))
            time.sleep(1)
        print("Doors opening")
        time.sleep(1)
        print("People exiting")
        time.sleep(1)
        print('Doors closing')
        time.sleep(1)
        elevatorposition = position
    return elevatorposition,call
def removeacross(call):
    for item in call[1][2]:
        if item in call[1][1]:
            call[1][2].remove(item)
    return call
def remove_duplicate(call):
    newcall = [[],[[],[],[],[]]]
    for i in range(len(call[1])):
        for j in range(len(call[1][i])):
            if call[1][i][j] not in newcall[1][i]:
                newcall[1][i].append(call[1][i][j])
    return newcall
buttonup(32)
