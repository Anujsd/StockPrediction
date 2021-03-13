from pymongo import MongoClient
import pandas as pd
from sys import exit
import matplotlib.pyplot as plt
import os

class Database:

    def __init__(self):
        self.username = 'DAV'
        self.password = 'DamanAnujVaibhav'
        self.db = 'MLpro'
        self.collection = 'stock_data'
        self.pdb = "prediction_data"


    def connect(self):
        """ A util for making a connection to mongo """


        URL = 'mongodb+srv://'+self.username +':'+  self.password + '@cluster0.eowpu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
              #'mongodb+srv://<username>:<password>@cluster0.eowpu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
        try:
            conn = MongoClient(URL)
        except:
            print('connection error !! ')
            exit(1)

        return conn

    def insert(self):
        """insert operation """
        conn = self.connect()
        DB = conn[self.db]

        collection = DB[self.collection]

        companies = ['tcs']
                        # 'Asian_paints',
                        # 'hindustan_unilever',
                        # 'bajaj_finance',
                        # 'hdfc_bank',
                        # 'reliance',
                        # 'hdfc',
                        # 'infosys',
                        # 'ITC',
                        # 'kotak_mahindra_bank']
        try:

            for company in companies:
                 data = pd.read_csv(company+'.csv')

                 data_dict = data.to_dict("records")
                 collection.insert_one({"index":company,"data":data_dict})

            print("data inserted !!")



        except Exception as e:

            print("Error while uploading the data to mongodb :")
            print(e)

            exit(1)



    def Get_Data(self,company_name):
        ''' fetch the data '''

        conn = self.connect()

        DB = conn[self.db]

        collection = DB[self.collection]

        data_from_db = collection.find_one({"index":company_name})

        df = pd.DataFrame(data_from_db["data"])


        return df


    def insert_predictions(self,company_name,data):

        conn = self.connect()

        DB = conn[self.pdb]

        collection = DB[self.collection]


        data_dict = data.to_dict("records")

        collection.insert_one({"index": company_name + "_prdictions","data":data_dict})

        print("prediction inserted for " + company_name )




    def Get_prediction_graph(self,company_name):
        conn = self.connect()
        DB = conn[self.pdb]
        collection = DB[self.collection]
        data_from_db = collection.find_one({"index":company_name + "_prdictions"})
        df = pd.DataFrame(data_from_db["data"])
        y = list(df.iloc[-1])
        return y[-1]

    