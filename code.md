**Organized Notes on Version 2.0 of Inserting Data at the Beginning of a Linked List**

### **Introduction**
- This presentation discusses **Version 2.0** of inserting data at the beginning of a **linked list**.
- The **main function** remains similar to previous lectures, creating a linked list with **two nodes**.
- The **head pointer** initially points to the first node of the list.

### **Understanding the Function Call**
- **Previous issue:** `head = add_beg(head, data);`
  - This passes `head` **by value**, not **by reference**.
  - This means changes made to `head` inside `add_beg` do not affect the original `head` in `main`.
- **Solution:** Pass the **address of head** instead.
  - Instead of passing `head`, pass `&head` (address of head pointer).
  - Example:
    - Assume `head`'s address is **600**.
    - Instead of passing `1000` (address of first node), pass `600` (address of head pointer).

### **Modification in `add_beg` Function**
- Change function parameter from:
  ```c
  struct node* head
  ```
  to
  ```c
  struct node** head
  ```
- Using a **double pointer (pointer to a pointer)** allows updating `head` in `main`.
- **Why use a double pointer?**
  - The head pointer is local to `main`, and we need to update it globally.
  - A pointer to `head` stores the address of `head`, enabling changes.

### **Steps in the `add_beg` Function**
1. **Creating a new node:**
   - The block of code initializes a new node (`ptr`).
2. **Updating the new node’s link:**
   - Instead of:
     ```c
     ptr->link = head;
     ```
   - Use:
     ```c
     ptr->link = *head;
     ```
   - `*head` retrieves the original value stored in `head` (i.e., the first node’s address `1000`).
3. **Updating the head pointer:**
   - Instead of `head = ptr;`, use:
     ```c
     *head = ptr;
     ```
   - `*head` refers to `head` in `main`, so assigning `ptr` updates `head` globally.
   - Now, `head` (in `main`) points to `ptr`, making `ptr` the new first node.

### **Final Updated Structure of Linked List**
- The **head of `main` is updated** with the new node (`ptr`).
- The list structure is now:
  ```
  Head -> [ New Node | Link ] -> [ First Node | Link ] -> [ Second Node | NULL ]
  ```
- **Output of the program:**
  ```
  345 98
  ```

### **Conclusion**
- Using a **double pointer** ensures changes in `add_beg` reflect in `main`.
- This approach allows **proper insertion at the beginning** of a linked list.
- Understanding pointer dereferencing is crucial for linked list operations.

**End of Notes**

