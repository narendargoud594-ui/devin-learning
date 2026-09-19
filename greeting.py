def greet(name):
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


def goodbye(name):
    """Return a goodbye message for the given name."""
    return f"Goodbye, {name}!"


if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet(name))
    print(goodbye(name))
