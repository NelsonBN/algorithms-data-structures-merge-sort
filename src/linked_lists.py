class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()


    def merge_sort(self):
        self.head = self.__merge_sort(self.head)

    def __merge_sort(self, head): # O(n log n)
        if not head or not head.next:
            return head

        middle = self.__get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self.__merge_sort(head)
        right = self.__merge_sort(next_to_middle)

        return self.__sorted_merge(left, right)

    def __get_middle(self, head): # O(n)
        if not head:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def __sorted_merge(self, left, right): # O(n)
        if not left:
            return right
        if not right:
            return left

        if left.value <= right.value:
            result = left
            result.next = self.__sorted_merge(left.next, right)
        else:
            result = right
            result.next = self.__sorted_merge(left, right.next)
        return result



list = LinkedList()
list.append(38)
list.append(27)
list.append(43)
list.append(3)
list.append(9)
list.append(82)
list.append(10)

print("Before:")
list.print_list()

list.merge_sort()

print("After:")
list.print_list()
