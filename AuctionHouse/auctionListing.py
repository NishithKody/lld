from auctionStatus import AuctionStatus
from uuid import uuid4
from typing import List
from bid import Bid
from user import User
from message import Message

class AuctionListing:
    def __init__(self, user:User, price, productName, duration):
        self.id = uuid4()
        self.user = user
        self.price = price
        self.productName = productName
        self.duration = duration
        self.highestBid = 0
        self.bids: List[Bid] = []
        self.status = AuctionStatus.Active
    
    def getListingDetils(self):
        return f"Product: ${self.productName} Price: ${self.price} Highest Bid: ${self.highestBid} Duration: ${self.duration}"
    
    def getAllBids(self):
        return self.bids
    
    def bidOnListing(self, user, price):
        newBid = Bid(user, price)
        self.bids.append(newBid)
        if(price>self.highestBid):
            self.highestBid = price
    
    def deactivateListing(self):
        self.status = AuctionStatus.Inactive
    
    def notifyUser(self, price):
        msg = Message("A bid has been placed for",price)
        self.user.notifyUser(msg)
    
