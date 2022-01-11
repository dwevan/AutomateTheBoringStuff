import time
import sys
indent = 0  #space to indent.
indent_increasing = True  #whether the indentation is increasing or not

try:
    while True:  #the main program loop
        print(' ' * indent, end='')
        print('*')
        time.sleep(0.02)  #  Pauses for 1/10 of sec

        if indent_increasing:
            # increase number of spaces
            indent = indent + 1
            if indent == 60:
                # chnging direction here
                indent_increasing = False

        else:
            # Decreases space number
            indent = indent - 1
            if indent == 0:
                # chnging direction here
                indent_increasing = True

except KeyboardInterrupt:
    sys.exit()
