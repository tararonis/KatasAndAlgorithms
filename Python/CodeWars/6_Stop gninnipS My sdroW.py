# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python


def spin_words(sentence: str) -> str:
    return " ".join([w[::-1] if len(w) > 4 else w for w in sentence.split(" ")])


def main():
    assert spin_words("Welcome") == "emocleW"
    assert spin_words("to") == "to"
    assert spin_words("CodeWars") == "sraWedoC"


if __name__ == "__main__":
    main()
