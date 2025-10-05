def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
        return print(f"The result of the division is {result:.1f}")
    except:
        if denominator == 0:
            return print ("Error: Cannot divide by zero.")
        else:
            return print("sklss")
   
    