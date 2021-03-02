# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 19:03:13 2021

@author: Nils
"""

import pandas as pd

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