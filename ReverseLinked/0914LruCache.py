from collections import OrderedDict




class LRUCache:
    def __init___(self, capacity: int):
        self.cache = OrderedDict();
        self.capacity = capacity;
        

    def get(self, key: int) -> int:
        if key not in self.cache :
            return -1;
        self.cache(key);
        return self.cache(key)

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache[key] = value;
            if len(self.cache) > self.capacity:
                self.cache.popitem(last= True);

class Node :
    def __init__(self, key, val, prev = None, next = None):
        self.key, self.val = key,val;
        self.prev, self.next = prev, next;

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {};
        self.capacity = capacity;

    def get(self, key: int) -> int:
        if key not in self.cache:
            -1;
        self.cache.remove(key);
        self.cache.insert(key);

    def put(self, key: int, value int) -> None:
        if key not in self.cache:
            self.cache.insert(key);
        self.cache[key] = value;
        if len(self.cache) > self.capacity :
            LRU  = self.left.next;
            self.cache.remove(LRU);
            self.




    def remove(self, node):
        prev, nxt  = node.prev, node.next;
        prev.next, next.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right;
        prev = nxt = node ;
        node.prev, node.next = prev, nxt ;




        """
        We have to maintain insertion order. So some sort of linked list is important
        """