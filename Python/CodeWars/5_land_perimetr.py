"""https://www.codewars.com/kata/5839c48f0cf94640a20001d3/train/python"""


def land_perimeter(arr:str) -> str:
    p = 0
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            if arr[x][y] == "X":
                p += 4
                if (x != len(arr) - 1) and (arr[x + 1][y] == "X"):
                    p -= 1
                if (x != 0) and (arr[x - 1][y] == "X"):
                    p -= 1
                if (y != len(arr[0]) - 1) and (arr[x][y + 1] == "X"):
                    p -= 1
                if (y != 0) and (arr[x][y - 1] == "X"):
                    p -= 1
    return "Total land perimeter: %i" % p  


def main():
    islands = [
        ["XOOXO", "XOOXO", "OOOXO", "XXOXO", "OXOOO"],
        [
            "OXOOOX",
            "OXOXOO",
            "XXOOOX",
            "OXXXOO",
            "OOXOOX",
            "OXOOOO",
            "OOXOOX",
            "OOXOOO",
            "OXOOOO",
            "OXOOXX",
        ],
        [
            "OXOOO",
            "OOXXX",
            "OXXOO",
            "XOOOO",
            "XOOOO",
            "XXXOO",
            "XOXOO",
            "OOOXO",
            "OXOOX",
            "XOOOO",
            "OOOXO",
        ],
        ["XXXXXOOO", "OOXOOOOO", "OOOOOOXO", "XXXOOOXO", "OXOXXOOX"],
        ["XOOOXOO", "OXOOOOO", "XOXOXOO", "OXOXXOO", "OOOOOXX", "OOOXOXX", "XXXXOXO"],
        ["OOOOXO", "XOXOOX", "XXOXOX", "XOXOOO", "OOOOOO", "OOOXOO", "OOXXOO"],
    ]

    for i in islands:
        print(land_perimeter(i))


if __name__ == "__main__":
    main()
