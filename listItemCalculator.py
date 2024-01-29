# for mrs kirshenbaum :)

def listItemCalulcator(firstItem, secondItem, lastItem):
    listInterval = secondItem - firstItem

    lastItem = ( lastItem - firstItem ) + listInterval
    firstItem = ( firstItem - firstItem ) + listInterval

    firstItem = firstItem / listInterval
    lastItem = lastItem / listInterval

    if ( firstItem == 1.0 ) and ( lastItem % listInterval == 0 ):
        answer = f"you have {int(lastItem)} items in your list."
        print(answer)
    else:
        print('ERR: your list is not valid \n'
              'one of the inputs does not follow a linear pattern. \n'
              'please try again.')

x, y, z = 7, 14, 147

listItemCalulcator(x, y, z)
# x = first item in list
# y = second item in list
# z = last item in list
# note: all numbers must be expressed as a single term 
# ex = 12, -50, (11/4), (6+(1/2))