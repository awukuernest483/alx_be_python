def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
        print(f"The result of the division is {result:.1f}")
    except:
        if denominator == 0:
            print ("Error: Cannot divide by zero.")
        if ValueError(numerator):
            print ("Error: Please enter numeric values only.")
        if ValueError(denominator):
            print ("Error: Please enter numeric values only.")
   
    