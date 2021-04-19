"""
https://www.codewars.com/kata/5848565e273af816fb000449/train/python
"""


def encrypt_this(text: str) -> str:
    """Function that takes string and "encrypt" it with follow rules:
    - first letter convert to ASCII;
    - replace second and last letters.
    Then return the results string.

    Args:
        text (str): income string

    Returns:
        str: encrypted string
    """
    result = []

    for word in text.split():
        # turn word into a list
        word = list(word)

        # replace first letter with ascii code
        word[0] = str(ord(word[0]))

        # switch 2nd and last letters
        if len(word) > 2:
            word[1], word[-1] = word[-1], word[1]

        # add to results
        result.append("".join(word))

    return " ".join(result)


def main():
    print(
        encrypt_this("A wise old owl lived in an oak")
        == "65 119esi 111dl 111lw 108dvei 105n 97n 111ka"
    )


if __name__ == "__main__":
    main()
