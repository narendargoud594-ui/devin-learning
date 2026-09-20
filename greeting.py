def greet(name):
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


def goodbye(name):
    """Return a goodbye message for the given name."""
    return f"Goodbye, {name}!"


def is_valid_name(name):
    """Check if the name is valid (not empty or whitespace only)."""
    return name.strip() != ""


def format_customer_id(customer_id):
    """Return a formatted customer ID string."""
    return f"Customer ID: {customer_id}"


if __name__ == "__main__":
    customer_id = input("Enter your customer ID: ")
    name = input("Enter your name: ")
    if is_valid_name(name):
        print(format_customer_id(customer_id))
        print(greet(name))
        print(goodbye(name))
    else:
        print("Please enter a valid name.")
