# This program allows the user to delete
# a record in the coffee.txt file.

import os  # Needed for the remove and rename functions

def main():
    # Create a bool variable to use as a flag.
    found = False

    # Get the coffee to delete.
    search = input('Which coffee do you want to delete? ')
    
    # Open the original coffee.txt file and the temporary file.
    with open('coffee.txt', 'r') as coffee_file, open('temp.txt', 'w') as temp_file:
        # Read the first record's description field.
        descr = coffee_file.readline()

        # Read the rest of the file.
        while descr != '':
            # Read the quantity field.
            qty = float(coffee_file.readline())

            # Strip the \n from the description.
            descr = descr.rstrip('\n')

            # If this is not the record to delete, then
            # write it to the temporary file.
            if descr != search:
                # Write the record to the temp file.
                temp_file.write(f'{descr}\n')
                temp_file.write(f'{qty}\n')
            else:
                # Set the found flag to True.
                found = True

            # Read the next description.
            descr = coffee_file.readline()

    # Delete the original coffee.txt file.
    os.remove('coffee.txt')

    # Rename the temporary file.
    os.rename('temp.txt', 'coffee.txt')

    # If the search value was not found in the file
    # display a message.
    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')

# Call the main function.
if __name__ == '__main__':
    main()