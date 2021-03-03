# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 19:03:13 2021

@author: Nils
"""

import pandas as pd
import numpy as np

from tools import datePrefixISO
from tools import nextguestListID
from tools import idComposer
from tools import idDecomposer
from tools import suffixFormat

class finStat:
     
    def __init__(self,ID):
        #self.main_dataframe = pd.DataFrame(data=None, columns='a')
        self.ID = ID
    
    def create(self, header):
        # Purpose: Create data frame for financial statements.
        # Arguments: 
        #   header - list object        
        # Variables:
        #   tmp - a temporary object, pandas data frame
        # Output: empty pandas data frame with named columns
        
            
        # Code
        print('The create method is active. It returns a pandas DataFrame')
        header = ["StatementID","Debit(-)", "Credit(+)"] + header
        self.tmp = pd.DataFrame(data=None, columns=header)
        return self.tmp
    
def nextFinStatID(path_finStatID, guestListID, talaID="1", default=None):
    # Purpose: Check if register of finStatIDs exists. If not, create a new one.
    #          Keeps track of the generated finStatListIDs and associate them with the talaID.
    #          Information is stored in pandas DataFrame.
    # 1. Define file path and file name.
    # 2. Take guestListID and derive finStatID.
    # 3. Check if register file exists.
    # 4. If exists: open register file and retrieve the latest guestListID
    #               search for a match of guestListID & finStatID & talaID
    #    If not: create a new register file "register.xlsx" and add new combination
    #            of guestListID & finStatID & talaID
    # 5. Save and close.
    # 6. Done  

    # Arguments: 
    #   path_finStatID - a relative file path to the finStatID register
    #   guestListID - the ID of the guestList that is used for the simulation
    #   talaID - the ID of the simulation, e.g. another combination of prizes yields
    #            a different finStat while using the same guestList
    #   default - a switch to debug/develop the function, string value     
    # Variables:
    #   ... - ....
    # Output: the finStatID (string object) that is used for the next simulation
    #         format if finStatID: finStatID-talaID    
    
    # Debug/Developer mode
    if default != None:
        return default                                  # A return statement ends the execution of the function call.
    else:
        pass

    # 1. Define file path and file name.        
    path = path_finStatID
    file = "finStatID_register.xlsx"

    # 2. Take guestListID and derive finStatID.   
    _,b,_ = idDecomposer(guestListID)
    finStatID_proposal = idComposer("F", b, "001")

    # 3. Check if register file exists.
    # 4. If exists: open register file and retrieve the latest guestListID
    #               search for a match of guestListID & finStatID & talaID
    #    If not: create a new register file "register.xlsx" and add new combination
    #            of guestListID & finStatID & talaID
    # 5. Save and close.
    # 6. Return finStatID
    try:
        with open(path + file) as f:
            print("File exists.")
        # 4. If exists: open register file and retrieve the latest guestListID
        #               search for a match of guestListID & finStatID & talaID
        tmp_columns = ["guestListID_register","finStatID_register","talaID_register"]       # read the excel file with values as string
        tmp_type = [str, str, str]                                                          # ...
        tmp_zip = zip(tmp_columns, tmp_type)                                                # ...
        tmp_dict = dict(tmp_zip)                                                            # ...
        
        existingIDs = pd.read_excel(path + file, index_col=0, header=0, dtype=tmp_dict)
        print(existingIDs)
        print(finStatID_proposal)
        
        # Create dataframe with of the proposed ID
        tmp_list = [[guestListID, finStatID_proposal, talaID]]
        tmp_columns = ["guestListID_register","finStatID_register","talaID_register"]
        tmp_df = pd.DataFrame(data=tmp_list, dtype=str, columns=tmp_columns)        
        
        # Check if combination of guestListID & finStatID & talaID exists in the file of "existingIDs"       
        # If match: update the finStatID until it is next in line and add combination
        tmp_df_merged = tmp_df.merge(existingIDs).drop_duplicates()
        tmp_df_noDuplicates = tmp_df.drop_duplicates()
        if len(tmp_df_merged) == len(tmp_df_noDuplicates):
            print("The proposed combination of IDs is already in the list.")
            
            while len(tmp_df_merged) == len(tmp_df_noDuplicates):                       # As long as the proposal is already existing,...
                a_proposal, b_proposal, c_proposal = idDecomposer(finStatID_proposal)   # ...fetch indicator, prefix, suffix from proposal
                c_proposal = np.int(c_proposal) + 1                                     # ...increase integer value
                c_proposal = suffixFormat(c_proposal)                                   # ...convert to string value in "001"
                finStatID_proposal = idComposer(a_proposal, b_proposal, c_proposal)     # ...make new proposal                                    

                # Re-create dataframe with of the updated-proposed ID
                tmp_list = [[guestListID, finStatID_proposal, talaID]]
                tmp_columns = ["guestListID_register","finStatID_register","talaID_register"]
                tmp_df = pd.DataFrame(data=tmp_list, dtype=str, columns=tmp_columns)

                tmp_df_merged = tmp_df.merge(existingIDs).drop_duplicates()
                tmp_df_noDuplicates = tmp_df.drop_duplicates()
                
                print(finStatID_proposal)
                                   
            existingIDs = pd.concat([existingIDs, tmp_df], axis=0, ignore_index=True)
            print(existingIDs)
            existingIDs.to_excel(excel_writer=path + file, sheet_name="test")
            
        # If no match: add new combination
        # 5. Save and close.
        else:
            # print("The proposed combination is new.")
            existingIDs = pd.concat([existingIDs, tmp_df], axis=0, ignore_index=True)
            print(existingIDs)
            existingIDs.to_excel(excel_writer=path + file, sheet_name="test")
        
        # 6. Return finStatID
        return guestListID, finStatID_proposal, talaID
    
    # 4. If not: create a new register file "register.xlsx" and add new combination
    #            of guestListID & finStatID & talaID
    # 5. Save and close.
    # 6. Return finStatID
    except IOError:
        print("No file found.")
        # guestListID = "G2021042003"                   # for debugging
        # finStatID_proposal = "F2021042003"            # for debugging
        # talaID = "1"                                  # for debugging
        tmp_list = [[guestListID, finStatID_proposal, talaID]]
        tmp_columns = ["guestListID_register","finStatID_register","talaID_register"]
        tmp_df = pd.DataFrame(data=tmp_list, dtype=str, columns=tmp_columns)
        tmp_df.to_excel(excel_writer=path + file, sheet_name="test")
                
        return guestListID, finStatID_proposal, talaID
    
    # 7. Done.    