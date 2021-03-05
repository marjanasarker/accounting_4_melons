#cost of melon will be a global variable which can be changed if another fruit used or cost of melon changes
melon_cost = 1.00

def customer_payment(file_path):
    '''Figuring out which one of these customers overpaid or underpaid'''
    order_file = open(file_path)
    for line in order_file:
        line = line.rstrip()
        #splitting at | to get list of strings which will separate name, quantity of melons purchased and how much they paid. 
        words = line.split('|')
        #print(words)
        customer_name = words[1]
        qty_purchased = words[2]
        #change to floats for numerical calulations
        customer_payment = float(words[3])
        expected = float(melon_cost)*float(qty_purchased)
        # we will only print out the names of customers who overpaid or underpaid
        if expected > customer_payment:
            print(f'{customer_name} underpaid. Expected: ${expected} Paid: ${customer_payment}.')
        else:
            print(f'{customer_name} overpaid. Expected: ${expected} Paid: ${customer_payment}.')


customer_payment("customer-orders.txt")
