import Queue
import threading
import time

import serial
import logging
import Colorer
import CommonUtility as cu

class ComMonitorThread(threading.Thread):
    """ A thread for monitoring a COM port. The COM port is 
        opened when the thread is started.
    
        data_q:
            Queue for received data. Items in the queue are
            (data, timestamp) pairs, where data is a binary 
            string representing the received data, and timestamp
            is the time elapsed from the thread's start (in 
            seconds).
        
        error_q:
            Queue for error messages. In particular, if the 
            serial port fails to open for some reason, an error
            is placed into this queue.
        
        port:
            The COM port to open. Must be recognized by the 
            system.
        
        port_baud/stopbits/parity: 
            Serial communication parameters
        
        port_timeout:
            The timeout used for reading the COM port. If this
            value is low, the thread will return data in finer
            grained chunks, with more accurate timestamps, but
            it will also consume more CPU.
    """    

    logger = logging.getLogger(__name__)
    def __init__(self,
        log,
        data_q,
        error_q, 
        port_num,
        port_baud,
        port_stopbits=serial.STOPBITS_ONE,
        port_parity=serial.PARITY_NONE,
        port_timeout=0.01):
        threading.Thread.__init__(self)
        '''Now, our ComMonitorThread class is a child class of the Thread class. 
        We then define a run method in our class. 
        This function will be executed when we call the start method of any object in our ComMonitorThread class.'''
                
        # cu.init_logging_commands(logger)
        self.logger=log
        
        self.serial_port = None
        try:
            self.serial_arg = dict( port=port_num,
                                    baudrate=port_baud,
                                    stopbits=port_stopbits,
                                    parity=port_parity,
                                    timeout=port_timeout)

            self.data_q = data_q
            self.error_q = error_q
            
            self.alive = threading.Event()
            self.alive.set()
            self.logger.info("ComMonitorThread intitalised")
        except Exception as e:
            self.logger.error(str(e))
        '''
        set()
        Set the internal flag to true. All threads waiting for it to become true are awakened. 
        Threads that call wait() once the flag is true will not block at all.
        '''
        
    def run(self):
        try:
            if self.serial_port: 
                self.serial_port.close()
            self.serial_port = serial.Serial(**self.serial_arg)
            self.logger.critical("Run command started")
        except serial.SerialException, e:
            # self.error_q.put(e.message)
            self.logger.error(str(e))
            return
        
        # Restart the clock
        time.clock()
        
        while self.alive.isSet():
            # Reading 1 byte, followed by whatever is left in the
            # read buffer, as suggested by the developer of 
            # PySerial.
            # 
            data = self.serial_port.read(1)
            self.logger.info("rx data is => {}".format(data))
            data += self.serial_port.read(self.serial_port.inWaiting())
            
            if len(data) > 0:
                timestamp = time.clock()
                self.data_q.put((data, timestamp))
                self.logger.info("rx data_q is => {}".format(data))
            
        # clean up
        if self.serial_port:
            self.serial_port.close()

    def join(self, timeout=None):
        self.alive.clear()
        threading.Thread.join(self, timeout)

