import os

# Get environment variables with default values
name = os.environ.get("NAME", "World")
greeting = os.environ.get("GREETING", "Hello")

print(f"{greeting}, {name}!")
