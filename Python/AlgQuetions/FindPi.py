import random as rnd
import matplotlib.pyplot as plt

#We have only func that gives float from 0 to 1. How to find the pi?

def calc_pi(n):
    cir_d, total = 0, n
    round_dots = []
    square_dots = []

    for _ in range(total):
        x, y = rnd.uniform(0,1), rnd.uniform(0,1)
        if (x**2 + y**2) ** 0.5 <= 1:  #if length of the dot is equal or less then 1 it means that the dot is in circle
            cir_d += 1
            round_dots.append([x,y])
            round_dots.append([-x,y])
            round_dots.append([x,-y])
            round_dots.append([-x,-y])
        else:
            square_dots.append([x,y])
            square_dots.append([-x,y])
            square_dots.append([x,-y])
            square_dots.append([-x,-y])
            
    plt.scatter([pair[0] for pair in round_dots], [pair[1] for pair in round_dots])
    plt.scatter([pair[0] for pair in square_dots], [pair[1] for pair in square_dots])

    plt.show()

    
    # Area of a Circle / Area of a Square == count of dotes in circle / count of dots in square =>
    # (pi * r**2) / (2 * r**2 * 4)== count of dotes in circle / count of dots in square =>
    # pi = (cir_d * 4) / total
       
    print((cir_d * 4) / total)    


def main():
    calc_pi(1000)

if __name__ == "__main__":
    main()