Design Questions
==========================

LeetCode 146. LRU Cache
----------------------------------

I have 2 solutions::

        class Node(object):
            def __init__(self, key, value):
                self.key = key
                self.value = value
                self.next = None
                self.prev = None

        class LRUCache(object):
            def __init__(self, capacity):
                """
                :type capacity: int
                """
                self.capacity = capacity
                self.data = dict()
                self.head = Node('dummy', 0)
                self.tail = Node('dummy', 0)
                self.head.next = self.tail
                self.tail.prev = self.head

            def get(self, key):
                """
                :type key: int
                :rtype: int
                """
                if key in self.data:
                    node = self.data[key]
                    self._tweak(node)
                    return self.head.next.value
                else:
                    return -1

            def put(self, key, value):
                """
                :type key: int
                :type value: int
                :rtype: void
                """
                if key in self.data:
                    node = self.data[key]
                    node.value = value
                    self._tweak(node)
                else:
                    node = Node(key, value)
                    self.data[key] = node
                    self._add(node)

                if len(self.data) > self.capacity:
                    leastNode = self.tail.prev
                    del self.data[leastNode.key]
                    self._remove(leastNode)

            def _add(self, node):
                # always move current node to the head
                headNext = self.head.next
                self.head.next = node
                headNext.prev = node
                node.next = headNext
                node.prev = self.head


            def _remove(self, node):
                # delete last element of the list
                prevNode = node.prev
                prevNode.next = self.tail
                self.tail.prev = prevNode
                node.prev = None
                node.next = None

            def _tweak(self, node):
                # always move current node to the head
                nextNode = node.next
                prevNode = node.prev
                headNext = self.head.next
                if node != headNext:
                    self.head.next = node
                    node.prev = self.head
                    node.next = headNext
                    headNext.prev = node

                    prevNode.next = nextNode
                    nextNode.prev = prevNode

        class LRUCache(object):

            def __init__(self, capacity):
                """
                :type capacity: int
                """
                self.stamp = 0
                self.size = capacity
                self.data = {}
                

            def get(self, key):
                """
                :type key: int
                :rtype: int
                """
                if key in self.data:
                    self.stamp += 1
                    self.data[key]['time'] = self.stamp
                    return self.data[key]['value']
                else:
                    return -1
                

            def put(self, key, value):
                """
                :type key: int
                :type value: int
                :rtype: void
                """
                self.stamp += 1
                if len(self.data) < self.size or key in self.data:
                    self.data[key] = {
                        'value':    value,
                        'time':     self.stamp
                    }
                else:
                    recent = self.stamp
                    for _key in self.data.keys():
                        if self.data[_key]['time'] < recent:
                            recentkey = _key
                            recent = self.data[_key]['time']
                    del self.data[recentkey]
                    self.put(key, value)
