
# 🏆 Object-Oriented Programming (OOP) in Java & Python

## 📌 What is OOP?
Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects" that bundle data and behavior together. OOP enhances **code reusability, modularity, and scalability**.

## 🎯 Key Principles of OOP
OOP is based on four fundamental principles:

### 1️⃣ Encapsulation 🛡️
Encapsulation means restricting direct access to some of an object's components, which can prevent accidental interference and modification of data.

✅ **Java Example:**
```java
class BankAccount {
    private double balance;
    
    public BankAccount(double balance) {
        this.balance = balance;
    }
    
    public double getBalance() {
        return balance;
    }
    
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }
}
```

✅ **Python Example:**
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
```

### 2️⃣ Inheritance 👪
Inheritance allows a class (child) to derive properties and behavior from another class (parent), enabling code reusability.

✅ **Java Example:**
```java
class Animal {
    void makeSound() {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {
    void bark() {
        System.out.println("Dog barks");
    }
}
```

✅ **Python Example:**
```python
class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")
```

### 3️⃣ Polymorphism 🎭
Polymorphism allows methods to take different forms based on the context.

✅ **Java Example (Method Overriding):**
```java
class Animal {
    void makeSound() {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {
    @Override
    void makeSound() {
        System.out.println("Dog barks");
    }
}
```

✅ **Python Example:**
```python
class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def make_sound(self):  # Overriding parent method
        print("Dog barks")
```

### 4️⃣ Abstraction 🔍
Abstraction is the concept of hiding implementation details and showing only the necessary functionalities.

✅ **Java Example (Abstract Class):**
```java
abstract class Vehicle {
    abstract void start(); // Abstract method
}

class Car extends Vehicle {
    void start() {
        System.out.println("Car starts with a key");
    }
}
```

✅ **Python Example (Abstract Base Class):**
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts with a key")
```

---

## ⚖️ Java vs. Python in OOP

| Feature        | Java 🏆 | Python 🐍 |
|---------------|--------|----------|
| Static Typing | ✅ Yes | ❌ No |
| Multiple Inheritance | ❌ No (Uses Interfaces) | ✅ Yes |
| Abstract Classes | ✅ Yes | ✅ Yes (Using `abc` module) |
| Encapsulation | ✅ Strict (private, protected, public) | ✅ Soft (Name mangling `__var`) |
| Method Overloading | ✅ Yes | ❌ No (Can simulate with default arguments) |

---

## 🔥 OOP Interview Questions & Answers

### 🔹 Q1: What is the difference between method overloading and method overriding?
✅ **Answer:**
- **Method Overloading**: Multiple methods with the same name but different parameters (only in Java, not in Python).
- **Method Overriding**: Redefining a method in a subclass that is already defined in the parent class.

### 🔹 Q2: What are access specifiers in Java?
✅ **Answer:**
Java provides:
- `public`: Accessible everywhere
- `protected`: Accessible in the same package and subclasses
- `private`: Accessible only within the class
- (Default): Accessible within the same package

### 🔹 Q3: How does Python implement encapsulation?
✅ **Answer:**
Python uses **name mangling** (`__variable`) to make attributes private, though they can still be accessed using `_ClassName__variable`.

### 🔹 Q4: Can Python achieve multiple inheritance? How?
✅ **Answer:**
Yes! Python allows multiple inheritance by defining multiple parent classes.

Example:
```python
class A:
    def show(self):
        print("Class A")

class B:
    def display(self):
        print("Class B")

class C(A, B):
    pass

obj = C()
obj.show()    # Output: Class A
obj.display() # Output: Class B
```

---

## 🎯 Summary
✅ **Java** is more structured and follows strict OOP rules.
✅ **Python** is more flexible but follows OOP principles dynamically.
✅ **Key OOP concepts**: **Encapsulation, Inheritance, Polymorphism, Abstraction**.
✅ **Practice interview questions** to solidify your understanding.

---

🚀 **Keep Practicing and Crack Your OOP Interview!** 🏆

