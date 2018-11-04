import logging
import Colorer
import CommonUtility as cu
class LiveDataFeed(object):
    """ A simple "live data feed" abstraction that allows a reader 
        to read the most recent data and find out whether it was 
        updated since the last read. 
        
        Interface to data writer:
        
        add_data(data):
            Add new data to the feed.
        
        Interface to reader:
        
        read_data():
            Returns the most recent data.
            
        has_new_data:
            A boolean attribute telling the reader whether the
            data was updated since the last read.    
    """
    logger = logging.getLogger(__name__)
    def __init__(self,log):
        self.cur_data = None
        self.has_new_data = False
        self.logger=log

    def add_data(self, data):
        self.cur_data = data
        self.has_new_data = True
        self.logger.info("add data value is {}".format(data))
    def read_data(self):
        self.has_new_data = False
        self.logger.info("read_data opeation performed")
        return self.cur_data


if __name__ == "__main__":
    pass

