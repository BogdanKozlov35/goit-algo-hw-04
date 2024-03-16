from pathlib import Path
import sys
from colorama import Fore, Back, Style


def main():
    if len(sys.argv) < 2:
        user_input = ""
    else:
        user_input = sys.argv[1]
    path = Path(user_input)
    if path.exists():
        if path.is_dir():
            items = path.iterdir()
            for item in items:
                print(f"{Fore.RED}{item}") if item.is_dir() else print(f"{Fore.GREEN}{item}")

            print(Style.RESET_ALL)
        else:
            return (f"{path} is a file")
    else:
        return (f"{path} is not exist")


if __name__ == '__main__':
    main()
