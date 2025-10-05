def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
        return print(f"The result of the division is {result:.1f}")
    except:
        if denominator == 0:
            return print ("Error: Cannot divide by zero.")
        if ValueError(numerator):
            return print ("Error: Please enter numeric values only.")
        if ValueError(denominator):
            return print ("Error: Please enter numeric values only.")
   
    