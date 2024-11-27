from collections.abc import Iterable

def greet(names: Iterable[str]) -> str | None:
    for name in names:
        print(name)

    return None

greet('1234')