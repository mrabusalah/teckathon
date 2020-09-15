import os

raw_data = "raw_data"
angles = [-90, 90, 0]
for raw in os.listdir(raw_data):
    for state in os.listdir(f"{raw_data}/{raw}"):
        for media in os.listdir(f"{raw_data}/{raw}/{state}"):
            for angle in angles:
                command = f"python3 {raw}.py {raw_data}/{raw}/{state}/{media} {1 if state == 'focus' else 0} {angle}"
                print(command)
                os.system(command)
    