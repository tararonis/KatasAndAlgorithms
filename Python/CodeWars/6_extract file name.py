"""https://www.codewars.com/kata/597770e98b4b340e5b000071/train/python"""


def extract_file_name(s):
    start = s.find("_") + 1
    end = s.rfind(".")
    return s[start:end]


def main():
    print(
        extract_file_name("1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION")
        == "FILE_NAME.EXTENSION"
    )


if __name__ == "__main__":
    main()
