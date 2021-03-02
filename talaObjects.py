# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 18:13:57 2021

@author: Nils
"""


class Costs:
    # The class Costs defines how much we think to pay for 
    
    # Unit: IDR
    
    electricity_kWH = 1500 # equals 1 EUR per kWh
    water_m3 = 5000 # equals 3-4 EUR per cubic meter
    
    def fixedCost_annual(self):
        pass
    
class PrizeList:
    # The class PrizeList defines the prizes which ultimately limit the revenue.
    
    # Unit: IDR
    
    bungalowsPerNight = 700000 # equals 40-45 EUR
    yogaClassSita = 100000 # equals 6-7 EUR
    yogaClassOther = 40000 # equlas 2-3 EUR
      

class Bungalows:
    
    prizes = PrizeList()
    
    
    def __init__(self, guestName):
        print("Hi, I am " + guestName + ". Message origin: Bungalows")
        
    def cost_perGuest(self):
        pass
        
    def revenue_perGuest(self, nights):
        return self.prizes.bungalowsPerNight*nights
        
