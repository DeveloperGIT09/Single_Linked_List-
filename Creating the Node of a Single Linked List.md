Here is your mind map for **Creating the Node of a Single Linked List**:  

```
                [Creating the Node of a Single Linked List]
                                │
        ┌───────────────────────┴───────────────────────┐
    [Introduction]                                      [Self-Referential Structure]
        │                                                   │
    - Node = Fundamental unit of SLL                     - Contains pointer to same structure type
    - Consists of:                                       - Example:
        • Data (value)                                       struct abc {
        • Link (pointer)                                        struct abc *ptr;
    - Implemented using self-referential structures           };
        │
        └──► Example: struct node { int data; struct node *link; };

                                │
    ┌───────────────────────────────────────────────────────────┐
    │                   [Defining a Node in C]                  │
    │   struct node {                                           │
    │       int data;  // Stores actual value                   │
    │       struct node *link;  // Points to next node          │
    │   };                                                      │
    │   - Self-referential since it contains pointer to itself  │
    └───────────────────────────────────────────────────────────┘

                                │
        ┌──────────────────────────────────────────┐
        │       [Steps to Create a Node]           │
        ├──────────────────────────────────────────┤
        │ 1. Declare Pointer to struct node        │
        │    struct node *head = NULL;            │
        │                                          │
        │ 2. Allocate Memory Using `malloc`        │
        │    head = (struct node*) malloc(sizeof(struct node)); │
        │                                          │
        │ 3. Initialize Node                        │
        │    head->data = 45; head->link = NULL;   │
        │                                          │
        │ 4. Print the Data                         │
        │    printf("%d", head->data);             │
        └──────────────────────────────────────────┘

                                │
    ┌───────────────────────────────────────────────────────────┐
    │                     [Key Takeaways]                      │
    │  - Self-referential structures enable linked lists.      │
    │  - Memory is allocated dynamically using `malloc`.       │
    │  - The head pointer is crucial for accessing nodes.      │
    │  - Arrow operator (`->`) is used for pointer access.     │
    │  - Nodes are lost if pointers are not managed properly.  │
    └───────────────────────────────────────────────────────────┘

                                │
                         [Conclusion]
                - A node is created using struct & pointers.
                - Dynamic memory allocation is necessary.
                - Understanding pointers is crucial for linked lists.
```

This mind map captures the essential points in a structured manner. Let me know if you need any modifications! 😊
**Creating the Node of a Single Linked List**

### **Introduction**
- A **node** is the fundamental building block of a **singly linked list**.
- Each node consists of **two parts**:
  1. **Data** (stores the actual value)
  2. **Link (Pointer)** (stores the address of the next node)
- Nodes are dynamically allocated using **self-referential structures** in C.

### **Self-Referential Structure**
- A **self-referential structure** contains a pointer to a structure of the same type.
- Example:
  ```c
  struct abc {
      struct abc *ptr;
  };
  ```
- This structure points to another structure of type **abc**, making it **self-referential**.

### **Defining a Node in C**
- A node is implemented using a **struct**:
  ```c
  struct node {
      int data;           // Data part
      struct node *link;  // Pointer to the next node
  };
  ```
- **Key Points**:
  - `int data` can be of any data type (char, float, etc.).
  - `struct node *link` points to the next node.
  - This structure is **self-referential** since it contains a pointer to itself.

### **Creating a Node in C**
#### **Required Libraries**
- `#include <stdio.h>` → For standard input/output operations.
- `#include <stdlib.h>` → For dynamic memory allocation (`malloc`).

#### **Steps to Create a Node**
1. **Declare a Pointer to struct node**
   ```c
   struct node *head;
   head = NULL;
   ```
   - The `head` pointer stores the address of the first node.
   - Initially, `head` is set to `NULL`.

2. **Allocate Memory Using `malloc`**
   ```c
   head = (struct node*) malloc(sizeof(struct node));
   ```
   - `malloc` dynamically allocates memory for a new node.
   - `sizeof(struct node)` ensures enough space is allocated for **data** and **pointer**.
   - The returned `void*` is typecasted to `struct node*`.

3. **Initialize the Node**
   ```c
   head->data = 45;   // Assign value to data part
   head->link = NULL; // Initialize link part to NULL
   ```
   - `head->data` stores **45**.
   - `head->link` is set to **NULL**, meaning it does not point to another node yet.

4. **Print the Data**
   ```c
   printf("%d", head->data);
   ```
   - This outputs `45` since `head->data` stores `45`.

### **Key Takeaways**
- **Self-referential structures** are used to create linked list nodes.
- **Memory allocation** is done dynamically using `malloc`.
- The **head pointer** is crucial for accessing nodes.
- The **arrow operator (`->`)** is used to access members of a struct via a pointer.
- **If a pointer to the node is not stored, the node becomes inaccessible.**

### **Conclusion**
- A **node** in a singly linked list is created using a struct with a self-referential pointer.
- **Memory allocation** and proper pointer management are essential for linked list operations.
- Understanding these concepts is the foundation for working with linked lists in C.

