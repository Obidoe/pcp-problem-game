# PCP Problem Game - Simple Explanation

## 🎯 HOW THE GAME WORKS (Not About Matching 2 Dominoes!)

### The Goal
**Arrange ALL dominoes left-to-right so that the ENTIRE top string matches the ENTIRE bottom string.**

It's NOT about matching 2 dominoes at a time. It's about building a long sequence!

---

## 📝 Step-by-Step Example

### Starting State (Empty Working Area)
```
Domino Set (all highlighted in YELLOW - any can start):
A: Top=[BLUE, BLUE] Bottom=[BLUE, BLUE, BLUE]
B: Top=[RED, GREEN] Bottom=[RED]
C: Top=[BLUE, BLUE, BLUE] Bottom=[GREEN]
D: Top=[RED] Bottom=[BLUE, BLUE]
```

### Step 1: Drag Domino A
```
Working Area: [A]

Top String:    BLUE, BLUE
Bottom String: BLUE, BLUE, BLUE

Match? NO (2 vs 3 colors)

What can go next? Look for dominoes where TOP = [BLUE, BLUE, BLUE]
→ Domino C is HIGHLIGHTED! ✨
```

### Step 2: Drag Domino C
```
Working Area: [A, C]

Top String:    BLUE, BLUE + BLUE, BLUE, BLUE = BLUE, BLUE, BLUE, BLUE, BLUE (5 colors)
Bottom String: BLUE, BLUE, BLUE + GREEN = BLUE, BLUE, BLUE, GREEN (4 colors)

Match? NO (different lengths and last color is different)

What can go next? Look for dominoes where TOP = [BLUE, BLUE, BLUE, GREEN]
→ NO matches! Nothing highlighted! 

This sequence is a DEAD END - click Clear and try a different combination!
```

### Better Approach: Start with Domino D
```
Working Area: [D]

Top String:    RED
Bottom String: BLUE, BLUE

What can go next? Look for dominoes where TOP = [BLUE, BLUE]
→ Domino A is HIGHLIGHTED! ✨
```

---

## 🎨 What You're Seeing in the Game

### Top Area (Domino Set)
- 10 random dominoes
- **YELLOW GLOWING BORDER** = can be placed next
- **NO BORDER** = can't be placed next (would break the sequence)

### Middle Area (Working Area)
- Your sequence being built (left to right)
- Automatically arranges dominoes
- Drag dominoes OUT to remove them

### Bottom Display
- **Top:** Shows the combined top sequence (all top halves)
- **Bottom:** Shows the combined bottom sequence (all bottom halves)
- **"No match yet..."** = Keep trying!
- **"✓ MATCH!"** = YOU WON! 🎉

---

## 🤔 Why Is Nothing Highlighted Sometimes?

This is NORMAL and actually demonstrates why PCP is undecidable!

**When no dominoes are highlighted**, it means:
- Your current bottom sequence doesn't match ANY domino's top
- You've reached a DEAD END
- This sequence can't lead to a solution
- Click "Clear" and try a different order!

---

## 🎮 Tips for Playing

1. **Start simple** - Try each domino as a starting piece
2. **Watch the highlights** - Only highlighted dominoes can continue the sequence
3. **Dead ends are OK** - Part of the challenge!
4. **Some sets might be unsolvable** - That's the nature of PCP!
5. **Click "New Game"** if you want a fresh set of dominoes

---

## 💡 For Your Presentation

### Key Points to Explain:
1. **"The goal is to make the ENTIRE top and bottom strings match"**
2. **"Yellow borders show which dominoes CAN be placed next"**
3. **"Sometimes there's no valid next move - that's a dead end!"**
4. **"Some domino sets have NO solution at all - that's why PCP is undecidable"**
5. **"This makes a great game because it's genuinely challenging without being artificially difficult"**

### Demo Strategy:
1. Start with empty working area (all highlighted)
2. Drag one domino - show how highlights change
3. Continue building - show the sequences growing
4. Hit a dead end - explain why nothing is highlighted
5. Click Clear and try different order
6. If you get lucky and find a match - celebrate! 🎉

Good luck! 🚀

