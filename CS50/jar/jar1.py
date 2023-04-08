class Jar:
    def __init__(self, capacity=12):
        if capacity > 0:
            self._capacity = capacity
            self._size = 1
        else:
            raise ValueError

    def __str__(self):
        return '🍪' * self._size

    def deposit(self, n):
        if (self._size + n) <= self._capacity:
            self._size += n
            return self._size
        else:
            raise ValueError

    def withdraw(self, n):
        if self._size >= n:
            self._size -= n
            return self._size
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar()
    print(str(jar.capacity))
    print(str(jar))
    jar.deposit(3)
    print(str(jar))
    jar.withdraw(1)
    print(str(jar))
    jar.deposit(4)
    print(str(jar))
    jar.withdraw(2)
    print(str(jar))

main()

