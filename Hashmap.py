class Hashmap:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]
        self.size = 0
        self.load_factor = 0.75

    def _bucket_index(self, key):
        hash_no = hash(key)
        return hash_no % self.capacity

    def put(self, key, value):
        index = self._bucket_index(key)
        bucket = self.buckets[index]

        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

        # When load-factor exceeds, capacity is made double to solve performance issue.
        if self.size / self.capacity > self.load_factor:
            self.capacity *= 2
            old_buckets = self.buckets
            self.buckets = [[] for _ in range(self.capacity)]

            # Re-inserting all elements
            for bucket in old_buckets:
                for key, value in bucket:
                    self.put(key, value)

    def disp(self):
        print(f"Hashmap:{self.buckets} ")

    def get(self, key):
        index = self._bucket_index(key)
        bucket = self.buckets[index]

        for _key, value in bucket:
            if _key == key:
                return value
        return None

    def remove(self, key):
        index = self._bucket_index(key)
        bucket = self.buckets[index]

        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(i)
                self.size -= 1
                return True
        return False

    def contains_key(self, key):
        return self.get(key) is not None

    def items(self):
        all_items = []

        for bucket in self.buckets:

            for pair in bucket:
                all_items.append(pair)

        return all_items


if __name__ == "__main__":
    h = Hashmap(8)

    h.put("Bangladesh", "Dhaka")
    h.put("Bindia", "Dehli")
    h.put("China", "Beijing")
    h.put("USA", "Washington-DC")
    h.put("Saudi", "Riad")
    print(h.get("Bangladesh"))
    h.disp()
