from crispy.os_types.base import Base

class Debian(Base):
    '''Ubuntu'''

    def enum_os(self):
        return Base.enum_os(self)


    def enum_users(self):
        return Base.enum_users(self)


    def enum_applications(self):
        return Base.enum_applications(self)


    def enum_drives(self):
        return Base.enum_drives(self)


    def enum_printers(self):
        return Base.enum_printers(self)


    def get_ssh_keys(self):
        return Base.get_ssh_keys(self)