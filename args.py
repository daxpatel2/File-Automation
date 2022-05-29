import sys
import automation
#can we use a que data strucutre to que which directories to process?
#check out argparse library for

#grab the args after the python3 file name in command line(first comnand should be the directory the user wants to clean)
args = sys.argv
print(args[1])

if args == 'downloads':
    #run automation.py's downloads dirctory function
    automation.main()
