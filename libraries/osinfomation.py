# The scripts is to find the operating system of curret machine

'''importing Libraries'''
import platform

def find_os_path_separator(os_name):
    ''' conditions ro check operating system'''
    os_name = os.getcwd()
    if os_name == "Windows" :
        print(f"The operating system of the current machine is {os_name}")
    else:
        print(f"The operating system of the current machine is {os_name}")

if __name__ == "__main__":
    path_separator = find_os_path_separator()
    print(path_separator)
