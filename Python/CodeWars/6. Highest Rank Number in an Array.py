def multiplication_table(row, col):

    return [[(x + 1) * (y + 1) for x in range(col)] for y in range(row)]


def main():
    print(multiplication_table(3, 4) == [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12]])
    print(multiplication_table(2, 2) == [[1, 2], [2, 4]])
    print(multiplication_table(3, 3) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]])
    print(
        multiplication_table(4, 4)
        == [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]]
    )
    print(multiplication_table(2, 5) == [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10]])


if __name__ == "__main__":
    main()
