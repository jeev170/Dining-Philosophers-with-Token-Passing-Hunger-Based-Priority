import threading
import time
import random
from queue import PriorityQueue
def log(message):
    print(f"[{time.strftime('%H:%M:%S')}] {message}")


# User Input

num_philosophers = int(input("Enter number of philosophers: "))
if num_philosophers < 2:
    print(" At least 2 philosophers are required for the Dining Philosophers Problem.")
    exit()
# Safe maximum number of tokens (non-adjacent rule)
num_tokens = num_philosophers // 2


print(f"\n Number of philosophers: {num_philosophers}")
print(f" Number of tokens (auto-calculated): {num_tokens}\n")

# Timing configuration
EAT_TIME = 2
THINK_TIME = 1

# Shared Resources
forks = [threading.Lock() for _ in range(num_philosophers)]
token_positions = []
token_lock = threading.Lock()
priority_queue = PriorityQueue()

# Initialize tokens at safe distances (non-adjacent)
token_positions = [i for i in range(0, num_philosophers, num_philosophers // num_tokens)]
if len(token_positions) > num_tokens:
    token_positions = token_positions[:num_tokens]
    token_ids = {token_positions[i]: i + 1 for i in range(len(token_positions))}

# Philosopher Thread

class Philosopher(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
        self.hunger = 0
        self.running = True

    def left_fork(self):
        return forks[self.id]

    def right_fork(self):
        return forks[(self.id + 1) % num_philosophers]

    def think(self):
        log(f"Philosopher {self.id} is THINKING ")
        time.sleep(random.uniform(0.5, THINK_TIME))

    def eat(self):
        
        time.sleep(EAT_TIME)
        log(f"Philosopher {self.id} finishes EATING")
        self.hunger = 0

    def run(self):
        global token_positions
        while self.running:
            self.think()
            self.hunger += 1  # gets hungrier
            log(f"Philosopher {self.id} is HUNGRY (Hunger = {self.hunger})")
            # Add to priority queue based on hunger (max priority = hungriest)
            priority_queue.put((-self.hunger, self.id))

            with token_lock:
                if self.id in token_positions:
                    token_index = token_positions.index(self.id)
                    token_id = token_index + 1  # Token number
                    log(f"Token {token_id} currently with Philosopher {self.id}")
                    left_acquired = self.left_fork().acquire(timeout=0.1)
                    right_acquired = self.right_fork().acquire(timeout=0.1)

                    if left_acquired and right_acquired:
                        log(f"Token {token_id} -> Philosopher {self.id} starts EATING")
                        self.eat()
                        self.left_fork().release()
                        self.right_fork().release()
                    else:
                        if left_acquired:
                            self.left_fork().release()
                        if right_acquired:
                            self.right_fork().release()
                        log(f"Philosopher {self.id} couldn’t acquire forks")

    # Token passing
                    if not priority_queue.empty():
                        _, next_id = priority_queue.get()
                        log(f" Philosopher {next_id} selected as most hungry — gets Token {token_id} next.")
                        idx = token_positions.index(self.id)
                        token_positions[idx] = next_id
                        log(f" Token {token_id} passed from Philosopher {self.id} -> Philosopher {next_id}")
                    else:
                        idx = token_positions.index(self.id)
                        token_positions[idx] = (self.id + 1) % num_philosophers
                        log(f"Token {token_id} passed from Philosopher {self.id} -> Philosopher {(self.id + 1) % num_philosophers}")

            time.sleep(0.5)


# Start Simulation

philosophers = [Philosopher(i) for i in range(num_philosophers)]
for p in philosophers:
    p.start()

SIMULATION_TIME = 10
time.sleep(SIMULATION_TIME)

for p in philosophers:
    p.running = False
for p in philosophers:
    p.join()

print("\nSimulation completed successfully ")
