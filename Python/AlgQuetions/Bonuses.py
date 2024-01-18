# In: [1, 2, 3, 2, 3, 5, 1]
# Out: [1, 2, 3, 1, 2, 3, 1]


def getBonuses(perfomance):
    """[summary]

    Args:
        perfomance (list): the data with perfomance results of each person

    Returns:
        list: result list of bonuses

    Rules:
        -Each employee begins with a bonus factor of 1x.
        -For each employee, if the perform better than the person
        sitting next to them, the employee is given +1 higher bonus
        (and up to +2 if they perform better than both people to their sides)


    Time complexity - O(n). We do 2 passes through the array.
    Space complexity - O(n). Just need extra space for bonuses.
    """

    bonuses = len(perfomance) * [1]
    for i in range(1, len(perfomance)):
        if perfomance[i - 1] < perfomance[i]:
            bonuses[i] = bonuses[i - 1] + 1

    for i in range(len(perfomance) - 2, -1, -1):
        if perfomance[i + 1] < perfomance[i]:
            bonuses[i] = max(bonuses[i], bonuses[i + 1] + 1)

    return bonuses


def test_getBonuses(test_data):
    return getBonuses(test_data) == [1, 2, 3, 1, 2, 3, 1]


def main():
    input = [1, 2, 3, 2, 3, 5, 1]
    print(getBonuses(input))
    print(test_getBonuses(input) == True)


if __name__ == "__main__":
    main()
