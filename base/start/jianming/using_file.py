#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test*.py


if __name__ == '__main__':
    poem = '''\
    Programming is fun
    When the work is done
    if you wanna make your work also fun:
            use Python!
    '''

    f = file('poem.txt', 'w')  # open for 'w'riting
    f.write(poem)  # write text to file
    f.close()  # close the file

    f = file('poem.txt')
    # if no mode is specified, 'r'ead mode is assumed by default
    while True:
        line = f.readline()
        if len(line) == 0:  # Zero length indicates EOF
            break
        print(line, end=' ')
        # Notice comma to avoid automatic newline added by Python
    f.close()  # close the file