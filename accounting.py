# Constant variable to hold the cost of a melon
MELON_COST = 1.00

#2 Create function to track customers' payments
# Function definition and its parameters
def track_customer_payment(name, melon, actual_payment, cost = MELON_COST):
    ''' Evaluate and print out which customers are overpaid or underpaid

    Inputs:
    - name of customer
    - number of melon bought
    - what he actually paid
    - the cost of one melon (constant)
    Output:
    - print out customer name, what he paid and what he is supposed to pay

    '''
    # What customer is supposed to pay
    expected_payment = melon * cost
    # Check if his actual payment is not the same as his expected payment
    if expected_payment != actual_payment:
        # print out a statement with customer name, his actual and his expected payment
        print(f"{name} paid ${actual_payment}, expected ${expected_payment}")
        

#1 Create a function to read text file and save customer's data
# Function definition and its parameter
def get_customer_data(path):
    ''' Process the input file and generate customer data report'''

    # Open the file passed in and assign to input_file
    input_file = open(path)
    # Read through each line in the file
    for line in input_file:
        # Remove whitespace on the right of the line
        line = line.rstrip()
        # Split the line into a list of strings seperated by '|'
        customer_data = line.split('|')

        # Assign some variables to hold the customers' data, and change to appropriate data type of int or float
        customer_name = customer_data[1]
        customer_melon = int(customer_data[2])
        customer_paid = float(customer_data[3])

        # Invoke function track_customer_payment 
        track_customer_payment(customer_name, customer_melon, customer_paid)
    # Close the file after processing all lines    
    input_file.close()

# Invoke the function get_customer_data and pass in the text file
get_customer_data("customer-orders.txt")


