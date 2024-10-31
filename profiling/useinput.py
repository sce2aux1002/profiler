from typing import Tuple

def DoInput(msg: str, options: Tuple[str,...] = ("dd",)) -> str:
    print(msg)
    for opt in options:
        print(opt)
    ind=input("Selection: ")
    return ind




