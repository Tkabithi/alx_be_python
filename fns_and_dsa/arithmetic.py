def perform_operation(num1: float, num2: float, operation: str) -> float:
   
    operation = operation.lower().strip()
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return None  # Indicates division by zero
        return num1 / num2
    else:
        raise ValueError("Invalid operation. Must be one of: 'add', 'subtract', 'multiply', 'divide'")
