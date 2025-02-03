from auctionStatus import AuctionStatus
from uuid import uuid4
from typing import List
from bid import Bid

class AuctionListing:
    def __init__(self, userId, price, productName, duration):
        self.id = uuid4()
        self.userId = userId
        self.price = price
        self.productName = productName
        self.duration = duration
        self.highestBid = 0
        self.bids: List[Bid] = []
        self.status = AuctionStatus.Active
    
    def getAllBids(self):
        return self.bids
    
    def bidOnListing(self, userId, price):
        newBid = Bid(userId,self.id, price)
        self.bids.append(newBid)
        if(price>self.highestBid):
            self.highestBid = price
    
    def deactivateBid(self):
        self.status = AuctionStatus.Inactive
        
    

    


        
