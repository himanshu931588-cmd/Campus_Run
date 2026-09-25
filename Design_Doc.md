# Campus Run: Design & Testing Document

This document outlines the Map Design, Items, Optional Interactions, Testing Plan, and Integration Notes for **Campus Run**, ensuring smooth collaboration between the content and core engine teams.

---

## 1. Map Design

The map is designed to be compact, forcing the player to make strategic movement choices while battling the clock.

### ASCII Layout

```text
########################################
#                                      #
# [MAIN GATE]                          #
#      |                               #
# [SECURITY CHECK]                     #
#      |                               #
# [MAIN CORRIDOR] ---- [CANTEEN]       #
#      |                  |            #
# [NOTICE BOARD]    [WRONG ROUTE]      #
#      |                               #
#   [STAIRS]                           #
#      |                               #
# [FLOOR 2] ---- [FRIEND ENCOUNTER]    #
#      |                               #
# [FLOOR 3]                            #
#      |                               #
# [FLOOR 4] ---- [LIFT (BROKEN)]       #
#      |                               #
# [CLASS 404]                          #
#                                      #
########################################
```

### Room Specifications
* **Starting Point:** Main Gate
* **Required Path:** Main Gate -> Security Check -> Main Corridor -> Notice Board -> Stairs -> Floor 2 -> Floor 3 -> Floor 4 -> Class 404
* **Optional / Interaction Areas:**
  * **Canteen:** Attached East of Main Corridor. Consumes time if interacted with.
  * **Friend Encounter:** Attached East of Floor 2. Player must choose to stop or ignore.
  * **Lift:** Attached East of Floor 4. Always broken ("OUT OF ORDER").
* **Wrong Route:** Attached South of Canteen or East of Notice Board. Entering this room displays a sarcastic narrator comment and wastes time before the player has to turn back.
* **Classroom Location:** North of Floor 4 (or continuing along the linear path).

---

## 2. Item Content

Every item has a purpose in the game. Useless items have been avoided.

| Item | Description | Purpose | Interaction |
|---|---|---|---|
| **ID Card** (Required) | Your college ID. The photo looks like a mugshot. | Required to pass the Security Guard. | You show it to the guard. He stares at it, then at you, then at it again. "Theek hai, jao." |
| **Timetable** (Required) | A crumpled piece of paper holding your destiny. | Reveals that your 9:30 AM class is in Room 404 (4th floor). | You look at the timetable. "Room 404." Great. |
| **Notebook** (Optional) | Mostly empty, except for some doodles on the back page. | Provides an illusion of being a serious student. | You flip through the empty pages. Much knowledge. Very wow. |
| **Pen** (Optional) | A classic Rs. 5 blue pen. The cap is chewed. | Used for signing the attendance sheet (if you make it). | You click it twice. It works. Good. |
| **Coffee** (Optional) | Overpriced canteen coffee. | Gives you a slight speed boost but costs time to buy. | You take a sip. It tastes like regret and burnt beans. |
| **Water Bottle** (Optional) | A plastic water bottle. | Recovers stamina after climbing the stairs. | You drink some water. You feel slightly less out of breath. |

---

## 3. Optional Interactions

These events add flavor and time-sinks to the game.

### Friend Encounter (Floor 2)
* **Dialogue:** "Bro, ek minute!"
* **Choices:** 
  1. Stop
  2. Ignore
* **Consequence:** Stopping wastes precious time but gives funny dialogue. Ignoring saves time with a sarcastic narrator comment.

### Canteen (Main Corridor -> East)
* **Dialogue:** "Samosa? Garam hai!"
* **Choices:** Buy Samosa / Leave
* **Consequence:** Interacting consumes time.

### Notice Board (Before Stairs)
* **Action:** Inspect Notice Board
* **Message:** "NOTICE: All 9:30 AM classes are strictly on time. Latecomers will be roasted."

### Lift (Floor 4)
* **Action:** Call Lift
* **Result:** "OUT OF ORDER" (Forces the player to realize there's no shortcut).

---

## 4. Integration Notes

To ensure teammates can easily use the provided content without rewriting the core engine, the dialogue has been structured into clean Python dictionaries and lists in `dialogue.py`. 

### How to use `dialogue.py`:
- Import the dictionaries in `game.py` or `room.py`:
  ```python
  from dialogue import OPENING_DIALOGUE, CAMPUS_DIALOGUE, ENDING_DIALOGUE, ITEMS_DATA
  ```
- **Opening Sequence:** Loop through `OPENING_DIALOGUE` when the game starts, pausing for player input or a small `time.sleep()` if desired.
- **Endings:** When the player reaches `Class 404`, calculate the arrival time and use the keys in `ENDING_DIALOGUE` (`"on_time"`, `"slightly_late"`, `"late"`, `"very_late"`) to fetch the appropriate string.
- **Items:** When initializing items in `item.py`, pass the attributes directly from `ITEMS_DATA[item_key]`.

---

## 5. Manual Testing Checklist

Follow this checklist to ensure all mechanics and dialogues work seamlessly.

### [ ] Movement
- [ ] Player can move in every valid direction.
- [ ] Player cannot move through walls or off the map.
- [ ] Player can successfully reach the staircase from the Main Corridor.
- [ ] Player can reach the fourth floor and Room 404.

### [ ] Navigation
- [ ] Correct route works and advances the player properly.
- [ ] Wrong route triggers the correct narrator commentary.
- [ ] Player can recover and return to the main path from a wrong route.

### [ ] Time Management
- [ ] Time advances correctly per movement.
- [ ] Security sequence properly advances the time to ~9:27 AM.
- [ ] Interactions (Canteen, Friend) advance time correctly.
- [ ] Arrival time at Room 404 is accurately logged and calculated.

### [ ] Items & Inventory
- [ ] Checking the Timetable displays "Room 404".
- [ ] Inventory displays all collected items correctly.
- [ ] Interacting with or using an item does not crash the game.
- [ ] Using the ID Card at the Security Check allows passage.

### [ ] Endings (Time-Based)
- [ ] **Before 9:30:** Triggers the On-time ending ("Just in time. Sit down.").
- [ ] **9:30–9:32:** Triggers the Slightly late ending.
- [ ] **9:33–9:35:** Triggers the Late ending.
- [ ] **After 9:35:** Triggers the Very late ending ("Get out.").

### [ ] Invalid Input Handling
- [ ] Typing random characters (e.g., `X`, `abc`) does not crash the game.
- [ ] Empty input (pressing Enter) does not crash the game.
- [ ] Inputting an invalid direction (e.g., `go north` when blocked) shows an appropriate error message and does not advance time unfairly.
- [ ] Interacting with an invalid or unowned item shows a safe error message.
