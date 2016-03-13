from abc import ABCMeta, abstractmethod

class Base:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def enum_os(self): 
        pass
    
    def upload(self, socket):
        pass
    
    def download(self, socket):
        pass
    
    #maybe include upload/download since it's os independent
    ##http://www.bogotobogo.com/python/python_network_programming_server_client_file_transfer.php
