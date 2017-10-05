Coding Questions - Linked List
=========================================

Find the middle of a given linked list
----------------------------------------------

**Two Pointers**, this is a very useful trick to deal with linked list problems.

    #. Method 1:
        Traverse linked list using two pointers. Move one pointer by one and other pointer by two. 
        When the fast pointer reaches end slow pointer will reach middle of the linked list.
    #. Method 2:
        Initialize mid element as head and initialize a counter as 0. Traverse the list from head, while 
        traversing increment the counter and change mid to mid->next whenever the counter is odd. 
        So the mid will move only half of the total length of the list.