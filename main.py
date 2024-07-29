from colorify import Colorify


def main(text: str):
    return Colorify.color_text(text, Colorify.CYAN, Colorify.YELLOW)


if __name__ == "__main__":
    print(main("Hello World!"))
    print("Hello World AGAIN!")
