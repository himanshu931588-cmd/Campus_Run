# Campus Run
### "Aagaye Maharaj"

A small, funny, text-based adventure game made in Python.

---

## What is this game?

You play as a college student who reaches college at **9:25 AM** for a class that starts at **9:30 AM**. You think you are early. You are wrong.

You have to pass security, find your classroom, discover it's on the 4th floor, find out the lift is broken, run up the stairs, and reach Room 404 before (or after) your class starts.

**Goal:** Reach the classroom.

---

## How to play

1. Run the game in your terminal.
2. Read the story at the start (the auto ride and the security check).
3. Once you're in the campus, use these keys to play:

```
W → Move Up
A → Move Left
S → Move Down
D → Move Right
E → Interact (talk, open, use)
I → Check your inventory
Q → Quit the game
```

4. Move through the campus, go up the stairs, and reach Room 404.
5. See how the teacher reacts based on when you arrive.
6. Choose to play again and try to beat your time.

---

## The story in short

```
Auto arrives → Security check → Explore campus →
Find the stairs → Climb 4 floors → Reach Room 404 →
"May I come in, Sir?" → "Aagaye maharaj aap."
```

Along the way you might run into:
- A **broken lift** (always broken, just for comedy)
- A **friend** who wants to talk (costs you time)
- A **canteen** selling samosas (costs you time)
- A **notice board** with useless information
- **Wrong rooms** if you take the wrong turn

None of these are required — you can ignore them and go straight for the classroom.

---

## Endings

How late (or on time) you are decides your ending:

| Arrival Time | Result           |
|---------------|------------------|
| Before 9:30   | Responsible Student |
| 9:30 – 9:32   | Just Made It     |
| 9:33 – 9:35   | Classic          |
| 9:36 onward   | Aagaye Maharaj   |

At the end, you'll see a small result screen showing your delay, wrong turns, and optional stops — then you can play again.

---

## What's inside the code

The game is built using simple Python classes:

- **Player** – tracks your position, time, and inventory
- **Room** – represents each area of the campus (corridor, stairs, floors, classroom, etc.)
- **Item** – things like your ID card and timetable
- **Game** – runs the overall game loop and story

## File structure

```
campus-run/
│
├── main.py       → starts the game
├── game.py       → controls the game loop
├── player.py     → player class and movement
├── room.py       → rooms and navigation
├── item.py       → items you can use
└── README.md     → this file
```

---

## Requirements

- Python 3 (no extra libraries needed)
- Works in any terminal or on Replit

To run:
```
python main.py
```

---

## Why this game exists

This game is built for a **Text-Based Adventure** category competition. It keeps things simple on purpose:

- No combat
- No health bars or levels
- No complicated systems

Just a small, playable, funny story about the very relatable experience of being "five minutes early" and somehow still ending up late.

**"Bas class tak pahunchna hai."**