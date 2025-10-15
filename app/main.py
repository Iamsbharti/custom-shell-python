import sys
import os
import subprocess
import shlex

# dictionary to hold the commands and their corresponding functions
commands = {
    "exit": lambda x: sys.exit(int(x) if x else 0),
    "echo": lambda x: ((echo_command(x))),
    "type": lambda x: ((type_command(x))),
    "pwd": lambda x: print(os.getcwd()),
    "cd": lambda x: ((cd_command(x))),
}

def echo_command(text):
    print(text.replace("'", ""))

def cd_command(path):
    try:
        if(os.path.isdir(path)):
            os.chdir(path)
        elif path == '~':
            os.chdir(os.path.expanduser('~'))
        else:
            print(f"cd: {path}: No such file or directory")
    except Exception as e:
        print(f"cd: {path} : {e}")


def is_command_executable(command):
    # check each directory in PATH for an executable file named x
    for directory in os.environ.get("PATH", "").split(os.pathsep):
        full_path = os.path.join(directory, command)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return full_path
    return None

def type_command(x):
    # check if x is a shell builtin    
    if x in ['exit', 'echo', 'type', 'pwd', 'cd']:
        print(f"{x} is a shell builtin")
        return
    executable_path = is_command_executable(x)
    if executable_path:
        print(f"{x} is {executable_path}")
    else:
        print(f"{x}: not found")

    

def main():
    while True:
        sys.stdout.write("$ ")
        command = input()
        # split the command into parts [command, arg1, arg2, ...]
        parts =  shlex.split(command)
        cmd = parts[0]

        # get the arguments if any by joining the rest of the parts
        args = ' '.join(parts[1:]) if len(parts) > 1 else None
        
        # search the dictionary for the command and execute it
        if cmd in commands:
            if args:
                commands[cmd](args)
            else:
                commands[cmd](0 if command == "exit" else None)
        else:
            # run external command
            executable_path = is_command_executable(cmd)
            if executable_path:
                subprocess.run([cmd] + (parts[1:] if len(parts) > 1 else []))
            else:
                print(f"{cmd}: not found")
        
if __name__ == "__main__":
    main()
