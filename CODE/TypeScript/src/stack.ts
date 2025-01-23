class Stack<T> {
    private items: T[] = [];

    // Push an element onto the stack
    push(item: T): void {
        this.items.push(item);
    }

    // Pop an element from the stack
    pop(): T | undefined {
        if (this.isEmpty()) {
            console.log("Stack is empty");
            return undefined;
        }
        return this.items.pop();
    }

    // Peek the top element without removing it
    peek(): T | undefined {
        if (this.isEmpty()) {
            console.log("Stack is empty");
            return undefined;
        }
        return this.items[this.items.length - 1];
    }

    // Check if the stack is empty
    isEmpty(): boolean {
        return this.items.length === 0;
    }

    // Get the size of the stack
    size(): number {
        return this.items.length;
    }
}

// Usage Example
const stack = new Stack<number>();

stack.push(10);
stack.push(20);
stack.push(30);


console.log(stack.peek());  // Output: 30
console.log(stack.pop());   // Output: 30
console.log(stack.pop());   // Output: 30
console.log(stack.size());  // Output: 2
console.log(stack.isEmpty());  // Output: false
