# Campus Run

## Game Overview
**Campus Run** is a comedy-focused 2D text-based/ASCII adventure game set in a college campus. It captures the universal, anxiety-inducing student experience of trying to make it to class on time while dealing with everyday campus obstacles.

## Story
The objective is simple yet daunting: **Reach the correct classroom after arriving at college at 9:25 AM for a 9:30 AM class.**

You start your morning with misplaced confidence. 9:25 AM. You have five whole minutes. Perfect. 
But soon, the realities of college life strike—from the meticulous security guard checking your bag and ID at the gate, to broken elevators and chatty friends. Every step you take and every interaction you have costs you precious time.

Will you make it to Room 404 before 9:30 AM, or will you face the ultimate professor roast: *"Aagaye maharaj aap."*?

## Controls
- Standard directional input to move between rooms (North, South, East, West).
- Text commands to interact with objects and people (e.g., `inspect notice board`, `talk friend`, `drink coffee`).
- Inventory commands to check your items (e.g., `use id card`, `read timetable`).

## Gameplay
- **Time Management:** Time ticks forward as you move and interact. Taking the wrong route or stopping for a samosa at the canteen might just make you late.
- **Exploration:** Navigate through the Main Gate, Corridors, Stairs, and various Floors to find your classroom.
- **Dynamic Endings:** The teacher's reaction when you enter the class completely depends on your exact arrival time (On-time, Slightly late, Late, Very late).

## Comedy Concept
The comedy style mimics authentic college humor, incorporating sarcasm, situational irony, short punchlines, and Hinglish. The game features a self-aware narrator who lightly mocks your failures ("You were early. Past tense.") and highly relatable scenarios like the elevator always being "OUT OF ORDER" when you need it most.

## OOP Concepts
This game is built on strong Object-Oriented Programming (OOP) principles:
- **Classes & Objects:** Core entities like `Player`, `Room`, `Item`, and `Game` are encapsulated in their respective classes.
- **State Management:** The `Game` class handles time updates, inventory state, and game endings based on player actions.
- **Modularity:** Dialogue and content are separated into `dialogue.py` for clean integration and easy expansion without touching the core engine.

## How to Run
1. Clone the repository: `git clone https://github.com/himanshu931588-cmd/Campus_Run`
2. Navigate to the project directory: `cd Campus_Run`
3. Run the main file: `python main.py`

## Team Members
*(Add your team members here)*
- Developer 1
- Developer 2
- Developer 3