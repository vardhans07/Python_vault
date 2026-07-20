# 1. DEFINE THE DECORATOR
def my_logger(my_func_45):
    def my_task():
        print(">> Starting Execution   ")
        my_func_45()  # Executes the original function
        print(">> Finished Execution   ")
    
    return  my_task  # Return the inner function without calling it ()

# 2. APPLY THE DECORATOR TO FUNCTION #1
@my_logger
def say_hello():
    print("Hello, World!")

# 3. APPLY THE DECORATOR TO FUNCTION #2
@my_logger
def calculate_sum():
    print("Calculating: 5 + 5 =", 5 + 5)
    
@my_logger	
def md_i():
    play=print("hii")


# 4. RUN THE FUNCTIONS
say_hello()
print()  # Empty line for clean output
calculate_sum()
print()  # Empty line for clean output
md_i()

Output:

>> Starting Execution   
Hello, World!
>> Finished Execution   

>> Starting Execution   
Calculating: 5 + 5 = 10
>> Finished Execution   

>> Starting Execution   
hii
>> Finished Execution   

=== Code Execution Successful ===
