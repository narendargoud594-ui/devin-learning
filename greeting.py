def greet(name):
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


def goodbye(name):
    """Return a goodbye message for the given name."""
    return f"Goodbye, {name}!"


def is_valid_name(name):
    """Check if the name is valid (not empty or whitespace only)."""
    return name.strip() != ""


if __name__ == "__main__":
    name = input("Enter your name: ")
    if is_valid_name(name):
        print(greet(name))
        print(goodbye(name))
    else:
        print("Please enter a valid name.")
