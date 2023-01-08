import os
import sys
import pandas as pd

class conversioni:


    def exportAX(df):
        #print(df)
        print("headers")
        #print(df.head())
        for index, row in df.iterrows():
            print(row["mineral"], row["Sample"] )
            print(row["SiO2"],row["TiO2"],row["Al2O3"],row["Cr2O3"],row["Fe2O3"],row["FeO"],row["MgO"],row["Na2O"],row["CaO"],row["K2O"])
            print("*")
        print("conversion to AX done")