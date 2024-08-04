class ListNode:
  def __init__(self, data, next=None):
    self.data, self.next = data, next


class LinkedList:
  def __init__(self):
    self.head = self.tail = None
    self.length = 0

  def __str__(self):
    if self.is_empty():
        return ""
    else:
        list_string = "Head"
        current_node = self.head

        for _ in range(self.length):
            list_string = f"{list_string} -> {current_node.data}"
            current_node = current_node.next

        return f"{list_string} -> None"


  def is_empty(self):
    return self.length == 0


  def insert_first(self, data):
    new_node = ListNode(data, self.head)
    self.head = new_node
    self.length += 1

    if not self.tail:
      self.tail = new_node


  def insert_last(self, data):
    new_node = ListNode(data)

    if self.is_empty():
      self.head = self.tail =  new_node
      self.length += 1
    else:
      self.tail.next = new_node
      self.tail = new_node
      self.length += 1


  def build_from(self, array):
    for item in array:
      self.insert_last(item)


  def delete_first(self):
    deleted_item = None

    if not self.is_empty():
      deleted_item = self.head.data

      if self.head == self.tail:
        self.head = self.tail = None
      else:
        self.head = self.head.next
      self.length -= 1
    
    return deleted_item


  def delete_last(self):
    deleted_item = None

    if not self.is_empty():
        if self.head == self.tail: 
            deleted_item = self.head.data
            self.head = self.tail = None
        else:
            current_node = self.head
            for _ in range(self.length - 2):
                current_node = current_node.next
            deleted_item = current_node.next.data
            self.tail = current_node
            current_node.next = None
        self.length -= 1

    return deleted_item


  def get_at(self, idx):
    if self.is_empty() or idx < 0 or idx >= self.length:
      return None

    if idx == 0:
      return self.head.data

    if idx == self.length - 1:
      return self.tail.data

    current_node = self.head
    for _ in range(idx):
      current_node = current_node.next 

    return current_node.data


  def set_at(self, idx, data):
    if self.is_empty() or idx < 0 or idx >= self.length:
      return None

    if idx == 0:
      self.head.data = data
      return

    if idx == self.length - 1:
      self.tail.data = data
      return

    current_node = self.head
    for _ in range(idx):
      current_node = current_node.next

    current_node.data = data


  def insert_at(self, idx, data):
    if idx < 0 or idx > self.length:
      return None

    if idx == 0:
      self.insert_first(data)
      return

    if idx == self.length:
      self.insert_last(data)
      return

    current_node = self.head
    for _ in range(idx - 1):
      current_node = current_node.next

    new_node = ListNode(data, current_node.next)
    current_node.next = new_node
    self.length += 1

  
  def delete_at(self, idx):
    if idx < 0 or idx >= self.length:
      return None

    if idx == 0:
      return self.delete_first()

    if idx == self.length - 1:
      return self.delete_last()

    current_node = self.head
    for _ in range(idx - 1):
      current_node = current_node.next

    deleted_item = current_node.next.data
    current_node.next = current_node.next.next
    self.length -= 1

    return deleted_item