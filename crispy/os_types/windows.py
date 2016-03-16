sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))

from crispy.os_types.base import Base

class Windows(Base):

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