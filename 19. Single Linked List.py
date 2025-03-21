# **Insertion & Deletion in Singly Linked List vs. Arrays**

## **Introduction**
This session covers **inserting and deleting elements** at specific positions in **Singly Linked Lists** and **Arrays**, discussing implementation techniques and time complexity.

---

## **Insertion in a Singly Linked List (Detailed Approach)**
### **Steps for Insertion**
1. **Find the desired position** by traversing the linked list (O(N) in the worst case).
2. **Create a new node** containing the new value.
3. **Modify pointers**:
   - Set the new node’s `next` to the current node’s `next`.
   - Update the previous node’s `next` to point to the new node.
4. **Insertion Complete**.

### **Time Complexity Analysis**
- **Best Case**: O(1) (if inserting at the head)
- **Worst Case**: O(N) (if inserting at the tail or middle position)

---

## **Insertion in an Array (Detailed Approach)**
### **Steps for Insertion**
1. **Determine the insertion position**.
2. **Shift elements** to the right from the insertion index.
3. **Insert the new element** at the specified position.
4. **Insertion Complete**.

### **Time Complexity Analysis**
- **Best Case**: O(1) (if inserting at the end)
- **Worst Case**: O(N) (if inserting at the beginning or middle, requiring shifts)

---

## **Deletion in a Singly Linked List (Deleting the First Node)**
### **Steps for Deletion**
1. **Check if the list is empty**.
2. **Store the reference to the current head**.
3. **Move the head pointer** to the next node.
4. **Delete the previous head node**.
5. **Deletion Complete**.

### **Time Complexity Analysis**
- **Best Case**: O(1) (always constant time for head deletion)
- **Worst Case**: O(1) (same as best case, as it's independent of list size)

### **Function Implementation for Deletion**
```cpp
struct Node {
    int data;
    Node* next;
};

void deleteFirstNode(Node*& head) {
    if (head == nullptr) return; // If the list is empty
    Node* temp = head;
    head = head->next;
    delete temp;
}
```

---

## **Memory Allocation & Data Copying**
- **Linked List**: Memory is allocated dynamically, and elements are stored non-contiguously.
- **Array**: Elements are stored contiguously in memory, requiring shifts during insertion/deletion.
- **Copying Process**:
  - **Linked List**: No need to copy elements; only pointer adjustments are made.
  - **Array**: Shifting requires copying multiple elements, leading to performance overhead.

---

## **Comparison: Singly Linked List vs. Array (Extended)**
| Operation       | Singly Linked List | Array |
|---------------|------------------|-------|
| Insertion at Head | O(1) | O(N) |
| Insertion at Middle | O(N) | O(N) |
| Insertion at Tail | O(N) | O(1) |
| Deletion at Head | O(1) | O(N) |
| Deletion at Middle | O(N) | O(N) |
| Deletion at Tail | O(N) | O(1) |
| Memory Allocation | Dynamic | Static |
| Element Shifting | No | Yes |

---

## **Function Implementation for Insertion**
### **Singly Linked List (Insertion Function)**
```cpp
void insertAtPosition(Node*& head, int position, int value) {
    Node* newNode = new Node{value, nullptr};
    if (position == 0) {
        newNode->next = head;
        head = newNode;
        return;
    }
    Node* temp = head;
    for (int i = 0; i < position - 1 && temp != nullptr; i++) {
        temp = temp->next;
    }
    if (temp == nullptr) return;
    newNode->next = temp->next;
    temp->next = newNode;
}
```

### **Array (Insertion Function)**
```cpp
void insertAtPosition(int arr[], int& size, int position, int value) {
    if (position > size) return;
    for (int i = size; i > position; i--) {
        arr[i] = arr[i - 1];
    }
    arr[position] = value;
    size++;
}
```

---

## **Conclusion**
- **Linked Lists** are preferable for frequent insertions and deletions at arbitrary positions.
- **Arrays** perform better when insertions/deletions happen at the end.
- **Choosing the right data structure** depends on memory usage, time complexity, and efficiency requirements.

✅ **Like, Share & Subscribe for more insights!**

