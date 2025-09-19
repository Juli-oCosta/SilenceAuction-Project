from IPython.display import clear_output

bidders = []

def auction(name, bid):
  new_bid = {'name': name, 'bid': bid}
  bidders.append(new_bid)

def winner(bidders):
  max_bid = 0
  winner_name = ""

  for dictionary in bidders:
    if dictionary['bid'] > max_bid:
      max_bid = dictionary['bid']
      winner_name = dictionary['name']

  print(f"The winner is {winner_name} with a bid of ${max_bid}")

over = False

while not over:
  while True:
    name_input = input("Type in your name: ")
    if name_input.strip() != "":
      break
    else:
      print("Invalid name! The name can not be empty or have only spaces.")

  while True:
    try:
      bid_input = float(input("Type in you bid: $"))
      break
    except ValueError:
      print("Oops! That doesn't seem to be a valid number. Please enter the bid using only digits and a decimal point (e.g., 125.50).")

  auction(name = name_input, bid = bid_input)

  while True:
    confirmation_input = input("Are there any other bidders? Type 'yes or 'no: ").lower()

    if confirmation_input == 'yes':
      clear_output()
      break
    elif confirmation_input == 'no':
      clear_output()
      winner(bidders)
      over = True
      break
    else:
      print("Invalid option. Please, type only 'yes' or 'no'.")
