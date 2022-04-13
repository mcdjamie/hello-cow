import cowsay

def say_hello() -> bool:
    cowsay.cow("Hello World!")
    return True


if __name__ == "__main__":
    say_hello()