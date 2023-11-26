from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.

print(art.logo)

bids = {}
response = "yes"

def add_bid():
  name = input("What's your name? ")
  bid_price = input("what's your bid? $")
  bids[name] = int(bid_price)


def check_highest_bidder():
  highest_bidder = ""
  highest_bid = 0
  for name in bids:
    if bids[name] > highest_bid:
      highest_bid = bids[name]
      highest_bidder = name
  print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
  
while response == "yes":
  add_bid()
  response = input("Are there any other bidders? Type 'yes' or 'no'. ")
  clear()

if response == "no":
  check_highest_bidder()
    