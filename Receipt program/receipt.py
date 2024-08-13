# Created by: Tomas Contreras, student from BYU Idaho

import csv

def main():

    KEY_INDEX = 0
    PRODUCT = 1
    PRICE = 2

    products_dict = read_dictionary('products.csv', KEY_INDEX)
    print(f'All products: {products_dict}')

    with open('request.csv', "rt") as request_list:
        reader_request = csv.reader(request_list)
        next(reader_request)
   
        for request_item in reader_request:
                #This function works: request_item[0] - [1] = gives me the 'key' from request_list and products_dict[request_item[0]][1] = gives me 'in product list, give me the name through the 'key' code.
                print("Product name: " + products_dict[request_item[0]][1] + " Quantity: " + request_item[1] + " Price: $" + products_dict[request_item[0]][2])
        
def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
  dictionary and return the dictionary.
  Parameters
      filename: the name of the CSV file to read.
      key_column_index: the index of the column
          to use as the keys in the dictionary.
  Return: a compound dictionary that contains
      the contents of the CSV file.
  """
    dictionary = {}


    with open(filename, "rt") as csv_file:
    # Open the text file for reading and store a reference
    # to the opened file in a variable named csv_file.

        reader = csv.reader(csv_file)
        next(reader)

        for row_list in reader:

            key = row_list[key_column_index]
            
            dictionary[key] = [row_list[0], row_list[1], row_list[2]]
            #this function works = key : [key, name, price]


    return dictionary
            
if __name__ == "__main__":
    main()