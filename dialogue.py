# dialogue.py
# Contains all the text, dialogue, and item content for Campus Run.

# ---------------------------------------------------------
# 1. DIALOGUE SECTIONS
# ---------------------------------------------------------

OPENING_DIALOGUE = [
    "9:25 AM. You step out of the auto.",
    "PLAYER: '9:25... five minutes early. Perfect.'",
    "You walk towards the main gate with misplaced confidence.",
    "SECURITY GUARD: 'Oye! Kahan ja raha hai? ID dikha!'",
    "He begins checking your bag with the thoroughness of an airport security check.",
    "NARRATOR: You were early. Past tense.",
    "Time is ticking. It's now 9:27 AM. The confidence is fading."
]

CAMPUS_DIALOGUE = {
    "timetable_check": "You check your timetable. Your heart drops.\nPLAYER: 'Fourth floor?!'",
    "lift_broken": "ELEVATOR: OUT OF ORDER\nPLAYER: 'Of course.'",
    "stairs_commentary": "NARRATOR: Ah, the stairs. Nature's treadmill. You are out of breath.",
    "wrong_route": "NARRATOR: That was definitely not Room 404. Excellent route selection."
}

INTERACTIONS_DIALOGUE = {
    "friend_encounter": "FRIEND: 'Bro, ek minute! Sunna...'",
    "friend_ignore": "NARRATOR: Friendship has been maintained. Attendance has not. (Wait, you ignored him! Attendance is saved!)",
    "friend_stop": "NARRATOR: You stopped. The gossip was mid, and you lost precious time.",
    "canteen": "CANTEEN UNCLE: 'Samosa? Garam hai!'",
    "canteen_interact": "NARRATOR: You bought a Samosa. It was indeed garam. Time was wasted.",
    "notice_board": "NOTICE: All 9:30 AM classes are strictly on time. Latecomers will be roasted."
}

CLASSROOM_DIALOGUE = {
    "door_open": "You push the door open. The squeak echoes through the silent room.",
    "ask_entry": "PLAYER: 'May I come in, Sir?'",
    "teacher_response": "TEACHER: 'Aagaye maharaj aap.'",
    "class_reaction": "NARRATOR: 60 heads turn to look at you. You consider melting into the floor."
}

ENDING_DIALOGUE = {
    "on_time": {
        "text": "TEACHER: 'Just in time. Sit down.'\nNARRATOR: A rare victory. You survived."
    },
    "slightly_late": {
        "text": "TEACHER: 'Class started at 9:30. It is 9:32. Go sit at the back.'\nNARRATOR: Minimal damage. You'll take it."
    },
    "late": {
        "text": "TEACHER: 'Good morning! Why didn't you just come for the next lecture? Stand at the back.'\nNARRATOR: The classic roast. Friendship has been maintained. Attendance has not."
    },
    "very_late": {
        "text": "TEACHER: 'Get out.'\nNARRATOR: Short, sweet, and devastating. Better luck tomorrow."
    }
}

# ---------------------------------------------------------
# 2. ITEMS CONTENT
# ---------------------------------------------------------

ITEMS_DATA = {
    "id_card": {
        "name": "ID Card",
        "description": "Your college ID. The photo looks like a mugshot.",
        "purpose": "Required to pass the Security Guard.",
        "interaction": "You show it to the guard. He stares at it, then at you, then at it again. 'Theek hai, jao.'"
    },
    "timetable": {
        "name": "Timetable",
        "description": "A crumpled piece of paper holding your destiny.",
        "purpose": "Reveals that your 9:30 AM class is in Room 404 (4th floor).",
        "interaction": "You look at the timetable. 'Room 404.' Great."
    },
    "notebook": {
        "name": "Notebook",
        "description": "Mostly empty, except for some doodles on the back page.",
        "purpose": "Provides an illusion of being a serious student.",
        "interaction": "You flip through the empty pages. Much knowledge. Very wow."
    },
    "pen": {
        "name": "Pen",
        "description": "A classic Rs. 5 blue pen. The cap is chewed.",
        "purpose": "Used for signing the attendance sheet (if you make it).",
        "interaction": "You click it twice. It works. Good."
    },
    "coffee": {
        "name": "Coffee",
        "description": "Overpriced canteen coffee.",
        "purpose": "Gives you a slight speed boost but costs time to buy.",
        "interaction": "You take a sip. It tastes like regret and burnt beans."
    },
    "water_bottle": {
        "name": "Water Bottle",
        "description": "A plastic water bottle.",
        "purpose": "Recovers stamina after climbing the stairs.",
        "interaction": "You drink some water. You feel slightly less out of breath."
    }
}
