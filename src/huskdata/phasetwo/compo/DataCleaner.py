""" DataCleaner file import """
import pandas as pd
import numpy as np
import threading
import logging

# setting up loggers
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)
class DataCleaner(threading.Thread):
    """
    Data Cleaner class for data cleaning

    """
    def __init__(self,dataset_location,not_required_headers,group=None,
                 target=None, name=None,
                 args=(), kwargs=None, verbose=None ):
        super().__init__()# getting the methods for thread class
        self.args = args
        self.kwargs = kwargs
        self.dataset_location = dataset_location  # location of dataframe
        self.dataframe = pd.read_csv(self.dataset)  # creating the dataframe :
        self.not_required_headers = not_required_headers  # getting the list of non required fields

    def run(self):# function to make the tthreads run simantaneously
        # attaching th eloggers with each thread
        logging.debug('running with %s and %s', self.args, self.kwargs)
        return

    def remove_uneccessary_data(self):
        """ removing not required fields """
        self.dataframe.drop(self.not_required_headers,axis=1,inplace=True)

    def remove_na(self):
        """Removing the nan or na values from the dataframe"""
        self.dataframe.dropna(inplace=True)

    def remove_dupliactes(self):
        """Removing the duplicates from the dataframe"""
        self.dataframe.drop_duplicates(inplace=True)

    def converting_data_types(self):
        """function for correcting the data types """
        self.dataframe.apply(pd.to_numeric, errors='ignore', inplace=True)

    def fix_typos(self):
        """making for future purpose"""
        pass

    def normalization_df(self):
        """function to normalize the data"""
        pass

    def scaling_transformation(self):
        """function for normalizing the scaling """
        pass

    def return_dataframe(self):
        return self.dataframe

###############################################################################################
