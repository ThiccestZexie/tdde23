
def split_it(encoded_message):
    low = ''
    up = ''
    for char in encoded_message:
        if char.isupper():
            up += char
        if char in [' ', '|']:
            up += char

    for char in encoded_message:
        if char.islower():
            low += char
        if char in ['_', '.']:
            low += char
    return low, up 


def split_rec(encoded_message):

    if encoded_message == "":
         return "", ""

    low, up = split_rec(encoded_message[1:])

    if encoded_message[0].islower():
        low = encoded_message[0] + low
    elif encoded_message[0].isupper():
        up = encoded_message[0] + up
    if encoded_message[0] in ['.', '_']:
        low = encoded_message[0] + low
    elif encoded_message[0] in [' ', '|']:
        up = encoded_message[0] + up

    return low, up


