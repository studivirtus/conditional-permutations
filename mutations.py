#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Michael
#
# Created:     29/04/2014
# Copyright:   (c) Michael 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

truthTable = (0, 0, 0, 1)
enter = ('a','b','c','d','e')
modEnter = ()
mutations = [
    [0,3,2,4,1],
    [0,3,4,1,2],
    [0,2,3,1,4],
    [0,1,3,4,2],
    [0,3,1,2,4,]]


from itertools import cycle

def mutatate (source, muta, rev):
    mutation = [0,0,0,0,0]
    mutaCycle = cycle(muta)
    if rev:
        muta.reverse()
    nextel = mutaCycle.__next__()
    i = 0
    while i < 5:
        #print(nextel)
        mutation[(mutaCycle.__next__())] = source[nextel]
        thisel, nextel = nextel, mutaCycle.__next__()
        #print(mutation)
        i += 1
    return mutation

print(truthTable)
