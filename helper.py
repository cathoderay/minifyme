import os


def compose(func_list, input):
    o = input
    for func in func_list:
        o = func(o)
    return o


def read_input(filename):
    return open(filename, 'r+').read(os.path.getsize(filename))


def write_output(output_filename, output):
    try:
        open(output_filename, 'w+').write(output)
    except Exception, e:
        print e
    
