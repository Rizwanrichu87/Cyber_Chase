import re
import os

game_dir = r"c:\Users\Rizwan\Documents\Cyper case"

# 1. Update GAME_STRUCTURE_AND_FLOWCHART.txt
file_path = os.path.join(game_dir, "GAME_STRUCTURE_AND_FLOWCHART.txt")
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace strings
replacements = [
    ("(4 Encrypted Files)", "(7 Encrypted Files)"),
    ("5 Level Progress Tracker", "8 Level Progress Tracker"),
    ("START: 5 SUSPECTS", "START: 8 SUSPECTS"),
    ("LEVEL 5 (MEGA PUZZLE)", "LEVEL 8 (MEGA PUZZLE)")
]
for old, new in replacements:
    content = content.replace(old, new)

# Expand Suspect list in the flowchart
suspect_list_old = """START: 8 SUSPECTS
┌─────────────────────────────┐
│ 1. Elias Vance              │
│ 2. Dr. Aris Thorne          │
│ 3. Nova Black               │
│ 4. Lyra Vance               │
│ 5. Kaelen Cross             │
└─────────────────────────────┘"""
suspect_list_new = """START: 8 SUSPECTS
┌─────────────────────────────┐
│ 1. Elias Vance              │
│ 2. Dr. Aris Thorne          │
│ 3. Nova Black               │
│ 4. Lyra Vance               │
│ 5. Kaelen Cross             │
│ 6. Jaxon Reed               │
│ 7. Silas Voss               │
│ 8. Elara Quinn              │
└─────────────────────────────┘"""
content = content.replace(suspect_list_old, suspect_list_new)

# Add level 5, 6, 7 blocks
level_4_block = """LEVEL 4
┌────────────────────────────────────────────┐
│ FILE: shield_grid.enc                      │
│ PASSWORD: ZEROEXPLOIT                      │
│ HINT: Check the Timeline for backdoor      │
├────────────────────────────────────────────┤
│ ✓ CORRECT                                  │
│ ↓                                          │
│ CLUE REVEALED: Kaelen has 8 witnesses        │
│ ↓                                          │
│ SUSPECT CLEARED: Kaelen Cross ✓             │
└────────────────────────────────────────────┘
         ↓
    Level 4 Complete
         ↓
    [LEVEL 5 UNLOCKED - MEGA PUZZLE]"""

levels_5_6_7 = """LEVEL 4
┌────────────────────────────────────────────┐
│ FILE: shield_grid.enc                      │
│ PASSWORD: ZEROEXPLOIT                      │
│ HINT: Check the Timeline for backdoor      │
├────────────────────────────────────────────┤
│ ✓ CORRECT                                  │
│ ↓                                          │
│ CLUE REVEALED: Kaelen has 8 witnesses        │
│ ↓                                          │
│ SUSPECT CLEARED: Kaelen Cross ✓             │
└────────────────────────────────────────────┘
         ↓
    Level 4 Complete
         ↓
    [LEVEL 5 UNLOCKED]


LEVEL 5
┌────────────────────────────────────────────┐
│ FILE: packet_headers.enc                   │
│ PASSWORD: GHOSTNODE                        │
│ HINT: Binary to ASCII                      │
├────────────────────────────────────────────┤
│ ✓ CORRECT                                  │
│ ↓                                          │
│ CLUE REVEALED: Jaxon trapped in elevator   │
│ ↓                                          │
│ SUSPECT CLEARED: Jaxon Reed ✓              │
└────────────────────────────────────────────┘
         ↓
    Level 5 Complete
         ↓
    [LEVEL 6 UNLOCKED]


LEVEL 6
┌────────────────────────────────────────────┐
│ FILE: memory_dump.enc                      │
│ PASSWORD: SYSTEMFAIL                       │
│ HINT: Hexadecimal to ASCII                 │
├────────────────────────────────────────────┤
│ ✓ CORRECT                                  │
│ ↓                                          │
│ CLUE REVEALED: Silas at loading dock       │
│ ↓                                          │
│ SUSPECT CLEARED: Silas Voss ✓              │
└────────────────────────────────────────────┘
         ↓
    Level 6 Complete
         ↓
    [LEVEL 7 UNLOCKED]


LEVEL 7
┌────────────────────────────────────────────┐
│ FILE: backup_comms.enc                     │
│ PASSWORD: BACKDOOR                         │
│ HINT: Morse code translation               │
├────────────────────────────────────────────┤
│ ✓ CORRECT                                  │
│ ↓                                          │
│ CLUE REVEALED: Elara at AWS stress test    │
│ ↓                                          │
│ SUSPECT CLEARED: Elara Quinn ✓             │
└────────────────────────────────────────────┘
         ↓
    Level 7 Complete
         ↓
    [LEVEL 8 UNLOCKED - MEGA PUZZLE]"""

content = content.replace(level_4_block, levels_5_6_7)

mega_puzzle_old = """LEVEL 8 (MEGA PUZZLE)
┌────────────────────────────────────────────┐
│ META-PUZZLE CHALLENGE                      │
│ Extract key truth from evidence logs:      │
│ L1 Evidence → HOLOCAST                     │
│ L2 Evidence → MEDICAL                      │
│ L3 Evidence → PROXY                        │
│ L4 Evidence → LUNAR                        │
│ Combine: HOLOMEDIPROXLUNA                      │"""

mega_puzzle_new = """LEVEL 8 (MEGA PUZZLE)
┌────────────────────────────────────────────┐
│ META-PUZZLE CHALLENGE                      │
│ Extract key truth from evidence logs:      │
│ L1 Evidence → HOLOCAST                     │
│ L2 Evidence → MEDICAL                      │
│ L3 Evidence → PROXY                        │
│ L4 Evidence → LUNAR                        │
│ L5 Evidence → ELEVATOR                     │
│ L6 Evidence → LOADING                      │
│ L7 Evidence → CLOUD                        │
│ Combine: HOLOMEDIPROXLUNAELEVLOADCLOU      │"""

content = content.replace(mega_puzzle_old, mega_puzzle_new)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated GAME_STRUCTURE_AND_FLOWCHART.txt")
