import sys

# dictionary to hold the commands and their corresponding functions
commands = {
    "exit": lambda x: sys.exit(int(x)),
    "echo": lambda x: print(x),
    "type": lambda x: print(f"{x} is a shell builtin") if x in ['exit', 'echo', 'type'] else print(f"{x}: not found")
}

def main():
    while True:
        sys.stdout.write("$ ")
        command = input()
        # split the command into parts [command, arg1, arg2, ...]
        parts =  command.split(maxsplit=-1)
        cmd = parts[0]

        # get the arguments if any by joining the rest of the parts
        args = ' '.join(parts[1:]) if len(parts) > 1 else None

        # search the dictionary for the command and execute it
        if cmd in commands:
            if args:
                commands[cmd](args)
            else:
                commands[cmd]()
        else:
            print(f"{cmd}: not found")

        
if __name__ == "__main__":
    main()
