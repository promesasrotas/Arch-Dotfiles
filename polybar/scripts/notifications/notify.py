#!/env/python

from subprocess import PIPE, Popen
from colorama import Fore, Style

def main ():
    task = Popen(['dunstctl', 'count', 'history'], stdout=PIPE, stderr = PIPE)
    notNumber = str(task.stdout.readline(), encoding='utf-8')
    notNumber = notNumber.strip()
    notNumber = int (notNumber)
    task.stdout.close
    if notNumber > 0:
        print ('󱅫 {}'.format(notNumber))
    else:
        print (" ")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print ("Error, try again")