class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class Linked_list:
    def __init__(self):
        self.head = None

    def create_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked-list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

    def create_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.create_at_end(data)  # calling create_at_end method

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.create_at_beginning()
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return
        
        count = 0
        itr = self.head
        while itr:
            if itr.data == data_after:
                self.insert_at(count + 1, data_to_insert)
                break
            itr = itr.next
            count += 1

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if itr.data == data:
                self.remove_at(count)
            itr = itr.next
            count += 1


if __name__ == '__main__':
    ll = Linked_list()
    # ll.create_at_beginning(10)
    # ll.create_at_beginning(5)
    # ll.create_at_end(8)
    ll.insert_values(['gagan', 'chandan', 'family', 'amma', 'appa'])
    ll.print()

    print(ll.get_length())

    ll.remove_at(2)
    ll.print()

    ll.insert_at(1, 'we')
    ll.print()

    ll.insert_after_value('chandan', 'name')
    ll.print()

    ll.remove_by_value("we")
    ll.print()



