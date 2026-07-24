# Simulated database of valid promotional discount codes
valid_promo_codes = {"SUMMER20": 0.20, "WELCOME10": 0.10}

def process_payment(amount_input, promo_code):
    try:
        # 1. Handle ValueError: Convert raw user text input to a float number
        clean_amount = float(amount_input)
        
        # 2. Handle KeyError: Look up the coupon code discount rate
        # If the code isn't in our dictionary, a KeyError triggers 

        discount_rate = valid_promo_codes[promo_code]     #discount_rate = valid_promo_codes["SUMMER20"] anwers 0.20  
        print(discount_rate)
      
        # Calculate final amount after discount
        discount_amount = clean_amount * discount_rate
        final_total = clean_amount - discount_amount
      """
      : starts the formatting rule..2 means "show exactly 2 decimal places".f means "treat this as a float number" (a decimal).
      """
        print(f"Payment successful! Charged: ${final_total:.2f}")    #5.6666666:.2f5.67 (rounds up automatically!)

    except ValueError:
        # Triggers if amount_input contains letters like "fifty dollars"
        print("Error: Please enter a valid numerical amount (e.g., 50.00).")
        
    except KeyError:
        # Triggers if the promo code is expired or misspelled
        print(f"Error: The promo code '{promo_code}' is invalid or expired.")
        
    except Exception as general_error:
        # A safety net that catches any other unexpected runtime error
        print(f"An unexpected critical system error occurred: {general_error}")
        
    finally:
        # This block ALWAYS runs, useful for cleanup actions
        print("Transaction session closed cleanly.")



#Case 1: The Successful Run (No Errors)
process_payment("100.00", "SUMMER20")
#Case 2: How to trigger the ValueError
process_payment("hundred", "SUMMER20")
#Case 3: How to trigger the KeyError
process_payment("100.00", "WINTER50")
#Case 4: How to trigger the general Exception
process_payment("100.00", [100, 200])



"""
Output for all error  or successful 

1)process_payment("100.00", "SUMMER20")   #for successfull

0.2
Payment successful! Charged: $80.00
Transaction session closed cleanly.

2) process_payment("hundred", "SUMMER20")

Error: Please enter a valid numerical amount (e.g., 50.00).
Transaction session closed cleanly.

3) process_payment("100.00", "WINTER50")


Error: The promo code 'WINTER50' is invalid or expired.
Transaction session closed cleanly.

4) process_payment("100.00", [100, 200])

An unexpected critical system error occurred: unhashable type: 'list'
Transaction session closed cleanly.
