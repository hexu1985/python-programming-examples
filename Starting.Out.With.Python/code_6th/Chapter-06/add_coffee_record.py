# This program adds coffee inventory records to
# the coffee.txt file.

def main():
    # Create a variable to control the loop.
    another = 'y'

    # Open the coffee.txt file in append mode.
    with open('coffee.txt', 'a') as coffee_file:
        # Add records to the file.
        while another == 'y' or another == 'Y':
            # Get the coffee record data.
            print('Enter the following coffee data:')
            descr = input('Description: ')
            qty = int(input('Quantity (in pounds): '))

            # Append the data to the file.
            coffee_file.write(f'{descr}\n')
            coffee_file.write(f'{qty}\n')

            # Determine whether the user wants to add
            # another record to the file.
            print('Do you want to add another record?')
            another = input('Y = yes, anything else = no: ')

    print('Data appended to coffee.txt.')

# Call the main function.
if __name__ == '__main__':
    main()