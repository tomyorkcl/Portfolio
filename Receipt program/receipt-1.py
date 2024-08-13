import csv
from datetime import datetime
from datetime import date
import random


today = date.today()
now = datetime.now()
day = now.strftime('%A')
days = str(day)
hour = now.strftime('%H')
hours = int(hour)


#function to do the coupon code
random_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(random_number)
number_code = []
random_numer_function = [random_number[0], random_number[1], random_number[2], random_number[3], random_number[4], random_number[5]]
random_code = number_code.append(random_numer_function)

    


def main():

    # Import the datetime class from the datetime
    # module so that it can be used in this program.

    # Call the now() method to get the current
    # date and time as a datetime object from
    # the computer's operating system.
    current_date_and_time = datetime.now()

    KEY_INDEX = 0
    PRODUCT = 1
    PRICE = 2

    market_name = 'Junji Store'
    print(market_name)

    products_dict = read_dictionary('products.csv', KEY_INDEX)

    plus = []
    quantity = []

    with open('request.csv', "rt") as request_list:
        reader_request = csv.reader(request_list)
        next(reader_request)
    
        for request_item in reader_request:
    #This function works: request_item[0] - [1] = gives me the 'key' from request_list and products_dict[request_item[0]][1] = gives me 'in product list, give me the name through the 'key' code.
            print("Product: " + products_dict[request_item[0]][1] + " x " + request_item[1] + " = each $" + products_dict[request_item[0]][2])
    #preparing results to be used in plus list then plus the results in there
            mult = float(request_item[1])
            mult_two = float(products_dict[request_item[0]][2])
            subtotal = mult * mult_two
            #prices to float
            result = float(subtotal)
            plus.append(result)
            #quantity to int
            result_two = int(request_item[1])
            quantity.append(result_two)

    #preparing the plus elements to get the subtotal (list plus +)        
    suma = 0.0 #here is the result from the plus [total in price]
    for num in plus:
        suma += num
    #preparing quantity of products to plus each other
    suma_two = 0 #here is the result from the plus [total quantity]
    for quant in quantity:
        suma_two += quant
    #calculate taxes for 6%
    taxes = suma * 0.06
    #result of TOTAL
    total = taxes + suma
    #discount from 10%
    discount = (suma * 10) / 100

    if days == 'Tuesday':

        print('----------------------')
        print(f'Number of Items: {suma_two}')
        print(f'Subtotal: ${suma:.2f}')
        print(f'Taxes: ${taxes:.2f}')
        print(f'discount: $-{discount:.2f}')
        print('----------------------')
        print(f'Total: ${total - discount:.2f}')
        print('----------------------')
        print('Thank you for shopping at the -Junji Store-.')
        print('We love the opinion from our clients, please take this survey to calificate our client service')
        print('Survey: survey.client.com/survey')
        print('----------------------')
        print(f'COUPON CODE: {number_code}')

    elif days == 'Wednesday':
   
        print(f'Number of Items: {suma_two}')
        print(f'Subtotal: ${suma:.2f}')
        print(f'Taxes: ${taxes:.2f}')
        print(f'discount: $-{discount:.2f}')
        print('----------------------')
        print(f'Total: ${total - discount:.2f}')
        print('----------------------')
        print('Thank you for shopping at the -Junji Store-.')
        print('We love the opinion from our clients, please take this survey to calificate our client service')
        print('Survey: survey.client.com/survey')
        print('----------------------')
        print(f'COUPON CODE: {number_code}')
    
    elif hours <= 11:
   
        print(f'Number of Items: {suma_two}')
        print(f'Subtotal: ${suma:.2f}')
        print(f'Taxes: ${taxes:.2f}')
        print(f'discount: $-{discount:.2f}')
        print('----------------------')
        print(f'Total: ${total - discount:.2f}')
        print('----------------------')
        print('Thank you for shopping at the -Junji Store-.')
        print('We love the opinion from our clients, please take this survey to calificate our client service')
        print('Survey: survey.client.com/survey')
        print('----------------------')
        print(f'COUPON CODE: {number_code}')

    else:
   
        print(f'Number of Items: {suma_two}')
        print(f'Subtotal: ${suma:.2f}')
        print(f'Taxes: ${taxes:.2f}')
        print('----------------------')
        print(f'Total: ${total:.2f}')
        print('----------------------')
        print('Thank you for shopping at the -Junji Store-.')
        print('We love the opinion from our clients, please take this survey to calificate our client service')
        print('Survey: survey.client.com/survey')
        print('----------------------')
        print(f'COUPON CODE: {number_code}')



    # Use an f-string to print the current
    # day of the week and the current time.
    print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y}")

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



#if days == 'Tuesday':
#    print (f'Your subtotal is: ${subtotal:.2f}')
#    print (f'discount: ${discount:.2f}')
 #   print (f'taxes: ${taxes:.2f}.')
  #  print (f'Total: ${subtotal - discount + taxes:.2f}')

#elif days == 'Wednesday':
#    print (f'Your subtotal is: ${subtotal:.2f}')
 #   print (f'discount: ${discount:.2f}')
  #  print (f'taxes: ${taxes:.2f}.')
   # print (f'Total: ${subtotal - discount + taxes:.2f}')

#elif subtotal >= 50.00:
#    print (f'Your subtotal is: ${subtotal:.2f}')
#    print (f'discount: ${discount:.2f}')
#    print (f'taxes: ${taxes:.2f}.')
#    print (f'Total: ${subtotal - discount + taxes:.2f}')

#else:
#    print (f'Your subtotal is: ${subtotal:.2f}')
#    print (f'discount: $00.00')
#    print (f'taxes: ${taxes:.2f}.')
#    print (f'Total: ${subtotal + taxes:.2f}')
