# 🪨📄✂️ Rock Paper Scissors Game  

A simple Python **console-based** game that lets you play **Rock, Paper, Scissors** against the computer.  
Each round, the computer makes a random choice, and the winner is determined by the classic rules of the game.  

---

## 🎮 How to Play  

1. **Make sure you have installed the dependencies by running:**
    ```bash
    pip install -r requirements.txt
    ```

2. **Run the Python script** in your terminal or code editor:  
   ```bash
   python rock_paper_scissors.py
   ```
3. **Choose** between **Rock**, **Paper**, or **Scissors** when prompted.  
4. The **computer will randomly choose** its option.  
5. The game will display:
   - Your choice  
   - The computer’s choice  
   - The result (Win 🏆, Lose 😞, or Tie ⚖️)  
6. After each round, you’ll be asked:  
   ```
   Do you want to play another round? (yes/no)
   ```
   - Type **yes** to continue playing.  
   - Type **no** to quit the game.  

---

## ⚙️ Requirements  

- **Python 3.x**  
- No external libraries needed — only the built-in `random` module is used.  

---

## 🧠 Game Logic Summary  

| Your Choice | Computer Choice | Result |
|--------------|-----------------|--------|
| Rock | Scissors | 🏆 You Win |
| Rock | Paper | 😞 You Lose |
| Paper | Rock | 🏆 You Win |
| Paper | Scissors | 😞 You Lose |
| Scissors | Paper | 🏆 You Win |
| Scissors | Rock | 😞 You Lose |
| Same | Same | ⚖️ It’s a Tie |

---

## 💡 Example Gameplay  

```bash
Choose between Rock,Paper or Scissors: rock
Person_choice: Rock
Computer_choice: Scissors
You won...hureeee 🏆🎉

Do you want to play another round?(yes/no): yes
Choose between Rock,Paper or Scissors: paper
Person_choice: Paper
Computer_choice: Scissors
You lost 😞
```

---

## Plans
**Soon planning to integrate the game with a UI and backend with FASTAPI to make interactive as possible not just to programmers but to everyone.**

---

## 👨‍💻 Author  

**Griffin Ngotho**  
📍 Nairobi, Kenya  
📧 [griffngotho@gmail.com](mailto:griffngotho@gmail.com)<br>
🧰 [LinkedIn Profile](https://www.linkedin.com/in/griffin-ngotho-a4048132a/)

---

## 🏁 License  

This project is **open-source** and free to use for learning purposes.  
