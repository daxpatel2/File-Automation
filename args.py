import sys
import subprocess
#can we use a que data strucutre to que which directories to process?
#check out argparse library for

#grab the args after the python3 file name in command line(first comnand should be the directory the user wants to clean)
args = sys.argv
print(args[1])
if args[1] == 'downloads':
    print('Yes args[1] is {}'.format(args[1]))
    #need to fix automation to add download command after filename to onlu run downloads directory
    cmd_line_arg = 'cd downloads'
    p1 = subprocess.Popen(cmd_line_arg, shell=True)
    if p1.returncode == 0:
        print('Successfully ran automation.py')
    else:
        print('Failed to run automation.py')
