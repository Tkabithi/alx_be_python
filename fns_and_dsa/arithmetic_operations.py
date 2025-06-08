def perform_operation(num1: float, num2: float, operation: str) -> float:
    """
    Performs basic arithmetic operations on two numbers.
    
    Args:
        num1: First number (float)
        num2: Second number (float)
        operation: Arithmetic operation to perform ('add', 'subtract', 'multiply', or 'divide')
        
    Returns:
        Result of the operation (float), or error message string for division by zero
        
    Raises:
        ValueError: If invalid operation is provided
    """
    operation = operation.lower().strip()
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: division by zero"  # Return error message as string
        return num1 / num2
    else:
        raise ValueError("Error: Invalid operation. Must be one of: 'add', 'subtract', 'multiply', 'divide'")
