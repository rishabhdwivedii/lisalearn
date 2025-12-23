def check_even(number):
    if number % 2 == 0:
        return True
    else:
        raise Exception("Number is not even")

# simulate a test
try:
    check_even(4)
    print("TEST PASSED")
except Exception as e:
    print("TEST FAILED:", e)





def check_positive(number):
    if number >= 0:
        return True
    else:
        raise Exception("Number is not positive")

#simulating test
try: 
    check_positive(-1)
    print("Test Passed for +ve")
except Exception as e:
    print("Failed", e)