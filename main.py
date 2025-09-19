bidders = []

def auction(name, bid):
  new_bid = {'name': name, 'bid': bid}
  bidders.append(new_bid)

def winner(bidders):
  max_bid = 0
  winner_name = ""

  for dictionary in bidders:
    if bid > max_bid:
      max_bid = bid
      winner_name = 

over = False

while not over:
  input_name = input("Type in your name: ")

  while True:
    try:
      bid_input = float(input("What is your bid?: $"))
      break
    except ValueError:
      print("Invalid option. Please, type only a real price with numbers.")

  auction(name = name_input, bid = bid_input)

  while True:
    confirmation_input = input("Are there any other bidders? Type 'yes or 'no").lower()

    if confirmation_ input == 'yes':
      break
    elif confirmation_input == 'no':
      winner(bidders)
      over = True
    else:
      print("Invalid option. Please, type only 'yes' or 'no'.")
