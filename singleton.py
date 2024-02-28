class Borg:
    
    """The Borg design pattern"""
    _shared_data = {}

    def __init__(self):
        self.__dict__ = self._shared_data #Make an attribute dictionary


class Singleton(Borg): 
    
    """The singleton class"""
    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_data.update(kwargs)

    def __str__(self):
        return str(self._shared_data) #Returns dictionary

x = Singleton(HTTP = "Hyper Text Transfer Protocol")

print(x)

y = Singleton(NFT = "Non-Fungible Token")

print(y)
