from collections.abc import MutableSequence

class MyList(MutableSequence):
    def __init__(self, initlist=None):
        super().__init__()
        if isinstance(initlist, list):
            self.data = initlist.copy()
        else:
            self.data = []
    
    def __getitem__(self, index):
        return self.data.__getitem__(index)
    
    def __setitem__(self, index, value) -> None:
        self.data.__setitem__(index, value)
    
    def __len__(self) -> int:
        return self.data.__len__()
    
    def __delitem__(self, index):
        self.data.__delitem__(index)
    
    def insert(self, index, value):
        self.data.insert(index, value)
