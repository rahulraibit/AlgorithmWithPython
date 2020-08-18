class CombinationIterator:
    def genrators(self, s, startingindex, stringsofar, k):
        if k == 0:
            self.iterators.append(stringsofar);
            return
        for i in range(startingindex, len(s)):
            self.genrators(s, i + 1, stringsofar + s[i], k-1)

    def __init__(self, characters: str, combinationLength: int):
        self.iterators = [];
        self.genrators(characters, 0, "", combinationLength);
        

    def next(self) -> str:
        if self.hasNext:
            return self.iterators.pop(0);
        

    def hasNext(self) -> bool:
        if len(self.iterators) > 0:
            return True;
        return False;

cmb = CombinationIterator("abc", 2);
print(cmb.next())