## Project Overview

This project is a simple **Flappy Bird Clone** built using **Pygame**, a Python library designed for creating video games. In this game, the player controls a bird that must navigate through a series of pipes. The bird's movement is controlled by pressing the spacebar to make it "flap" upwards, while gravity constantly pulls it down. The game ends when the bird collides with a pipe or the ground, and the player's score is based on the number of pipes successfully passed.

---

## Features

- **Simple Graphics**: The bird, pipes, and background are rendered using basic images.
- **Sound Effects**: The game includes sound effects for flapping, scoring, and game over events.
- **Score Tracking**: The player's score increases by 1 for each pipe passed, and the final score is displayed when the game is over.
- **Game Over Screen**: After the bird hits a pipe or the ground, the game over screen shows the final score.

---

## Game Controls

- **Spacebar**: Press the spacebar to make the bird flap and move upwards.
- **Mouse Click**: Click the "Start" button on the main menu to begin the game.
- **Quit**: To quit the game, simply close the window.

---

## Requirements

- **Python 3.x**: Make sure Python 3 is installed on your system.
- **Pygame**: Install Pygame using the following command:

  ```bash
  pip install pygame
  ```

---

## Project Structure

```
.
├── assets
│   ├── bird.png            # Image for the bird
│   ├── pipe.png            # Image for the pipes
│   ├── background.png       # Image for the background
│   ├── flap.wav             # Sound effect for bird flapping
│   ├── score.wav            # Sound effect for scoring
│   ├── game_over.wav        # Sound effect for game over
├── main.py                  # Main game logic
└── README.md                # Project documentation
```

---

## How to Run the Game

1. Clone or download this repository to your local machine.
   
2. Navigate to the project directory and ensure all required assets (images, sounds) are located in the `assets` folder.

3. Run the game using the following command in your terminal:

   ```bash
   python main.py
   ```

4. The game will start with a main menu. Click on "Start" to begin the game.

---

## How to Play

- Press the **spacebar** to make the bird flap.
- Avoid hitting the pipes or the ground.
- The score increases by 1 for every pipe you successfully pass.
- The game ends when the bird hits a pipe or the ground.
- After the game over screen, your final score will be displayed.

---

## Future Improvements

- Add more challenging features, such as increasing pipe speed over time.
- Implement a high score system to keep track of the best score.
- Add animations to the bird and pipes for a more polished experience.

---

## Credits

This project was inspired by the original **Flappy Bird** game. The graphics and sounds are simplified, and all code was written in Python using the Pygame library.
***All assets used in this project was not owned by me. all credits goes to respected owners***
---

## License

This project is open-source and available for personal use. Feel free to modify and share it as per the terms of the [MIT License](https://opensource.org/licenses/MIT). 

---

Enjoy playing the game!
