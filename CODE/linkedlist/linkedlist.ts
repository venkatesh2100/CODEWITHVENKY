class Node<T> {
  data: T;
  next: Node<T> | null;

  constructor(data: T) {
    this.data = data;
    this.next = null;
  }
}

class LinkedList<T> {
  head: Node<T> | null;
  tail: Node<T> | null;
  length: number;

  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }

  // Append a node to the end of the list
  append(data: T) {
    const newNode = new Node(data);

    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail!.next = newNode;
      this.tail = newNode;
    }

    this.length++;
  }

  // Prepend a node to the beginning of the list
  prepend(data: T) {
    const newNode = new Node(data);

    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      newNode.next = this.head;
      this.head = newNode;
    }

    this.length++;
  }

  // Insert a node at a specific index
  insert(data: T, index: number) {
    if (index < 0 || index > this.length) {
      throw new Error("Invalid index");
    }

    if (index === 0) {
      this.prepend(data);
    } else if (index === this.length) {
      this.append(data);
    } else {
      let current = this.head;
      let previous = null;
      let i = 0;

      while (i < index) {
        previous = current;
        current = current!.next!;
        i++;
      }

      const newNode = new Node(data);
      newNode.next = current;
      previous!.next = newNode;
      this.length++;
    }
  }

  // Remove a node at a specific index
  remove(index: number) {
    if (index < 0 || index >= this.length) {
      throw new Error("Invalid index");
    }

    if (index === 0) {
      this.head = this.head!.next;
    } else if (index === this.length - 1) {
      let current = this.head;
      while (current!.next !== this.tail) {
        current = current!.next;
      }
      current!.next = null;
      this.tail = current;
    } else {
      let current = this.head;
      let previous = null;
      let i = 0;

      while (i < index) {
        previous = current;
        current = current!.next!;
        i++;
      }

      previous!.next = current!.next;
    }

    this.length--;
  }

  // Get the node at a specific index
  get(index: number) {
    if (index < 0 || index >= this.length) {
      throw new Error("Invalid index");
    }

    let current = this.head;
    let i = 0;

    while (i < index) {
      current = current!.next!;
      i++;
    }

    return current;
  }

  // Reverse the linked list
  reverse() {
    let previous = null;
    let current = this.head;
    let next = null;

    while (current) {
      next = current.next;
      current.next = previous;
      previous = current;
      current = next;
    }

    this.head = previous;
  }
}
