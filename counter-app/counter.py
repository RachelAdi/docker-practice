import os
from datetime import datetime

# Directory for our data
data_dir = "/app/data"
os.makedirs(data_dir, exist_ok=True)

# Path to our counter file
counter_file = os.path.join(data_dir, "counter.txt")

# Read current count or start at 0
if os.path.exists(counter_file):
    with open(counter_file, "r") as f:
        lines = f.readlines()
        if lines:
            count = int(lines[0].strip())
        else:
            count = 0
else:
    count = 0

# Increment count
count += 1

# Save updated count and time
with open(counter_file, "w") as f:
    f.write(f"{count}\n")
    f.write(f"Last run: {datetime.now()}\n")

print(f"This container has been run {count} time(s).")
print(f"Last run at: {datetime.now()}")
