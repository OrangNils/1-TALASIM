# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 23:15:49 2021

@author: Nils
"""

import numpy as np
import pandas as pd

def datePrefixISO(date):
    # Return the datePrefix in the format 2021133, i.e. YYYY CW WD
    full = date
    YYYY = str(full.isocalendar()[0])
    CW = full.isocalendar()[1]
    if CW < 10:
        CW = "0" + str(CW)
    else:
        CW = str(CW)
    WD = str(full.isocalendar()[2])    
    datePrefix = YYYY + CW + WD
    return datePrefix

def idComposer(indicator, prefix, suffix):
    
    genericID = indicator + prefix + suffix
    return genericID

def idDecomposer(genericID):
    
    indicator = genericID[0]
    prefix = genericID[1:8]
    suffix = genericID[8::]
    
    return (indicator, prefix, suffix)


def suffixFormat(n_integer):
    # Purpose: make integer like 1 to string like "001"
    if (n_integer < 10):
        n_string = "00" + str(n_integer)
    elif (n_integer >= 10) and (n_integer < 100):
        n_string = "0" + str(n_integer)
    elif (n_integer >= 100):
        n_string = str(n_integer)
    return n_string

def nextguestListID(inputID, proposedID):
    # Compares inputID with propsedID.
    # Returns the one that is correct.
    
    indicator_input, prefix_input, suffix_input = idDecomposer(inputID)
    indicator_proposed, prefix_proposed, suffix_proposed = idDecomposer(proposedID)
    
    # Increase the suffix by 1, if the prefix is the same.
    if prefix_input == prefix_proposed:
        prefix_correct = prefix_proposed
        suffix_correct = np.int(suffix_input) + 1
        suffix_correct = suffixFormat(suffix_correct)

        correctID = idComposer(indicator_input, prefix_correct, suffix_correct)
    
    # Start a new count for today, i.e. prefix_proposed + proposedSuffix
    else:
        correctID = idComposer(indicator_proposed, prefix_proposed, suffix_proposed)
    
    return correctID
