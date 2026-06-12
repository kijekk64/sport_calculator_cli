import json
from pathlib import Path

profile_path = Path('data')/'user_profile.json'

def save_profile(profile):

    profile_path.parent.mkdir(exist_ok= True)

    with open(profile_path, 'w', encoding='utf-8') as file:
        json.dump(profile, file, indent=4, ensure_ascii=False)

def load_profile():
    if not profile_path.exists():
        return None
    with open(profile_path, 'r', encoding= 'utf-8') as file:
        return json.load(file)