**Array vs. Single Linked List (In Terms of Representation)**

### **Introduction**
- Arrays and singly linked lists are two fundamental data structures used to store lists of numbers in memory.
- Both have different ways of storing and organizing data.

### **Array Representation**
- Arrays store elements in **consecutive memory locations**.
- Example list: **[23, 54, 78, 90]**.
- If the **base address** of the array is **1000** and the integer size is **4 bytes**:
  - The first element (23) is at **1000**.
  - The second element (54) is at **1004**.
  - The third element (78) is at **1008**.
  - The last element (90) is at **1012**.
- **Key Characteristics**:
  - Elements are stored sequentially in memory.
  - Memory blocks are allocated in **consecutive fashion**.
  - Array is a **sequential representation** of a list.

### **Single Linked List Representation**
- A **single linked list** consists of **nodes** that are connected via pointers.
- Each node contains:
  1. **Data** (e.g., 23, 54, 78, 90)
  2. **Pointer** to the next node’s memory address.
- **Example representation with assumed memory addresses**:
  - First node (23) at **1000**, pointing to the second node.
  - Second node (54) at **5000**, pointing to the third node.
  - Third node (78) at **4750**, pointing to the fourth node.
  - Last node (90) at **3978**, pointing to NULL.
- **Key Characteristics**:
  - Nodes are **not stored in consecutive memory locations**.
  - Memory allocation is **random**, and nodes are scattered in memory.
  - Each node’s link part contains the **address of the next node**.
  - **Head pointer** points to the first node of the list.
  - Since nodes are linked via pointers, this is called **linked representation**.

### **Conclusion**
- Arrays have **sequential representation** where elements are stored in contiguous memory locations.
- Single linked lists have **linked representation**, where nodes are scattered but connected through pointers.
- Arrays provide **direct access** to elements, whereas linked lists require **traversal** to access elements.

