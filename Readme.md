# **🍽️ Dining Philosophers with Token Passing & Hunger-Based Priority – Python Threading Simulation**

This project is a Python implementation of the classic **Dining Philosophers Problem**, enhanced with:

* **Token-based fork acquisition**
* **Hunger-based priority queue scheduling**
* **Non-adjacent token distribution**
* **Thread-based philosopher simulation**
* **Safe deadlock-free dining mechanism**

The goal is to simulate realistic dining behavior while preventing starvation and deadlock using controlled token movement and priority scheduling.

---

## 📌 **Features**

### ✔ **Token Passing Mechanism**

* Only philosophers holding a *token* may attempt to acquire forks.
* Tokens are placed initially at **non-adjacent positions** for safety.
* After eating (or failing to eat), a philosopher **passes the token**:

  * Preferably to the **hungriest philosopher** in the priority queue.
  * Otherwise, to the **next philosopher** clockwise.

### ✔ **Hunger-Based Priority Queue**

* Hunger increases every time a philosopher becomes hungry.
* Priority queue ensures **hungriest philosophers get tokens first**.
* Prevents starvation.

### ✔ **Thread-Based Execution**

* Each philosopher is a thread:

  * Thinks
  * Becomes hungry
  * Attempts to eat (if holding a token)

### ✔ **Fork Locking**

* Forks are `threading.Lock()` objects.
* Safe and fair access using timed lock acquisition.

---

## 🏗 **How It Works**

### 1️⃣ Input

The user enters the number of philosophers:

```
Enter number of philosophers: 5
```

Automatically computed:

```
Number of tokens: 2
```

### 2️⃣ Token Placement

Tokens are distributed at **equal safe distances** (non-adjacent).

### 3️⃣ Philosopher Lifecycle

```
THINK → HUNGRY (+1 hunger) → (Has token?) Try to EAT → Pass token
```

Eating resets hunger to zero.

### 4️⃣ Token Passing Rules

When a philosopher finishes/attempts eating:

* If priority queue is not empty → token moves to **most hungry philosopher**.
* Else → token moves to **next philosopher in circle**.

---

## ▶️ **How to Run**

### **Requirements**

* Python 3.x

### **Run the Simulation**

```
python dining_philosophers.py
```

Enter number of philosophers when prompted.

Simulation runs for 10 seconds and prints all events.

---

## 📤 **Output Example**

```
[12:01:22] Philosopher 0 is THINKING
[12:01:23] Philosopher 0 is HUNGRY (Hunger = 1)
[12:01:23] Token 1 currently with Philosopher 0
[12:01:23] Token 1 -> Philosopher 0 starts EATING
[12:01:25] Philosopher 0 finishes EATING
[12:01:25] Philosopher 3 selected as most hungry — gets Token 1 next.
[12:01:25] Token 1 passed from Philosopher 0 -> Philosopher 3
```

---

## 🧠 **Concepts Demonstrated**

| Concept                    | Description                           |
| -------------------------- | ------------------------------------- |
| **Deadlock Prevention**    | Token prevents circular wait          |
| **Starvation Prevention**  | Hunger-based priority queue           |
| **Thread Synchronization** | Fork locking using `threading.Lock()` |
| **Distributed Scheduling** | Token passing between philosophers    |

---

## 📦 **Project Structure**

```
dining_philosophers.py
README.md
```

---

## 📝 **Simulation Duration**

The simulation runs for:

```python
SIMULATION_TIME = 10
```

Modify this value to extend the run time.

---

## ✔ **End of Simulation**

At the end, philosophers stop gracefully:

```
Simulation completed successfully
```

---
