class CLI_Audio_Exception(Exception):
    """Base class for exceptions in this program"""
    pass

class CLI_Audio_File_Exception(CLI_Audio_Exception):
    """Exception for when an audio file is not found"""
    pass

class CLI_Audio_Screen_Size_Exception(CLI_Audio_Exception):
    """Exception for when screen size is too small"""
    pass
