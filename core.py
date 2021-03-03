# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 18:30:43 2021

@author: Nils
"""


from talaObjects import Bungalows
from financialStatements import finStat
from guestLists import guestAttributes
from talaObjects import PrizeList

import pandas as pd
import numpy as np

def main():
    # Purpose: Create data frame for financial statements.
    #
    # 1. Define file paths.
    # 2. Choose and load guestList.
    # 3. Create empty financialStatement with attributes in header.
    # 4. Add financial statements by looping through guestList and simulating interactions.
    # 5. Save the financialStatements sheet to excel-file.
    # 6. Done.

    # Arguments: 
    #   profileID - integer, determines which guest profile to choose from        
    # Variables:
    #   self.tmp - an instance of the class, a pd data frame that grows every time that "addProfile()" is called
    # Output: the guest list "self.tmp" as pandas data frame which has the profile attached to the data frame
 
    

    
    # 1. Define file paths.
    path_finStat = ".\\financialStatements\\"
    path_guestList = ".\\guestLists\\"
    
    # 2. Choose and load guestList.
    guestListID = "2"
    tmp_guestList = pd.read_excel(path_guestList + guestListID + ".xlsx", index_col=0, header=0)
    #print(list(tmp_guestList.columns.values))                  # "tmp_guestList.columns.values" return an nd.ndarray 
       
    # 3. Create empty financialStatement with attributes in header 
    header = guestAttributes.attributes                         # "header" is a list object

    newFinStat = finStat(ID=3)
    newFinStat_df = newFinStat.create(header=header)            # creates an empty DataFrame with named header

    # 4. Add financial statements.
    # Loop over this sequence:
    #   4.1 Fetch guest.
    #   4.2 Fetch cost.
    #   4.3 Add statement.
    
    # 4.1 Fetch guest.
    #print(tmp_guestList.index.values)   
    tmp_guestInfo = tmp_guestList.loc[0]
    tmp_guestID = tmp_guestInfo[0]
    #print(tmp_guestInfo)
    #print(tmp_guestList.dtypes)
    
    # 4.2 Fetch cost.
    tmp_data = np.ndarray([1,4])                                # does not work, array is flattened
    tmp_data = np.array([[tmp_guestID],[1],[0],[100000]]).transpose()         # now array is ok
    newCosts = pd.DataFrame(data=tmp_data, columns=["GuestID","StatementID","Debit(-)", "Credit(+)"])    
    #print(newCosts.loc[0])
    #print(newCosts.dtypes)
    
    # 4.3 Merge data and add to financial statement.
    
    #print(tmp_guestList.columns.values)
    #print(newCosts.columns.values)
    result = newCosts.merge(right=tmp_guestList, how="inner", on="GuestID")
    #print(result)
    
    # print(newFinStat_df.shape)
    print(newFinStat_df.columns)
    # print(result.shape)
    print(result.columns)
    newFinStat_df = pd.concat([newFinStat_df, result], axis=0, ignore_index=True)       #pd.concat automatically matches the column labels
    newFinStat_df = pd.concat([newFinStat_df, result], axis=0, ignore_index=True)
    newFinStat_df = pd.concat([newFinStat_df, result], axis=0, ignore_index=True)
    newFinStat_df = pd.concat([newFinStat_df, result], axis=0, ignore_index=True)
    newFinStat_df = pd.concat([newFinStat_df, result], axis=0, ignore_index=True)

    # newFinStat_df = newFinStat_df.reset_index(inplace=False)
    # print(newFinStat_df.index)
    
    # newFinStat_df = newFinStat_df.merge(right=result, how="inner", on="GuestID")
    
    # 5. Save the financialStatements sheet to excel-file.
    newFinStat_df.to_excel(path_finStat + str(newFinStat.ID) + ".xlsx", sheet_name="test")
    result.to_excel(path_finStat + "333" + ".xlsx", sheet_name="test")
 
    # 6. Done

    
if __name__ == "__main__":
    main()