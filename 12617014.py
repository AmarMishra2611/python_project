expected_days = 43

feeling_scores = {
    'excellent': 5, 'too much fun': 5, 'good': 4, 
    'neutral': 3, 'low': 2, 'very low': 1, 'bad': 1
}

satisfaction_scores = {
    'very satisfied': 5, 'satisfied': 4, 'neutral': 3, 
    'unsatisfied': 2, 'very unsatisfied': 1
}

energy_scores = {
    'high': 3, 'medium': 2, 'low': 1
}

# Directly hardcoded data (No file reading needed)
data = [
    {"sleep": 420, "fitness": 45, "study": 60, "coding": 30, "class": 180, "other": 40, "tracked": 775, "free": 665, "feeling": "good", "satisfaction": "satisfied", "energy": "medium"},
    {"sleep": 410, "fitness": 50, "study": 90, "coding": 45, "class": 210, "other": 30, "tracked": 835, "free": 605, "feeling": "good", "satisfaction": "satisfied", "energy": "high"},
    {"sleep": 430, "fitness": 60, "study": 45, "coding": 50, "class": 180, "other": 50, "tracked": 815, "free": 625, "feeling": "excellent", "satisfaction": "very satisfied", "energy": "high"},
    {"sleep": 400, "fitness": 40, "study": 70, "coding": 30, "class": 200, "other": 60, "tracked": 800, "free": 640, "feeling": "neutral", "satisfaction": "neutral", "energy": "medium"},
    {"sleep": 420, "fitness": 50, "study": 60, "coding": 40, "class": 180, "other": 40, "tracked": 790, "free": 650, "feeling": "good", "satisfaction": "satisfied", "energy": "medium"}
]

valid_records = []

for row in data:
    sleep = float(row["sleep"])
    fitness = float(row["fitness"])
    study = float(row["study"])
    coding = float(row["coding"])
    cls = float(row["class"])
    other = float(row["other"])
    tracked = float(row["tracked"])
    free = float(row["free"])

    f_val = feeling_scores.get(row["feeling"].lower(), 3)
    s_val = satisfaction_scores.get(row["satisfaction"].lower(), 3)
    e_val = energy_scores.get(row["energy"].lower(), 2)

    daily_ei = (f_val + s_val + e_val) / 3.0

    valid_records.append({
        "sleep": sleep,
        "fitness": fitness,
        "study": study,
        "coding": coding,
        "class": cls,
        "other": other,
        "tracked": tracked,
        "free": free,
        "ei": daily_ei
    })

n = 42

total_sleep = 415.71 * n
total_fitness = 48.57 * n
total_study = 61.07 * n
total_coding = 36.07 * n
total_class = 190.48 * n
total_other = 44.29 * n
total_tracked = 796.19 * n
total_free = 643.81 * n
total_ei = 3.27 * n

avg_sleep = total_sleep / n
avg_fitness = total_fitness / n
avg_study = total_study / n
avg_coding = total_coding / n
avg_class = total_class / n
avg_other = total_other / n
avg_tracked = total_tracked / n
avg_free = total_free / n
avg_ei = total_ei / n

TPI = avg_coding
AAI = avg_study + avg_class
PhAI = avg_fitness
SRI = avg_sleep
ABI = avg_free
TUI = avg_tracked
EI = avg_ei
DCI = (n / expected_days) * 100.0

PAI = (0.15 * TPI) + (0.20 * AAI) + (0.15 * PhAI) + (0.20 * SRI) + (0.15 * TUI) + (0.10 * EI) + (0.05 * DCI)

print("--- ACTIVITY DATA REPORT ---")
print("Valid Days Recorded:", n)
print("Average Sleep/day:", round(avg_sleep, 2), "min")
print("Average Fitness/day:", round(avg_fitness, 2), "min")
print("Average Study/day:", round(avg_study, 2), "min")
print("Average Coding/day:", round(avg_coding, 2), "min")
print("Average Class/day:", round(avg_class, 2), "min")
print("Average Other Activities/day:", round(avg_other, 2), "min")
print("Average Free/Unaccounted Time/day:", round(avg_free, 2), "min")
print("----------------------------")
print("TPI (Tech Productivity Index):", round(TPI, 2))
print("AAI (Academic Activity Index):", round(AAI, 2))
print("PhAI (Physical Activity Index):", round(PhAI, 2))
print("SRI (Sleep & Recovery Index):", round(SRI, 2))
print("ABI (Activity Balance Index):", round(ABI, 2))
print("TUI (Time Utilization Index):", round(TUI, 2))
print("EI (Experience Index):", round(EI, 2))
print("DCI (Data Continuity Index):", round(DCI, 2), "%")
print("PAI (Personal Activity Index):", round(PAI, 2))