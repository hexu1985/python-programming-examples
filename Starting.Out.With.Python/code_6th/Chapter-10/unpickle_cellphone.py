# This program unpickles CellPhone objects.
import pickle
import cellphone

# Constant for the filename.
FILENAME = 'cellphones.dat'

def main():
    end_of_file = False   # To indicate end of file
    
    # Open the file.
    with open(FILENAME, 'rb') as input_file:
        # Read to the end of the file.
        while not end_of_file:
            try:
                # Unpickle the next object.
                phone = pickle.load(input_file)

                # Display the cell phone data.
                display_data(phone)
            except EOFError:
                # Set the flag to indicate the end
                # of the file has been reached.
                end_of_file = True

# The display_data function displays the data
# from the CellPhone object passed as an argument.
def display_data(phone):
    print(f'Manufacturer: {phone.get_manufact()}')
    print(f'Model Number: {phone.get_model()}')
    print(f'Retail Price: ${phone.get_retail_price():,.2f}')
    print()

# Call the main function.
if __name__ == '__main__':
      main()