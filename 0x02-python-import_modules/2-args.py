#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    argc = len(argv[1:])

    if argc == 0:
        print('0 arguments.')
    else:
        if argc == 1:
            print('{} argument:'.format(argc))
        else:
            print('{} arguments:'.format(argc))

        for i in range(1, argc + 1):
            print('{0}: {1}'.format(i, argv[i]))
