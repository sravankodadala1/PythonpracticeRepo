#list

def process_commands(list, commands):
    for i in commands:
        #input and spit the values in form of list
        commands = i.split()

        if commands[0] == 'print':
            #if input is print, then print the list
            print(list)

        elif commands[0] == 'insert':
            #if input is insert, append the values commands[2] at commands[1]
            list.insert(int(commands[1]), int(commands[2]))

        elif commands[0] == 'remove':
            #if input is remove, remove the value at command[1] index
            list.remove(int(commands[1]))

        elif commands[0] == 'append':
            #if input is append, append the values of commands[1] at the end
            list.append(int(commands[1]))

        elif commands[0] == 'sort':
            #if input is sort, sort the list
            list.sort()

        elif commands[0] == 'pop':
            #if input is pop, pop the last index
            list.pop()

        elif commands[0] == 'reverse':
            #if input is reverse, reverse the index
            list.reverse()




