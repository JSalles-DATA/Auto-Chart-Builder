"""
generate_data.py
----------------
Generates a sample CSV dataset for testing the AutoChart Builder.
"""

import os
import pandas as pd
import random
from datetime import datetime, timedelta

# -----------------------
# Folder & file setup
# -----------------------
DATA_DIR = "data"
FILE_PATH = os.path.join(DATA_DIR, "user_data.csv")
os.makedirs(DATA_DIR, exist_ok=True)

# -----------------------
# Generate sample data
# -----------------------
num_rows = 100
start_date = datetime.today() - timedelta(days=num_rows)

data = {
    "date": [(start_date + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(num_rows)],
    "mood_score": [random.randint(0, 10) for _ in range(num_rows)],
    "sleep_hours": [round(random.uniform(4, 9), 1) for _ in range(num_rows)],
    "exercise_minutes": [random.randint(0, 120) for _ in range(num_rows)],
    "stress_level": [random.randint(0, 10) for _ in range(num_rows)],
    "notes": [random.choice(["Good day", "Average day", "Tired", "Energetic", "Stressed"]) for _ in range(num_rows)]
}

df = pd.DataFrame(data)

# -----------------------
# Save CSV
# -----------------------
df.to_csv(FILE_PATH, index=False)
print(f"✅ Sample data generated at {FILE_PATH}")
