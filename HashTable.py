#Referenced from WGU C950 supplemental resources, C950 - Webinar-1 - Let’s Go Hashing
class hashtable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, size=40):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(size):
            self.table.append([])
    
    #Insert the key-item if it doesn't exist already, updates if it does.
    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        #Updates if already exists
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
            return True
        
        #Inserts if new
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    #Takes in key (package ID for this project) and searches the buckets for the matching
    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        #Searches for the key-value item
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
        return None
    
    #Removes the key-item from the hash table bucket
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0],kv[1]])