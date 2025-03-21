# Creating a Single Linked List

## Part 1: Introduction to Single Linked List

### Understanding the Basics
- A **single linked list** consists of nodes connected in a linear sequence.
- Each node contains:
  - **Data** (value stored in the node)
  - **Link part** (pointer to the next node)

### Creating a Single Linked List
1. **Define the Structure:**
   ```c
   struct node {
       int data;
       struct node *link;
   };
   ```
2. **Allocate Memory for a Node:**
   - Use `malloc()` to allocate memory dynamically.
   - Example:
     ```c
     struct node *head;
     head = (struct node*)malloc(sizeof(struct node));
     ```
3. **Initialize the First Node:**
   - Assign a value to `data`.
   - Set `link` to `NULL` initially.
   - Example:
     ```c
     head->data = 45;
     head->link = NULL;
     ```

### Adding the Second Node
- Allocate memory and store the new node’s address in a temporary pointer.
- **Issue:** If we use `head = malloc(...)`, we lose the reference to the first node.
- **Solution:** Use an additional pointer (e.g., `current`).
- Example:
  ```c
  struct node *current;
  current = (struct node*)malloc(sizeof(struct node));
  current->data = 98;
  current->link = NULL;
  head->link = current;
  ```

## Part 2: Adding the Third Node

### Method 1: Using an Extra Pointer
1. **Allocate Memory for Third Node:**
   ```c
   struct node *current2;
   current2 = (struct node*)malloc(sizeof(struct node));
   current2->data = 3;
   current2->link = NULL;
   ```
2. **Link the Second Node to the Third Node:**
   ```c
   current->link = current2;
   ```
- **Problem:** If we need multiple nodes, we will require multiple pointers (`current3`, `current4`, etc.), leading to memory wastage.

### Method 2: Reusing the Pointer
- Instead of creating a new pointer (`current2`), **reuse** `current`.
- **Concept:** Use `head->link->link` to directly access the second node’s `link` part.
- **Steps:**
  1. Allocate memory using `current`.
  2. Store the new node’s address in `current`.
  3. Use `head->link->link = current` to update the link part of the second node.

- **Code Implementation:**
  ```c
  current = (struct node*)malloc(sizeof(struct node));
  current->data = 3;
  current->link = NULL;
  head->link->link = current;
  ```
- **Advantage:** No need for extra pointers, reducing memory usage.

## Conclusion
- **We successfully created a single linked list with three nodes.**
- **Best Practice:** Use method 2 to optimize memory usage.
- **Next Steps:** Add more nodes dynamically and implement deletion operations.

**Congratulations! You have created your first linked list.** 🎉

