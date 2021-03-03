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
    tmp_guestListID = guestListID(path_guestListID=path_guestList, default="2")
    print("This is the guestListID that is returned by the function guestListID(): " + str(tmp_guestListID))
    
    # 3. Create empty guestList with attributes in header.
    new = guestList(tmp_guestListID)                     # attributes are automaticall taken from the class "guestAttributes"
    # new = guestList(1)                                   # if                 
    # new.tmp.to_excel(path_guestList + str(new.ID) + ".xlsx", sheet_name="test")
    
    # 4. Loop through combination of profiles.
    # test
    # new2 = guestList(100)
    
    for i in range(10):
        
        guestListDummy = new.addProfile(1)              # The method "addProfile()" returns the modified guest list. The guest list is an instance variable of the class, i.e. the guest list is contained in the class instance and is directly accessible for future modifications.
        guestListDummy = new.addProfile(2)
    
    # 5. Save guestList to excel-file.
    guestListDummy.to_excel(path_guestList + str(new.ID) + ".xlsx", sheet_name="test")
    
    # 6. Done.
     
if __name__ == "__main__":
    main()