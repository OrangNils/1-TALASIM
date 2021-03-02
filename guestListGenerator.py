# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 21:12:29 2021

@author: Nils
"""

from talaObjects import Bungalows
from financialStatements import finStat
from guestLists import guestList
from guestLists import guestListID
import pandas as pd

def main():
    
    # 1. Define file path.
    # 2. Define guestListID.
    # 3. Create empty guestList with attributes in header.
    # 4. Loop through combination of profiles.
    # 5. Save guestList to excel-file.
    # 6. Done.
    
    # 1. Define file path.
    path_guestList = ".\\guestLists\\"
 
    # 2. Define guestListID
    tmp_guestListID = guestListID(path_guestListID=path_guestList)
    print(tmp_guestListID)
    
    # 3. Create empty guestList with attributes in header.
    # Create new guestList sheet - option 2 all-in-one
    new = guestList(10)
    new.tmp.to_excel(path_guestList + str(guestList(1).ID) + ".xlsx", sheet_name="test")
    
    # 4. Loop through combination of profiles.
    # test
    new2 = guestList(100)
    
    for i in range(10):
        
        guestListDummy = new2.addProfile(1)
        guestListDummy = new2.addProfile(2)
    
    # 5. Save guestList to excel-file.
    guestListDummy.to_excel(path_guestList + str(guestList(100).ID) + ".xlsx", sheet_name="test")
    
    # 6. Done.
     
if __name__ == "__main__":
    main()