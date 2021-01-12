#Copied over my LinkedList from the DSA repo to use in this lab

class Node:
    def __init__(self,value,next=None):
        self.value = value 
        self.next = next

    def __str__(self):
        return f'{ self.value }'


class LinkedList:
    def __init__(self, head=None, values=None):
        self.head = head
        if values:
            for value in reversed(values):
                self.insert(value)

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def __str__(self):
        output = ""
        current = self.head
        while current:
            output += '{ ' + str(current) + ' } -> '
            current = current.next
        return output + 'NULL'
        


# .append(value) which adds a new node with the given value to the end of the list
    def append_at_the_end(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

# .insertBefore(value, newVal) which add a new node with the given newValue immediately before the first value node
    def insert_before(self, value, new_value):
        if not self.head:
            return
        if self.head.value == value:
            self.insert(new_value)
            return
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = Node(new_value, current.next)
                return
            current = current.next

# .insertAfter(value, newVal) which add a new node with the given newValue immediately after the first value node
    def insert_after(self, value, new_value):
        if not self.head:    
            return
        current = self.head
        while current:
            if current.value == value:
                current.next = Node(new_value, current.next)
                return
            current = current.next

    def kthFromEnd(self,k):
        count = -1
        current = self.head
        if current == None:
            return
        while current:
            count += 1
            current = current.next
        current = self.head
        while current:
            if count == k :
                return current.value
            count -= 1
            current = current.next
