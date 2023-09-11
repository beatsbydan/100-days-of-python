# Secret Auction Program

def get_highest_bidder(bidders):
    winner = ""
    highest_bid = 0
    for bidder in bidders:
        print(bidders[bidder])
        if bidders[bidder] > highest_bid:
            highest_bid = bidders[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    
available = True

bidders = {} 

while available:
    name = input("What is your name?: ")
    amount = int(input("How much is your bid?: $"))
    more_bidders = input("Are there any other users? Yes ot No: ").lower()
    bidders[name] = amount
    
    if more_bidders == "no":
        get_highest_bidder(bidders=bidders)
        available = False
