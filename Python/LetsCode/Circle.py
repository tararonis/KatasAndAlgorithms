import random as rnd

"""
We have only func that gives float from 0 to 1. How to find the pi?
"""

def rand_float():
    return rnd.uniform(0,1)


def main():
    cir_d, total = 0, 70000
    for _ in range(total):
        x, y = rand_float(), rand_float()
        if (x**2 + y**2) ** 0.5 <= 1:  #if length of the dot is equal or less then 1 it means that the dot is in circle
            cir_d +=1

    """
    Area of a Circle / Area of a Square == count of dotes in circle / count of dots in square =>
    (pi * r**2) / (2 * r**2 * 4)== count of dotes in circle / count of dots in square =>
    pi = (cir_d * 4) / total
    """        
    print((cir_d * 4) / total)    


if __name__ == "__main__":
    main()