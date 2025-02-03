from user import User
from auctionListing import AuctionListing
from bid import Bid

class Driver:
    def run():
        print('create two user')
        user1 = User('Nish','test@gmail','ionionasad4s')
        user1 = User('Kody','test2@gmail','ionionasad4s')

        print('Add five listings')
        listing1 = AuctionListing(user1.id, )