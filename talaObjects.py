# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 18:13:57 2021

@author: Nils
"""

import pandas as pd
import numpy as np
from financialStatements import finStatTemplate

class Costs:
    # The class Costs defines how much we think to pay for services, goods, ...
    
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
      

class Bungalows(object):
    
    prize = PrizeList()
    cost = Costs()
    
    def __init__(self, guestID, guestAttributes, headerFinStat, df_finStat):
        self.guestID = guestID                              # np.int64
        self.guestAttributes = guestAttributes              # pd.DataFrame
        self.headerFinStat = headerFinStat                  # column names
        self.df_finStat = df_finStat                        # pd.DataFrame
        self.name = type(self).__name__                     # name of talaObject
        #self.df_temp = finStatTemplate(headerFinStat)       # empty DataFrame
        
    def giveBack(self):                                     # not used
        modifiedFinStat = self.df_finStat
        return self.guestID
        return self.df_finStat

    def funcName(self, function):
        print(function.__name__)
    ### Debit
            
    def cost_perGuest(self):
        # Collect variables
        funName = "cost_perGuest"
        nights = np.single(self.guestAttributes["NightsInBungalow"])
        water_shower = 10 * 12                                              # L, min * 12 L/min
        water_toilet = 5 * 6                                                # L, flushes * 6 L/flush
        electricity_AC = 12 * 1                                             # kWh, hrs * kW
        water = nights * (water_shower + water_toilet) * 0.001 * self.cost.water_m3
        electricity = nights * electricity_AC * self.cost.electricity_kWH
        cost = - (water + electricity)

        #["talaObjects","GuestID","StatementID","Debit(-)", "Credit(+)"]
        columns = self.headerFinStat                                                    # column names
        funName = self.name + ": " + funName
        tmp = [[funName, self.guestID, "NA", cost, 0]]                                # data
        tmp = pd.DataFrame(data=tmp, columns=columns)                                   # single DataFrame
        self.df_finStat = pd.concat([self.df_finStat, tmp], axis=0, ignore_index=True)  # concatenate
    
        return self.df_finStat
    
    ### Credit                    
        
    
    def revenue_perGuest(self):
        # Collect variables
        funName = "revenue_perGuest"
        nights = np.single(self.guestAttributes["NightsInBungalow"])     # float32
        prizePerNight = np.single(self.prize.bungalowsPerNight)             # float32
        revenue = np.int64(nights * prizePerNight)                          # int64

        #["talaObjects","GuestID","StatementID","Debit(-)", "Credit(+)"]
        columns = self.headerFinStat                                                    # column names
        funName = self.name + ": " + funName
        tmp = [[funName, self.guestID, "NA", 0, revenue]]                             # data
        tmp = pd.DataFrame(data=tmp, columns=columns)                                   # single DataFrame
        self.df_finStat = pd.concat([self.df_finStat, tmp], axis=0, ignore_index=True)  # concatenate

        return self.df_finStat
        
    
# TESTING
# test DataFrame 
l1 = [[1, 3, "credit-card"]]
l2 = ["GuestID","NightsInBungalow","PaymentMethod"]
test = pd.DataFrame(data=l1, dtype=str, columns=l2) 

tmp_list = None
tmp_columns = ["talaObjects","GuestID","StatementID","Debit(-)", "Credit(+)"]
tmp_finStat = pd.DataFrame(data=tmp_list, columns=tmp_columns) 
tmp_headerFinStat = ["talaObjects", "GuestID", "StatementID", "Debit(-)", "Credit(+)"]

z=Bungalows(1,test,tmp_headerFinStat,tmp_finStat)
