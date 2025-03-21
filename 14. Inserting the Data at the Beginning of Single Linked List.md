# Inserting Data at the Beginning of a Single Linked List (2nd Method)

## Introduction
In this method, we insert a new node at the beginning of a **Singly Linked List** by passing the **address of the head pointer** instead of passing it by value. This ensures that changes made inside the function reflect in the main function. Let's explore the key steps involved.

---

## **Understanding the Main Function**
- The main function first creates a linked list with two nodes.
- The `head` pointer points to the first node.
- The function call `head = add_beg(head, data);` was previously used, but this follows **pass by value**, which does not update the original `head` in memory.
- To update `head` correctly, we **pass its address** instead.
  
### **Why Pass the Address of `head`?**
- Suppose `head` is stored at address `600` and points to the first node at `1000`.
- Instead of passing `1000`, we pass `600` (`&head`), ensuring that modifications in the function reflect in the main function.

---

## **Modifications in the `add_beg` Function**
### **Updating the Function Signature**
- Previously: `struct node* add_beg(struct node* head, int data);`
- Updated: `void add_beg(struct node** head, int data);`
- We change `struct node* head` to `struct node** head`, making it a **double pointer**.
- A **double pointer** stores the address of another pointer, allowing us to modify `head` from within the function.

### **Creating a New Node**
```c
struct node* ptr = (struct node*)malloc(sizeof(struct node));
ptr->data = data;
```
- A new node `ptr` is created and initialized with the given `data`.

### **Updating the Link Part**
```c
ptr->link = *head;
```
- Instead of `ptr->link = head;`, we use `*head`, which dereferences the pointer to obtain the actual `head` address.
- `*head` contains `1000` (address of the first node), which is now stored in `ptr->link`.

### **Updating the Head Pointer**
```c
*head = ptr;
```
- This updates the head pointer to `ptr`, effectively inserting the new node at the beginning.
- The `head` pointer in the **main function** now points to the newly added node.

---

## **Final State of the Linked List**
- The linked list before insertion:
  ```
  Head -> [98] -> [45] -> NULL
  ```
- After inserting `34`:
  ```
  Head -> [34] -> [98] -> [45] -> NULL
  ```
- The output when printed: `34 98 45`

---

## **Key Takeaways**
✅ Using **pass by reference** (double pointer) allows us to modify `head` in the main function.
✅ `ptr->link = *head;` ensures the new node correctly links to the existing list.
✅ `*head = ptr;` updates `head` to point to the new first node.
✅ This method is crucial for efficient **dynamic insertion** in linked lists.

---

## **Code Implementation**
```c
#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node* link;
};

void add_beg(struct node** head, int data) {
    struct node* ptr = (struct node*)malloc(sizeof(struct node));
    ptr->data = data;
    ptr->link = *head;
    *head = ptr;
}

void printList(struct node* head) {
    struct node* temp = head;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->link;
    }
    printf("\n");
}

int main() {
    struct node* head = NULL;
    add_beg(&head, 45);
    add_beg(&head, 98);
    add_beg(&head, 34);
    printList(head);
    return 0;
}
```
---

## **Conclusion**
This method optimizes **linked list insertion at the beginning** by passing the address of `head`, ensuring efficient memory updates. Understanding pointer manipulation and double pointers is crucial for mastering linked list operations.

📌 **Practice:** Try inserting multiple nodes at the beginning and observe how `head` updates dynamically!

