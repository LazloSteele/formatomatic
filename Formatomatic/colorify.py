class Colorify:
    PREFIX = "\033["
    POSTFIX = "m"
    FG_PREFIX = "3"
    JOIN_PREFIX = ";"
    BG_PREFIX = "4"

    RESET = f"{PREFIX}0{POSTFIX}"

    BLACK = "0"
    RED = "1"
    GREEN = "2"
    YELLOW = "3"
    BLUE = "4"
    MAGENTA = "5"
    CYAN = "6"
    WHITE = "7"

    @staticmethod
    def color_text(text: str, text_color=None, bg_color=None):

        color_code = ""

        if text_color or bg_color:
            color_code += Colorify.PREFIX
            if text_color:
                color_code += Colorify.FG_PREFIX + text_color
            if text_color and bg_color:
                color_code += Colorify.JOIN_PREFIX
            if bg_color:
                color_code += Colorify.BG_PREFIX + bg_color
            color_code += Colorify.POSTFIX

        return color_code + text + Colorify.RESET
