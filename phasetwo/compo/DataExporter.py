import pandas as pd
from threading import Thread
import logging
# setting up loggers
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)


class DataExporter(Thread):

    def __init__(self, dataframe, group=None,
                 target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super().__init__()
        self.dataframe = dataframe

    def export_file(self, path_to_file, suffix='csv'):
        """this function export the dataframe to specified format """
        return self.dataframe.to_csv(path_to_file)

    def run(self):  # function to make the tthreads run simantaneously
        # attaching the loggers with each thread
        logging.debug('running with DataExporter %s and %s', self.args, self.kwargs)
