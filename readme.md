# FrozenLake 8x8 AI Trainer


Welcome to the **FrozenLake 8x8 AI Trainer**! This project teaches a computer how to play the FrozenLake game using a technique called **Q-learning**. The goal is to help the computer learn how to navigate an 8x8 icy grid, avoid holes, and reach the goal.


---


## What is FrozenLake?


FrozenLake is a game where:
- You start at the top-left corner of an 8x8 grid.
- You need to reach the bottom-right corner (the goal).
- The ice is slippery, so sometimes you might slide in a direction you didn’t intend!
- If you step into a hole, you lose. If you reach the goal, you win!


---


## How Does the AI Learn?


The AI learns by playing the game over and over again. Here’s how it works:


1. **Q-learning**:
   - The AI keeps a "memory" (called a Q-table) of which moves are good or bad.
   - It tries random moves at first (exploration) but slowly starts choosing the best moves based on its memory (exploitation).


2. **Training**:
   - During training, the AI plays the game many times (e.g., 15,000 episodes).
   - It updates its Q-table after every move to remember what works and what doesn’t.


3. **Testing**:
   - After training, the AI uses its Q-table to play the game without making random moves.
   - You can watch it play and see how well it performs!


---


## How to Use This Code


### Prerequisites
Make sure you have Python installed. You’ll also need to install the following libraries:
```bash
pip install gymnasium numpy matplotlib
```


---


### Running the Code


1. **Train the AI**:
   - Uncomment the `play_game(15000)` line in the `if __name__ == '__main__':` block.
   - This will train the AI for 15,000 episodes and save its Q-table to a file (`frozen_lake8x8.pkl`).


2. **Test the AI**:
   - After training, comment out the training line and uncomment the `play_game(1, is_training=False, render=True)` line.
   - This will let the AI play the game using its saved Q-table, and you can watch it in action!


3. **View the Results**:
   - After training, a graph (`frozen_lake8x8.png`) will be saved. It shows how often the AI won over time.
   - If the line goes up, it means the AI is getting better!


---


## Code Explanation


Here’s a quick breakdown of the code:


1. **Setup**:
   - The game is created using `gym.make('FrozenLake-v1')`.
   - The Q-table is initialized as a 64x4 array (64 states x 4 actions).


2. **Training**:
   - The AI explores the game by taking random moves and updates its Q-table using the Q-learning formula.
   - Over time, it reduces exploration (epsilon) and relies more on its memory.


3. **Testing**:
   - The AI uses its Q-table to choose the best moves and plays the game.


4. **Graph**:
   - A graph is created to show the AI’s progress over time.


5. **Save/Load**:
   - The Q-table is saved to a file (`frozen_lake8x8.pkl`) after training and loaded during testing.


---


## Key Parameters


- **Learning Rate (alpha)**: How quickly the AI learns (default: 0.9).
- **Discount Factor (gamma)**: How much the AI cares about future rewards (default: 0.9).
- **Epsilon**: How often the AI explores (tries random moves). It starts at 1 (100% random) and decays over time.
- **Epsilon Decay Rate**: How quickly the AI stops exploring (default: 0.0001).


---


## Example Output


After training, you’ll see:
- A graph showing the AI’s win rate over time.
- The AI playing the game in real-time (if `render=True`).


---


## Have Fun!


Try tweaking the parameters (e.g., learning rate, epsilon decay) to see how they affect the AI’s performance. You can also make the game easier by setting `is_slippery=False` and see how the AI learns faster.


Let me know if you have any questions or need help! 😊


---


 Enjoy watching your AI conquer FrozenLake! 🎮❄️ 


---





