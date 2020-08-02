
class Node:
    def __init__(self, data):
         self.left = None;
         self.right = None;
         self.data = data;

def SortedArrayToBst(arr):
           if not arr:
               return None;
           mid = int(len(arr) / 2);
           print(mid);
           root = Node(arr[mid]);
           root.left =  SortedArrayToBst(arr[:mid]);
           root.right = SortedArrayToBst(arr[mid+1:]);
           return root;

def preOrder(node): 
    if not node: 
        return
      
    print(node.data), 
    preOrder(node.left) 
    preOrder(node.right) 


         
arr = [1, 2, 3, 4, 5, 6, 7] 
root = SortedArrayToBst(arr) 
preOrder(root) 

#1) Get the Middle of the array and make it root.
#2) Recursively do same for left half and right half.
#      a) Get the middle of left half and make it left child of the root
#          created in step 1.
#      b) Get the middle of right half and make it right child of the
#          root created in step 1.


