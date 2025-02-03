from typing  import List
from auctionListing import AuctionListing
from auctionStatus import AuctionStatus
from user import User

class AuctionSystem:
    def __init__(self):
        self.auctionListing: List[AuctionListing] = []
    
    def getAllAuctionListings(self):
        return self.auctionListing

    def getAllActiveAuctionListings(self):
        listings = []
        for auctionListing in self.auctionListing:
            if(auctionListing.status == AuctionStatus.Active):
                listings.append(auctionListing)
        return listings

    def bidOnAuctionListing(self, listingId, price, user: User):
        for auctionListing in self.auctionListing:
            if(auctionListing.id == listingId and auctionListing.status == AuctionStatus.Active):
                print('Listing has been found')
                auctionListing.bidOnListing(user, price)
                auctionListing.notifyUser(price)
                print('Bid has been placed')
                return True
            else:
                print('lising not found or is not active')
                return False
    
    def deactivateAuctionListings(self, currentTime):
        for auctionListing in self.auctionListing:
            if(auctionListing.duration < currentTime):
                auctionListing.deactivateListing()
                