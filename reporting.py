# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 19:47:44 2021

@author: Nils
"""

import pandas as pd
import numpy as np


def existingReport():
    pass

def newReport():
    pass

def activateReport(path_reports, documentID=None, action=None, style=None):
        
    # Purpose: Check if register of reportIDs exists. If not, create a new one.
    #          Keeps track of the generated reportIDs.
    # 1. Define file path and file name.
    # 2. Check if register file exists.
    # 3. If exists: open register file and retrieve the latest reportID
    #               Differentiate between styles: "new", "existing"
    # 4. If not: create a new register file "register.xlsx" and add new reportID
    #            depending on the style, i.e. "single..." -> "R..." , "multiple..." -> "M..."
    # 5. Save and close.
    # 6. Done  

    # Arguments: 
    #   path_Reports - a relative file path to the reportID register
    #   documentID - string, the ID of
    #                a) a finStatID to create a new report OR
    #                   a [list of finStatIDs] of which a report is generated
    #                   --> enter as ["F2021315001-1", ...]
    #                b) an existing report which is to be modified
    #   action - string, "new" or "existing"
    #            "new" -> create a new reportID, check reportID_register
    #            "existing" -> check if existing, if true: return reportID    
    #   style - string, "singelFinStat" or "multipleFinStat"
    #           "singleFinStat" -> report analyzes one finStat only
    #           "multipleFinStat" -> report analyzes multiple finStat
    # Variables:
    #   ... - ....
    # Output: the reportID (string object) that is used for the next report    

    # 1. Define file path and file name.      
    path = path_reports
    file = "reports_register.xlsx"
    
    # 2. Check if register file exists.    
    try:
        with open(path + file) as f:
            print("File exists.")
    except IOError:
        print("No file found.")
        # guestListID = "G2021042003"                   # for debugging
        # finStatID_proposal = "F2021042003"            # for debugging
        # talaID = "1"                                  # for debugging
        # 1. Decompose documentID -> improve idDecomposer()
        tmp_list = [[guestListID, finStatID_proposal, talaID]]
        tmp_columns = ["reportID_register","finStatID_register","talaID_register"]
        tmp_df = pd.DataFrame(data=tmp_list, dtype=str, columns=tmp_columns)
        tmp_df.to_excel(excel_writer=path + file, sheet_name="test")
                
        return guestListID, finStatID_proposal, talaID
    
    

    pass