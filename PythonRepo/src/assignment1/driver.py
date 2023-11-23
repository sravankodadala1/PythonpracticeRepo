from util import process_commands

def main():
    #input the number of commands
    N = int(input("enter the number of commands to be done on the list"))
    #created a empty list
    list = []
    #created a list, the commands to be performed will be stored her
    commands = []

    for _ in range(N):
        perform_commands = input("enter the commands to be performed on the list")
        #append the list of command to be performed on list
        commands.append(perform_commands)

    #calling the function
    process_commands(list, commands)
