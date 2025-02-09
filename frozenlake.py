import gymnasium as gym  # This is the library for the FrozenLake game
import numpy as np       # This helps us work with numbers and arrays
import matplotlib.pyplot as plt  # This helps us draw graphs
import pickle            # This helps us save and load the computer's memory

def play_game(episodes, is_training=True, render=False):
    # Set up the FrozenLake game
    env = gym.make('FrozenLake-v1', map_name="8x8", is_slippery=True, render_mode='human' if render else None)

    # If the computer is learning, start with a blank memory
    if is_training:
        q = np.zeros((env.observation_space.n, env.action_space.n))  # 64 states x 4 actions
    else:
        # If not learning, load the computer's memory from a file
        with open('frozen_lake8x8.pkl', 'rb') as f:
            q = pickle.load(f)

    # Set up learning rules
    learning_rate = 0.9  # How fast the computer learns
    discount_factor = 0.9  # How much the computer cares about future rewards
    epsilon = 1  # How often the computer explores (tries random moves)
    epsilon_decay = 0.0001  # How quickly the computer stops exploring
    rng = np.random.default_rng()  # A random number generator

    # Keep track of rewards (1 if the computer wins, 0 if it loses)
    rewards = np.zeros(episodes)

    # Play the game for the number of episodes
    for episode in range(episodes):
        state = env.reset()[0]  # Start at the beginning of the game
        done = False  # The game isn't over yet

        while not done:
            # Decide what action to take
            if is_training and rng.random() < epsilon:
                action = env.action_space.sample()  # Try a random move
            else:
                action = np.argmax(q[state, :])  # Choose the best move from memory

            # Take the action and see what happens
            new_state, reward, terminated, truncated, _ = env.step(action)

            # If the computer is learning, update its memory
            if is_training:
                q[state, action] = q[state, action] + learning_rate * (
                    reward + discount_factor * np.max(q[new_state, :]) - q[state, action]
                )

            state = new_state  # Move to the new state
            done = terminated or truncated  # Check if the game is over

        # Slowly reduce exploration (epsilon) over time
        epsilon = max(epsilon - epsilon_decay, 0)

        # If the computer wins, record it
        if reward == 1:
            rewards[episode] = 1

    # Close the game
    env.close()

    # Draw a graph of how well the computer is doing
    sum_rewards = np.zeros(episodes)
    for t in range(episodes):
        sum_rewards[t] = np.sum(rewards[max(0, t-100):(t+1)])
    plt.plot(sum_rewards)
    plt.savefig('frozen_lake8x8.png')

    # Save the computer's memory if it was learning
    if is_training:
        with open("frozen_lake8x8.pkl", "wb") as f:
            pickle.dump(q, f)

# Run the game
if __name__ == '__main__':
    # Train the computer (uncomment this to train)
    # play_game(15000)

    # Let the computer play using its memory (no training)
    play_game(1, is_training=False, render=True)