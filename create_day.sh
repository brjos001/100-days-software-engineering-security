#!/bin/bash

# Change this number for each new day
DAY=003

# Create the day folder and exercises folder
mkdir -p "day-$DAY/exercises"

# Create standard files
touch "day-$DAY/.gitignore" \
      "day-$DAY/JOURNAL.md" \
      "day-$DAY/README.md" \
      "day-$DAY/ROADMAP.md" \
      "day-$DAY/pyproject.toml"

echo "Created day-$DAY successfully!"

