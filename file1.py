"""Addition function module."""


def add(a, b):
    """
    Add two numbers and return the result.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of a and b
    """
    return a + b


if __name__ == "__main__":
    # Test the addition function
    result = add(5, 3)
    print(f"5 + 3 = {result}")
    
    result = add(10, 20)
    print(f"10 + 20 = {result}")
    
    result = add(-5, 8)
    print(f"-5 + 8 = {result}")
