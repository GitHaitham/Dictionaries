from datetime import datetime, timedelta

# ==========================================
# CALORIE TRACKER — LEVEL 4 (HARDER)
# ==========================================

logs = [
    ("Ali", "eat", 450, "2025-12-17 08:10"),
    ("Ali", "eat", 700, "2025-12-17 13:30"),
    ("Sara", "eat", 300, "2025-12-17 09:00"),
    ("Sara", "eat", 600, "2025-12-17 19:15"),
    ("Ali", "eat", 900, "2025-12-18 20:00"),
    ("Omar", "eat", 500, "2025-12-18 10:30"),
    ("Omar", "eat", 800, "2025-12-18 18:45"),
    ("Ali", "eat", 1200, "2025-12-21 12:00"),
    ("Sara", "eat", 1500, "2025-12-21 14:00"),
]

# Each log: (username, action, calories, timestamp)

# ------------------------------------------
# PART 1: BUILD USER LOGS
# ------------------------------------------
# Create user_logs
# Key   → username
# Value → list of (calories, datetime)

user_logs = {}
# loop over logs
# parse datetime
# append per user

for username, action, calories, timestamp in logs:
    parsed_datetime = datetime.strptime(timestamp, "%Y-%m-%d %H:%M")
    if not username in user_logs:
        user_logs[username] = [(calories, parsed_datetime)]
    else:
        user_logs[username].append((calories, parsed_datetime))

print(f"User Logs: {user_logs}")

# ------------------------------------------
# PART 2: TOTAL CALORIES PER USER
# ------------------------------------------
# Create total_calories
# Key   → username
# Value → total calories eaten

total_calories = {}
# loop over user_logs
# sum calories per user

for username, log in user_logs.items():
    if not username in total_calories:
        total_calories[username] = 0
    for entry in log:
        calories, timestamp = entry
        total_calories[username] += calories

print(f"Total Calories Per User: {total_calories}")

# ------------------------------------------
# PART 3: DAILY CALORIE SUMMARY
# ------------------------------------------
# Create daily_summary
# Key   → YYYY-MM-DD
# Value → dict { username → calories that day }

daily_summary = {}
# extract date from datetime
# sum calories per user per day

for username, action, calories, timestamp in logs:
    formatted_date = datetime.strptime(timestamp, "%Y-%m-%d %H:%M").strftime("%Y-%m-%d")
    if not formatted_date in daily_summary:
        daily_summary[formatted_date] = {}
    if not username in daily_summary[formatted_date]:
        daily_summary[formatted_date][username] = calories
    else:
        daily_summary[formatted_date][username] += calories

print(f"Daily Summary Per User: {daily_summary}")

# ------------------------------------------
# PART 4: WEEKLY CALORIE SUMMARY
# ------------------------------------------
# Create weekly_summary
# Key   → week_start_date (YYYY-MM-DD) of the week
# Value → dict { username → total calories that week }
#
# Hint: You can use datetime_object - timedelta(days=datetime_object.weekday())
# to get the Monday of the week

weekly_summary = {}
# loop through daily_summary
# accumulate per user per week

from datetime import datetime, timedelta

weekly_summary = {}

for day_str, users in daily_summary.items():
    # 1. Convert day string to datetime
    day_dt = datetime.strptime(day_str, "%Y-%m-%d")
    # 2. Find Monday of that week
    week_start_dt = day_dt - timedelta(days=day_dt.weekday())
    # 3. Convert Monday back to string
    week_start = week_start_dt.strftime("%Y-%m-%d")
    # 4. Ensure week exists
    if week_start not in weekly_summary:
        weekly_summary[week_start] = {}
    # 5. Accumulate per user
    for username, calories in users.items():
        if username not in weekly_summary[week_start]:
            weekly_summary[week_start][username] = calories
        else:
            weekly_summary[week_start][username] += calories

print(f"Weekly Summary: {weekly_summary}")

# ------------------------------------------
# PART 5: ALERTS
# ------------------------------------------
# Create alerts
# Include any user who had a day with more than 2000 calories OR
# a week with more than 10000 calories
#
# Structure: { username: {"days": [dates], "weeks": [week_start_dates]} }
# loop through daily_summary and weekly_summary
# detect exceedances




# loop through daily_summary
alerts = {}

# ---------- DAILY ALERTS ----------
for day, logs in daily_summary.items():
    for username, calories in logs.items():
        if calories > 1000:
            # Ensure the user exists and initialize sets if not
            alerts.setdefault(username, {"days": set(), "weeks": set()})
            # Add the day to the set (duplicates automatically ignored)
            alerts[username]["days"].add(day)

# ---------- WEEKLY ALERTS ----------
for week_start, logs in weekly_summary.items():
    for username, calories in logs.items():
        if calories > 1000:
            # Ensure the user exists and initialize sets if not
            alerts.setdefault(username, {"days": set(), "weeks": set()})
            # Add the week to the set (duplicates automatically ignored)
            alerts[username]["weeks"].add(week_start)

print(f"Alerts: {alerts}")

# ------------------------------------------
# PART 6: FINAL OUTPUT
# ------------------------------------------
# Print nicely:
# Daily summary per user
# Weekly summary per user
# Alerts for high intake

# loop through daily_summary
# loop through weekly_summary
# loop through alerts
