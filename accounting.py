MELON_COST = 1.00

#2 Create function to evaluate if a customer is behind in payments
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
    
    expected_payment = melon * cost
    if expected_payment != actual_payment:
        print(f"{name} paid ${actual_payment}, expected ${expected_payment}")
        

#1 Create a function to read text file and save customer's data
def get_customer_data(path):
    ''' Process the input file and generate customer data report'''

    input_file = open(path)
    for line in input_file:
        line = line.rstrip()
        customer_data = line.split('|')

        # print(customer_data)

        customer_name = customer_data[1]
        customer_melon = int(customer_data[2])
        customer_paid = float(customer_data[3])

        track_customer_payment(customer_name, customer_melon, customer_paid)

get_customer_data("customer-orders.txt")


