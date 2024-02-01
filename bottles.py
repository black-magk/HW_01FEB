
"""
No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.

99 bottles of beer on the wall, 99 bottles of beer.
Take one down and pass it around, 98 bottles of beer on the wall.

"""
# pass num into bottles


def bottle_song(num):
    # Use Range function to create iteral object

    while num >= 1:
        if (num == 2):

            print(f'{num} bottles of beer on the wall, {num} bottles of beer. Take one down and pass it around, {num - 1} bottle of beer on the wall.')
        elif (num == 1):
            print('1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall.')
        else:
            print(f'{num} bottles of beer on the wall, {num} bottles of beer. Take one down and pass it around, {num - 1} bottles of beer on the wall.')
        num -= 1
    return "No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall."


print(bottle_song(99))
