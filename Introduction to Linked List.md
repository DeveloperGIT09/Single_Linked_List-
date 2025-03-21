# Introduction to Linked List

## 1. What is a Linked List?
A linked list is a data structure used to store a collection of elements (nodes) in memory. Unlike arrays, linked lists do not require contiguous memory allocation.

## 2. Ways to Maintain a List in Memory
There are two main data structures to maintain a list in memory:
1. **Array**
2. **Linked List**

Arrays have limitations, and linked lists help overcome these limitations.

## 3. Types of Linked Lists
1. **Singly Linked List**: Navigation is forward only.
2. **Doubly Linked List**: Navigation is both forward and backward.
3. **Circular Linked List**: The last element is linked to the first element, forming a circular structure.

## 4. Structure of a Singly Linked List
A singly linked list consists of multiple **nodes**, where each node contains:
1. **Data** - Stores the actual value.
2. **Link (Pointer)** - Stores the address of the next node in the sequence.

### Representation of a Singly Linked List
- Example: Storing the numbers 23, 54, 78, and 90.
- Each number is stored in a separate node.
- Each node has a memory address (not necessarily sequential).

| Node | Data | Address |
|------|------|---------|
| 1    | 23   | 1000    |
| 2    | 54   | 2000    |
| 3    | 78   | 3000    |
| 4    | 90   | 4000    |

### Linking the Nodes
- Each node contains a link to the next node’s address.
- The last node contains `NULL` to indicate the end of the list.

Example:
```
Head -> [23 | 2000] -> [54 | 3000] -> [78 | 4000] -> [90 | NULL]
```

## 5. Accessing the Linked List
- The **head pointer** stores the address of the first node.
- Using the head pointer, we can traverse through the list.
- If we have the first node’s address, we can access all subsequent nodes.

## 6. Summary
- Linked lists are an alternative to arrays for dynamic memory allocation.
- They consist of nodes, where each node has data and a pointer to the next node.
- Different types include singly, doubly, and circular linked lists.
- Accessing a linked list requires a head pointer.

In the next lessons, we will learn how to create and manipulate linked lists programmatically.

