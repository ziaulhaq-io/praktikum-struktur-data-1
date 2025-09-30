class Stack:
    def __init__(self):
        self.data = list()

    def isEmpty(self):
        return len(self.data) == 0

    def __len__(self):
        return len(self.data)

    def peek(self):
        if self.isEmpty():
            raise Exception('Stack kosong. Tidak ada data top.')
        else:
            return self.data[-1]

    def pop(self):
        if self.isEmpty():
            raise Exception('Stack kosong. Tidak ada data yang dapat di-pop.')
        else:
            return self.data.pop()

    def push(self, data):
        self.data.append(data)

    def printData(self):
        for item in self.data:
            print(item)

    def deleteAll(self):
        for item in self.data:
            self.data.pop() 
          
myStack = Stack()
myStack.push(10)
myStack.push(21)
myStack.push(32)

print(f'Total Data = {myStack.__len__()}');
print(f'Elemen TOP = {myStack.peek()}')

print() 
print('Data dalam Stack : ')
myStack.printData()

print() 
print('Hapus Data')
myStack.pop()

print('Data dalam Stack : ')
myStack.printData()

print('Hapus Seluruh Data')
myStack.deleteAll()

if myStack.isEmpty():
    print('Stack Kosong')
else:
    print('Data dalam Stack : ')
    myStack.printData()