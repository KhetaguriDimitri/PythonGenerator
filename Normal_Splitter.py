import itertools 

name = "571.txt"
size = 50000

def grouper(size, iterable, fillvalue=None):
    args = [iter(iterable)] * size
    return itertools.zip_longest(fillvalue=fillvalue, *args)


with open(name) as f:
    for i, g in enumerate(grouper(size, f, fillvalue=''), 1):
        with open('571_{0}.txt'.format(i * size), 'w') as fout:
            fout.writelines(g)
