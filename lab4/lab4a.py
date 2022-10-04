
def split_it(encodedmessage):
    understring = ''
    upperstring = ''
    for char in encodedmessage:
        if char.isupper():
            upperstring += char
        if char in [' ', '|']:
            upperstring += char

    for char in encodedmessage:
        if char.islower():
            understring += char
        if char in ['_', '.']:
            understring += char
    print(understring + ", " + upperstring)
    return understring, upperstring 

def split_rec(encodedmessage):

    if encodedmessage == "":
         return "", ""

    low, up = split_rec(encodedmessage[1:])
    if encodedmessage[0].islower():
        low = encodedmessage[0] + low
    elif encodedmessage[0].isupper():
        up = encodedmessage[0] + up
    if encodedmessage[0] in ['_', '_']:
        low = encodedmessage[0] + low
    elif encodedmessage[0] in [' ', '|']:
        up = encodedmessage[0] + up

    return low, up


