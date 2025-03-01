class Index(list):

    def __init__(self, length: int|None = None) -> None:
        super().__init__(range(length) if length else [])
    
    def __getitem__(self, idx: int) -> int:
        if idx not in self:
            raise IndexError(idx)
        return self.index(idx)
    
    def __setitem__(self, idx, new_idx: int) -> None:
        if new_idx in self:
            return
        
        if idx != new_idx:
            raise IndexError(f'Index not matching {idx} != {new_idx}')
        
        self.append(new_idx)
