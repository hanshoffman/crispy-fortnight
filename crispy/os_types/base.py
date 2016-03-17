from abc import ABCMeta, abstractmethod

class Base(object):
    '''Abstract class for the various OS types'''
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def enum_os(self): 
        pass
    
    @abstractmethod
    def enum_users(self):
        pass
    
    @abstractmethod
    def enum_applications(self):
        pass
    
    @abstractmethod
    def enum_drives(self):
        pass
        
    @abstractmethod
    def enum_printers(self):
        pass
    
    @abstractmethod
    def get_ssh_keys(self):
        pass
    
    @abstractmethod
    def enable_persistence(self):
        pass