# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 18:30:43 2021

@author: Nils
"""


from talaObjects import Bungalows
from financialStatements import finStat
from financialStatements import nextFinStatID
from financialStatements import finStatTemplate
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
    
    # 2. Choose and load guestList and talaConfiguration.
    guestListID = "2" #G2021092002"
    talaID = "1"
    tmp_guestList = pd.read_excel(path_guestList + guestListID + ".xlsx", index_col=0, header=0)
    #print(list(tmp_guestList.columns.values))                        # "tmp_guestList.columns.values" return an nd.ndarray 
    
    
    
    # 3. Create empty financialStatement with guest attributes in header 
    newFinStatID = nextFinStatID(path_finStatID=path_finStat,
                                 guestListID=guestListID,
                                 talaID=talaID,
                                 default="2")                         # returns the corresponding finStatID and saves the finStatID in excel-file
    headerGuests = guestAttributes.attributes                         # "header" is a list object
    newFinStat = finStat(ID=newFinStatID)
    newFinStat_df = newFinStat.create(header=headerGuests)            # creates an empty DataFrame with named header, i.e. the guest attributes

    # 4. Add financial statements.
    # Loop over this sequence:
    #   4.1 Fetch guest.
    #   4.2 Fetch cost.
    #   4.3 Add statement.
    
    headerFinStat = ["talaObjects", "GuestID", "StatementID", "Debit(-)", "Credit(+)"]
    #df_finStat = finStatTemplate(headerFinStat)                        # problem: output is not of "pandas.DataFrame" class type
    df_finStat = pd.DataFrame(data=None, columns=headerFinStat)
    #print(type(df_finStat))
    
    # 4.1 Fetch guest.
    #     Guest attributes are fed to the talaObjects.  
    for element in tmp_guestList.index:
        tmp_guestAttributes = tmp_guestList.iloc[element]              # pd.Series object
        tmp_guestID = tmp_guestAttributes["GuestID"]                   # np.int64 object
              
    
        # 4.2 Fetch cost.
        #     Each cost is represented by a row in the finStat
        #     Take the guestAttributes (one-guest-at-a-time) and feed those into the talaObjects.
        #     Fill the DataFrame with the financial statements.
        
        
        # Take the guestAttributes (one-guest-at-a-time) and feed those into the talaObjects.
        tmp_class = Bungalows(tmp_guestID, tmp_guestAttributes, headerFinStat, df_finStat)
        # Fill the DataFrame with the financial statements.
        df_finStat = tmp_class.revenue_perGuest()
        df_finStat = tmp_class.cost_perGuest()
        
        
        # 4.3 Bundle data of each guest and merge with financial statement.
        # -> Moved outside of the loop. Loop over all guests first
        # After that use LEFT JOIN like merging of the data frames "df_finStat" and "tmp_guestList".
        
        
        #print(tmp_guestList.columns.values)
        #print(newCosts.columns.values)
        # result = newCosts.merge(right=tmp_guestList, how="inner", on="GuestID")
        #print(result)
        
        # print(newFinStat_df.shape)
        # print(newFinStat_df.columns)
        # print(result.shape)
        # print(result.columns)
        # newFinStat_df = pd.concat([newFinStat_df, result], axis=0, ignore_index=True)       #pd.concat automatically matches the column labels
        # newFinStat_df = pd.concat([newFinStat_df, result], axis=0, ignore_index=True)
        # newFinStat_df = pd.concat([newFinStat_df, result], axis=0, ignore_index=True)
        # newFinStat_df = pd.concat([newFinStat_df, result], axis=0, ignore_index=True)
        # newFinStat_df = pd.concat([newFinStat_df, result], axis=0, ignore_index=True)
    
        # newFinStat_df = newFinStat_df.reset_index(inplace=False)
        # print(newFinStat_df.index)
        
        # newFinStat_df = newFinStat_df.merge(right=result, how="inner", on="GuestID")
    
 
    df_finStat = df_finStat.astype({"GuestID": "int64"})                                    # problem: necessary to match data types
    new = df_finStat.merge(right=tmp_guestList, how="left", on="GuestID", indicator=True)
    
    # 5. Save the financialStatements sheet to excel-file.
    new.to_excel(path_finStat + str(newFinStatID) + "-" + talaID + ".xlsx", sheet_name="test")
    # result.to_excel(path_finStat + "333" + ".xlsx", sheet_name="test")
 
    # 6. Done

    
if __name__ == "__main__":
    main()