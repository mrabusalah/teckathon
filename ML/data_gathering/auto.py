import os

raw_data = "raw_data"
for raw in os.listdir(raw_data):
    for state in os.listdir(f"{raw_data}/{raw}"):
        for media in os.listdir(f"{raw_data}/{raw}/{state}"):
            command = f"python3 {raw}.py {raw_data}/{raw}/{state}/{media} {1 if state == 'focus' else 0}"
            print(command)
            os.system(command)
    