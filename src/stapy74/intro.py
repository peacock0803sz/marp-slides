def without_typing(s):
    return "Hello" + s


without_typing("EuroPython")


def with_typing(s: str) -> str:
    return "Hello" + s


with_typing("EuroPython")
#


with_typing(1)
without_typing(1)
