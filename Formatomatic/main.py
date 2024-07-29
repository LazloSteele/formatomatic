from Formatomatic.colorify import Colorify


def main(text: str):
    return Colorify.color_text(text, Colorify.CYAN, Colorify.YELLOW)


if __name__ == "__main__":
    print(main("Hello World!"))
    print(Colorify.color_text("No COLOR!"))
    print(Colorify.color_text("BACKGROUND ONLY", bg_color=Colorify.RED))
    print(Colorify.color_text("FOREGROUND ONLY", text_color=Colorify.YELLOW))
    print("Hello World AGAIN!")
