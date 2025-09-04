# 🎯 Number Guessing Game

A modern, feature-rich number guessing game built with Python and Tkinter, featuring a sleek dark theme interface, persistent statistics, and multiple difficulty levels.

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🌟 Features

### 🎮 Gameplay
- **Smart Number Generation**: Random numbers between 1-100
- **Multiple Difficulty Levels**: Easy (10 attempts), Medium (7 attempts), Hard (5 attempts)
- **Real-time Feedback**: "Too high" or "too low" hints
- **Input Validation**: Prevents invalid inputs and out-of-range guesses
- **Keyboard Support**: Press Enter to submit guesses

### 📊 Statistics System
- **Persistent Data Storage**: Game statistics saved in JSON format
- **Comprehensive Tracking**: Games played, won, win rates, and best scores
- **Difficulty-Specific Stats**: Separate statistics for each difficulty level
- **Best Game Tracking**: Records your best performance (fewest attempts)
- **Average Performance**: Calculates average attempts for won games

### 🎨 Modern Interface
- **GitHub Dark Theme**: Professional dark color scheme (#0D1117)
- **Responsive Design**: Centered windows with optimal sizing
- **Emoji Icons**: Visual feedback with relevant emojis
- **Intuitive Navigation**: Easy switching between game states
- **Error Handling**: User-friendly error messages and warnings

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Tkinter (usually included with Python)

### Installation

1. **Clone or download the repository**:
```bash
git clone https://github.com/yourusername/number-guessing-game.git
cd number-guessing-game
```

2. **Run the game**:
```bash
python number_guessing_game.py
```

### First Launch
- The game will create a `game_stats.json` file automatically
- No additional configuration required
- Statistics are saved automatically after each game

## 🎯 How to Play

1. **Launch the Game**: Run the Python script
2. **Choose Difficulty**: 
   - 🟢 **Easy**: 10 attempts (great for beginners)
   - 🟡 **Medium**: 7 attempts (balanced challenge)
   - 🔴 **Hard**: 5 attempts (expert mode)
3. **Make Your Guess**: Enter a number between 1-100
4. **Follow the Hints**: 
   - 📈 "Too low" means guess higher
   - 📉 "Too high" means guess lower
5. **Win Condition**: Guess the exact number to win!
6. **View Statistics**: Check your progress and best scores

## 🏆 Scoring System

### Performance Metrics
- **Games Played**: Total number of games started
- **Games Won**: Successfully guessed numbers
- **Win Rate**: Percentage of games won
- **Best Game**: Fewest attempts used to win (overall)
- **Average Attempts**: Mean attempts for won games
- **Difficulty Best**: Best score for each difficulty level

### Strategy Tips
- **Binary Search Method**: Start with 50, then adjust by half each time
- **Range Tracking**: Keep mental note of eliminated ranges
- **Optimal Play**: Mathematically, any number can be found in 7 guesses max

## 🛠️ Technical Details

### Architecture
```
NumberGuessingGame/
├── NumberGuessingGame (Main Class)
│   ├── setup_main_window()
│   ├── show_difficulty_selection()
│   ├── setup_game()
│   ├── check_guess()
│   └── show_detailed_stats()
└── Stats (Statistics Class)
    ├── load_stats()
    ├── save_stats()
    ├── update_stats()
    └── get_stats()
```

### Dependencies
```python
import tkinter as tk           # GUI framework
import random                  # Number generation
from tkinter import messagebox, ttk  # UI components
import json                    # Data persistence
import os                      # File system operations
import time                    # Future enhancements
```

### Data Structure (game_stats.json)
```json
{
  "games_played": 15,
  "games_won": 12,
  "total_attempts": 45,
  "best_game": 3,
  "difficulty_stats": {
    "easy": {
      "played": 8,
      "won": 7,
      "best": 4
    },
    "medium": {
      "played": 5,
      "won": 4,
      "best": 3
    },
    "hard": {
      "played": 2,
      "won": 1,
      "best": 5
    }
  }
}
```

## 🔧 Customization

### Colors (GitHub Dark Theme)
- **Background**: `#0D1117` (Dark gray)
- **Primary Text**: `#F0F6FC` (Light gray)
- **Secondary Text**: `#C9D1D9` (Medium gray)
- **Accent Blue**: `#58A6FF` (GitHub blue)
- **Success Green**: `#238636` (GitHub green)
- **Warning Orange**: `#FB8500` (Orange)
- **Error Red**: `#DA3633` (GitHub red)

### Font Configuration
- **Title**: Helvetica, 32pt, Bold
- **Buttons**: Helvetica, 14-16pt, Bold
- **Body Text**: Helvetica, 12-14pt, Regular

### Window Dimensions
- **Main Window**: 800x600 pixels
- **Auto-centered**: Calculated based on screen resolution

## 📁 File Structure
```
number-guessing-game/
├── number_guessing_game.py    # Main game file
├── game_stats.json           # Statistics data (auto-generated)
├── README.md                 # This file
└── requirements.txt          # Python dependencies (if needed)
```

## 🐛 Error Handling

### Robust Input Validation
- **Non-numeric Input**: Shows error dialog, clears input
- **Out of Range**: Warning for numbers outside 1-100
- **Empty Input**: Handles gracefully without crashing

### File System Safety
- **Missing Stats File**: Creates new file with defaults
- **Corrupted JSON**: Falls back to default statistics
- **Permission Errors**: Continues running, shows console warnings

## 🚧 Future Enhancements

### Planned Features
- [ ] **Hint System**: Optional hints for struggling players
- [ ] **Timer Mode**: Speed challenges with time limits
- [ ] **Multiplayer**: Local two-player competitions
- [ ] **Custom Ranges**: Allow different number ranges (1-50, 1-1000)
- [ ] **Sound Effects**: Audio feedback for actions
- [ ] **Themes**: Multiple color schemes and themes
- [ ] **Export Stats**: Save statistics to CSV/Excel
- [ ] **Achievements**: Unlock badges for milestones

### Technical Improvements
- [ ] **Config File**: External configuration for customization
- [ ] **Logging System**: Debug logs for troubleshooting
- [ ] **Unit Tests**: Comprehensive test coverage
- [ ] **Package Structure**: Proper Python package organization

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Tkinter Community**: For extensive GUI documentation
- **GitHub Design System**: Color scheme inspiration
- **Python Community**: Best practices and code standards

## 📞 Support

If you encounter any issues or have suggestions:

1. **Check Issues**: Browse existing GitHub issues
2. **Create New Issue**: Describe the problem with steps to reproduce
3. **Feature Requests**: Suggest new features or improvements

---

**Happy Gaming! 🎮**

*Made with ❤️ and Python*
