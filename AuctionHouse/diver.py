from user import User
from auctionListing import AuctionListing
from bid import Bid
from auctionSystem import AuctionSystem

class Driver:
    def run(self):
        print('create two user')
        user1 = User('Nish','test@gmail','ionionasad4s')
        user2 = User('Kody','test2@gmail','ionionasad4s')

        print('created the auction system')
        auctionSystem = AuctionSystem()
        
        print('Add five listings')
        listing1 = AuctionListing(user1, 100, "Laptop", 10)
        listing2 = AuctionListing(user1, 400, "Laptop", 210)
        listing3 = AuctionListing(user1, 200, "Laptop", 5)

        auctionSystem.addAuctionListing(listing1)
        auctionSystem.addAuctionListing(listing2)
        auctionSystem.addAuctionListing(listing3)

        print('display all listings')
        listings = auctionSystem.getAllAuctionListings()
        for listing in listings:
            print(listing.getListingDetils())
        
        print('place a bid ')
        auctionSystem.bidOnAuctionListing(listing1, 500, user2)

        print('display all listings after bid')
        listings = auctionSystem.getAllAuctionListings()
        for listing in listings:
            print(listing.getListingDetils())
        
        print('messages of user1')
        msg1= user1.getLatestmessage()
        print('msg1',msg1)



if( __name__=='__main__'):
    driver = Driver()
    driver.run()
