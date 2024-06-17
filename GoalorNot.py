import random

def take_shot():
    outcome = random.choice(["Goal!", "Miss!"])
    return outcome

def shootout():
    print("Welcome to the Football Shootout Simulation!")
    print("You have 5 penalty shots to score as many goals as possible.\n")
    
    goals = 0
    
    for shot_number in range(1, 6):
        input(f"Press Enter to take shot {shot_number}...")
        result = take_shot()
        print(f"Shot {shot_number}: {result}")
        
        if result == "Goal!":
            goals += 1
    
    print(f"\nShootout over! You scored {goals} out of 5 shots.")

if __name__ == "__main__":
    shootout()
