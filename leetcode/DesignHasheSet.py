class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashset = [[] for _ in range(1000)];
        

    def add(self, key: int) -> None:
        if not self.contains(key):
            subkey = key%1000;
            self.hashset[subkey].append(key);

    def remove(self, key: int) -> None:
        if self.contains(key):
            subkey = key %1000;
            self.hashset[subkey].remove(key);

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        subkey = key %1000;
        return key in self.hashset[subkey];
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


#class MyHashSet:

#    def __init__(self):
#        """
#        Initialize your data structure here.
#        """
#        self.hashset = [None]*100000;
        

#    def add(self, key: int) -> None:
#            self.hashset[key] = True;

#    def remove(self, key: int) -> None:
#        self.hashset[key] = None;

#    def contains(self, key: int) -> bool:
#        """
#        Returns true if this set contains the specified element
#        """
#        return self.hashset[key];
        


## Your MyHashSet object will be instantiated and called as such:
## obj = MyHashSet()
## obj.add(key)
## obj.remove(key)
## param_3 = obj.contains(key)