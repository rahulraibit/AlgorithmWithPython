
class Binary:
    def __init__(self, value):
        self.left = None;
        self.right = None;
        self.data = value;

    def insert(self, data):
        if self.data:
            if self.data < data:
                if self.right is None:
                   self.right = Binary(data);
                else:
                    self.right.insert(data); 
            elif self.data > data:
                if self.left is None:
                    self.left = Binary(data);
                else:
                    self.left.insert(data);
        else: 
            self.data = data;

    def printData(self):
        if self.left:
            self.left.printData();
        print(self.data);
        if self.right:
            self.right.printData()

root = Binary(5);
root.insert(10);
root.insert(15);
root.insert(6);
root.insert(1);
root.insert(3);
root.insert(5);

root.printData();
    

