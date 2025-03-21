**Creating a Single Linked List (Part 1) - Summary**

### Introduction
- This tutorial explains how to create a single linked list in C.
- In the previous lecture, the creation of a single node was covered.
- The goal is to create a complete linked list with three nodes.

### Structure of a Single Linked List
- A linked list consists of nodes containing:
  - Data (e.g., 45, 98, 3)
  - A pointer linking to the next node
- The first node (head) points to the second node, the second node points to the third, and the third node’s pointer is NULL.

### Creating a Node in C
- Define a structure `struct node`:
  ```c
  struct node {
      int data;
      struct node* link;
  };
  ```
- This structure includes:
  - `data` (to store the value)
  - `link` (pointer to the next node)

### Allocating Memory for the First Node
- The first node is created using `malloc()`:
  ```c
  struct node* head;
  head = (struct node*) malloc(sizeof(struct node));
  ```
- Assign values:
  ```c
  head->data = 45;
  head->link = NULL;
  ```
- The head pointer now points to this node.

### Allocating Memory for the Second Node
- Create the second node:
  ```c
  head = (struct node*) malloc(sizeof(struct node));
  head->data = 98;
  head->link = NULL;
  ```
- **Problem:** Head now points to the second node, and the first node is lost.

### Fixing the Issue
- Introduce a new pointer `current`:
  ```c
  struct node* current;
  current = (struct node*) malloc(sizeof(struct node));
  current->data = 98;
  current->link = NULL;
  ```
- Keep `head` pointing to the first node and `current` pointing to the second.
- Update the link of the first node to point to the second node:
  ```c
  head->link = current;
  ```
- Now, the first node is linked to the second node correctly.

### Conclusion
- Successfully created and linked two nodes.
- The next part will cover adding a third node to the list.

