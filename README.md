# 🎮 AI Tic-Tac-Toe Game using the Minimax Algorithm

**Author:** Aiden Cary  
**Course:** AI with Prof. Stein  

---

## 🧠 Overview

This project implements a **Tic-Tac-Toe game** where the player competes against an **unbeatable AI** that uses the **Minimax algorithm** for decision-making.  

Tic-Tac-Toe is a **zero-sum**, **perfect-information** game with a **small state space**, making it ideal for demonstrating how game tree search algorithms work.  

The maximum depth of the game tree is **9 plies** (one for each cell on the 3×3 board).

---

## ⚙️ Features

- Play as **X** or **O**
- AI uses the **Minimax algorithm** to guarantee an optimal move every turn
- **Dynamic menu system** for playing, clearing the terminal, and exiting
- **Win tracking** for both user and AI
- **Fully text-based** interface
- Optional **AI thinking delay** for realism

---

## 🧩 How It Works

### 🎯 Minimax Algorithm
The **Minimax algorithm** explores all possible game states recursively to determine the best possible move for the AI.

- **Maximizing player (AI)** tries to maximize its score.
- **Minimizing player (User)** tries to minimize the AI’s score.
- Base cases handle terminal states:
  - Win for AI → `10 - depth`
  - Win for Player → `depth - 10`
  - Draw → `0`

This ensures that:
- The AI **never loses** (optimal play)
- The game can end in a **draw** if the user also plays optimally

---

## 🕹️ Game Controls

1. Run the Python script:
   ```bash
   python tic_tac_toe_minimax.py
