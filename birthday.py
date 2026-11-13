"""Is it my birthday? Wrong once, then never again."""
import sys
from datetime import date
from pathlib import Path

MEMORY = Path(__file__).with_name("birthday.txt")


def is_it_my_birthday(today=None):
    today = today or date.today()
    return MEMORY.exists() and MEMORY.read_text() == f"{today:%m-%d}"


def it_is_actually(today=None):
    today = today or date.today()
    MEMORY.write_text(f"{today:%m-%d}")


if __name__ == "__main__":
    if sys.argv[1:] == ["it", "is"]:
        it_is_actually()
        print("Sorry. Happy birthday. It won't happen again.")
    else:
        print("Yes. Happy birthday." if is_it_my_birthday() else "No.")
