class TrieNode:
    def __init__(self):
        self.child = [None]*26;
        self.isWordEnd = False;

class Trie:
    def __init__(self):
        self.root = TrieNode();

    def charToIndex(self, c):
        return ord(c) - ord('a');

    def insert(self, word):
        wlength = len(word);
        temp = self.root;
        for i in range(wlength):
            index = self.charToIndex(word[i]);
            if not temp.child[index]:
                temp.child[index] = TrieNode();
            temp = temp.child[index];
        temp.isWordEnd = True;

    def searchUtil(self, key, node):
        temp = node;
        wlength= len(key);
        for i in range(wlength):
            if not key[i] == '.':
                index = self.charToIndex(key[i]);
                if not temp.child[index]:
                    return False;
                temp = temp.child[index];
            else:
                for ch in temp.child:
                    if ch is not None and self.searchUtil(key[i+1:], ch):
                        return True;
                return False;
        return temp is not None and temp.isWordEnd;
    def search(self, key):
        if key is None:
            return False;
        return self.searchUtil(key, self.root)

trie = Trie();
trie.insert("abc")
print(trie.search("a.."))
