1) Sport Calculators CLI:
A simple command-line Python application with sport-related calculators and a user profile stored locally in JSON.

2) Description:
Sport Calculators CLI is my first Python portfolio project.
The app allows the user to create a personal profile and use saved data for basic sport-related calculations.

The user profile stores information such as name, age, weight and height.
Thanks to this, the user does not need to enter the same data every time when using calculators like BMI or max heart rate.

3) Features:
- Create and edit user profile
- Save user profile to a JSON file
- Load user profile from JSON
- Show saved user profile
- BMI calculator
- Running pace calculator
- Max heart rate calculator
- Heart rate zones calculator
- Input validation
- Unit tests with pytest

4) Tech stack:
- Python
- JSON
- pathlib
- pytest
- Git
- GitHub

5) Project structure:

sport-calculators-cli/
├── data/
│   └── .gitkeep
├── src/
│   ├── __init__.py
│   ├── calculators.py
│   ├── input_utils.py
│   ├── main.py
│   └── user_storage.py
├── tests/
│   └── test_calculator.py
├── .gitignore
├── README.md
└── requirements.txt

6) How to run:

Clone the repository:

git clone https://github.com/kijekk64/sport_calculator_cli.git
cd sport-calculator-cli

Install dependencies:

python -m pip install -r requirements.txt

Run the app:

python src/main.py
How to run tests
python -m pytest

Example menu:

===== Sport Calculators CLI =====
1. Create/Edit Profile
2. Show Profile
3. BMI Calculator
4. Running Pace Calculator
5. Maximum Heart Rate And Heart Rate Zones
6. Exit

Example user profile:

The app stores user data locally in a JSON file:

{
    "name": "Kacper",
    "age": 17,
    "weight": 75.0,
    "height": 1.8
}

The user_profile.json file is ignored by Git because it contains private user data.

7) Future improvements:

- Add calculation history
- Add option to delete user profile
- Add export to CSV
- Add more sport calculators
- Add better terminal UI
- Add tests for JSON profile storage
- Add Polish / English language selection

8) Status

Finished as my first Python portfolio project.