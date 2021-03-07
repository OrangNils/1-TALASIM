# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 21:10:24 2021

@author: Nils
"""

import pandas as pd
import numpy as np
import datetime

from tools import datePrefixISO
from tools import nextguestListID
from tools import idComposer
from tools import idDecomposer


def guestListID(path_guestListID, default=None):
    # Purpose: Check if register of guestListIDs exists. If not, create a new one.
    #          Keeps track of the generated guestListIDs.
    # 1. Define file path and file name.
    # 2. Check if register file exists.
    # 3. If exists: open register file and retrieve the latest guestListID
    # 4. If not: create a new register file "register.xlsx" and add new guestListID
    # 5. Save and close.
    # 6. Done  

    # Arguments: 
    #   path_guestListID - a relative file path to the guestListID register
    #   default - a switch to debug/develop the function, string value     
    # Variables:
    #   ... - ....
    # Output: the guestListID (string object) that is used for the next guestList    
    
    # 
    if default != None:
        return default                                  # A return statement ends the execution of the function call.
    else:
        pass
        
    path = path_guestListID
    file = "guestListID_register.xlsx"
    indicator = "G"
    datePrefix = datePrefixISO(date=datetime.date.today())
    dateSuffix = "001"
    proposedID = idComposer(indicator=indicator, prefix=datePrefix, suffix=dateSuffix)
    
    try:
        with open(path + file) as f:
            print("File exists.")
        tmp_sr = pd.read_excel(path + file, index_col=0, header=0, dtype={"guestListID_register": str}, squeeze=True)
        print(tmp_sr)
        # tmp_sr_length = len(tmp_sr.index.values)
        lastGuestListID = str(tmp_sr.iloc[-1])           # "[0]" would also select the value
        print(lastGuestListID)
        tmp_nextID = nextguestListID(inputID=lastGuestListID, proposedID=proposedID)
        print(tmp_nextID)
        tmp = pd.Series(data=[tmp_nextID], dtype=str, name="guestListID_register")
        print(tmp_sr)
        print(tmp)
        tmp_sr =pd.concat([tmp_sr, tmp], axis=0, ignore_index=True)
        print(tmp_sr)
        tmp_sr.to_excel(excel_writer=path + file, sheet_name="test")
        
        return tmp_nextID
        
    except IOError:
        print("No file found.")
        guestListID = datePrefix + dateSuffix
        tmp_df = pd.Series(data=[guestListID], dtype=str, name="guestListID_register")
        tmp_df.to_excel(excel_writer=path + file, sheet_name="test")
        
        return guestListID


### ---
# Not needed at the moment: makes the code more complicated than it needs to be 
# PROBLEMS: see comments

class guestAttributes:
    
    attributes = ["GuestID",
                  "ProfileID",
                  "NightsInBungalow",
                  "Breakfast",
                  "Lunch",
                  "Dinner",
                  "SingleParter",
                  "Scooter",
                  "YogaClass",
                  "YogaCourse",
                  "ConsumerLevel",
                  "Platform",
                  "PaymentMethod",
                  "Cafe"]

    def NightsInBungalow(self, data, nRows, guestID, profileID, nights):
        #print("I am the attribute: NightsInBungalow")
        newData = [guestID, profileID,nights,None,None,None,None,None,None,None,None,None,None,None] # PROBLEM: "None" overwrites fields. One needs to select by row AND by column.
        data.loc[nRows] = newData # loc starts counting at 0, i.e. nRows adds a new row
        return data
    
    def Breakfast(self, data, nRows, profileID, breakfastMenu):
        #print("I am the attribute: Breakfast")
        newData = [guestID, profileID,None,breakfastMenu,None,None,None,None,None,None,None,None,None,None] # PROBLEM: "None" overwrites fields. One needs to select by row AND by column.
        data.loc[nRows] = newData # loc starts counting at 0, i.e. nRows adds a new row
        return data
### ---

class guestList:
    
    # initialize Class Variables
    attributes = guestAttributes() # referred to as "self.attribute" in code

    def __init__(self,ID):
        #self.main_dataframe = pd.DataFrame(data=None, columns='a')
        self.ID = ID
        self.tmp = pd.DataFrame(data=None, columns=self.attributes.attributes)
    
    # def create(self):
    #     print("The create method is active. It returns a pandas DataFrame")
    #     self.tmp = pd.DataFrame(data=None, columns=self.attributes.attributes)
    #     return self.tmp
    
    def addProfile(self, profileID):
        # Purpose: Create data frame for financial statements.
        # Arguments: 
        #   profileID - integer, determines which guest profile to choose from        
        # Variables:
        #   self.tmp - an instance of the class, a pd data frame that grows every time that "addProfile()" is called
        # Output: the guest list "self.tmp" as pandas data frame which has the profile attached to the data frame
        print("Now online: addProfile method.")
        
        # Leave as archive for "class guestAttributes"
        ### ---
        # if profileID == 0:
        #     #print("ProfileID = " + str(profileID) + " is selected.")
        #     self.nRows = len(self.tmp.index)
        #     self.nights = 2
        #     self.breakfast = "basic"
            
        #     self.tmp = self.attributes.NightsInBungalow(data=self.tmp, nRows=self.nRows, profileID=profileID, nights=self.nights)
        #     self.tmp = self.attributes.Breakfast(data=self.tmp, nRows=self.nRows, profileID=profileID, breakfastMenu=self.breakfast)

        #     return self.tmp
        ### ---

        if profileID == 1:
            #print("ProfileID = " + str(profileID) + " is selected.")
            self.nRows = len(self.tmp.index)
           
            # specify the attributes
            self.guestID = self.nRows+1
            self.nights = 2
            self.breakfast = "basic"
            self.lunch = 1
            self.dinner = 2
            self.many = "single"
            self.scooter = 1
            self.yogaClass = 0
            self.yogaCourse = "no"
            self.consumerLevel = "low"
            self.bookingPlatform = "booking.com"
            self.paymentMethod = "credit-card"
            self.cafe = 100000
            
            newData = [self.guestID,
                       profileID,
                       self.nights,
                       self.breakfast,
                       self.lunch,
                       self.dinner,
                       self.many,
                       self.scooter,
                       self.yogaClass,
                       self.yogaCourse,
                       self.consumerLevel,
                       self.bookingPlatform,
                       self.paymentMethod,
                       self.cafe]
            
            self.tmp.loc[self.nRows] = newData # loc starts counting at 0, i.e. nRows adds a new row
            
            return self.tmp
            
        elif profileID == 2:
            #print("ProfileID = " + str(profileID) + " is selected.")
            self.nRows = len(self.tmp.index)
            
            # specify the attributes
            self.guestID = self.nRows+1
            self.nights = 4
            self.breakfast = "extra"
            self.lunch = 0
            self.dinner = 2
            self.many = "single"
            self.scooter = 1
            self.yogaClass = 3
            self.yogaCourse = "no"
            self.consumerLevel = "medium"
            self.bookingPlatform = "airbnb"
            self.paymentMethod = "cash"
            self.cafe = 100000
            
            newData = [self.guestID,
                       profileID,
                       self.nights,
                       self.breakfast,
                       self.lunch,
                       self.dinner,
                       self.many,
                       self.scooter,
                       self.yogaClass,
                       self.yogaCourse,
                       self.consumerLevel,
                       self.bookingPlatform,
                       self.paymentMethod,
                       self.cafe]

            self.tmp.loc[self.nRows] = newData # loc starts counting at 0, i.e. nRows adds a new row
            
            return self.tmp

        else:
            print("The profile " + str(profileID) + " does not exist.")
        
        

