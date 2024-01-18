#https://www.codewars.com/kata/513e08acc600c94f01000001/train/python



def rgb(r:int, g:int, b:int) -> str:
    """
    RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.
    Return should always be 6 characters long, the shorthand with 3 will not work here.
    """    
    to_hex = lambda dec: format(dec, '02x').upper() if 0 <= dec <= 255 else "00" if dec < 0 else "FF"
    return to_hex(r) + to_hex(g) + to_hex(b)


def rgb_2(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))


def hex_con(color):
    hex_dict = '0123456789ABCDEF'
    d1 = color//16
    d2 = color%16
    if d1 > 15:
        d1 = 15
        d2 = 15
    elif d1 < 0:
        d1 = 0
        d2 = 0
    return str(hex_dict[d1]) + str(hex_dict[d2])   


def rgb_3(r, g, b):  
    R = hex_con(r)
    G = hex_con(g)
    B = hex_con(b)
    return R+G+B


rgb_4 = lambda r, g, b: '{0:02X}{1:02X}{2:02X}'.format(max(min(r, 255), 0), max(min(g, 255), 0), max(min(b, 255), 0))