from datetime import datetime, timedelta

# ==========================================
# CALORIE TRACKER — LEVEL 4 (HARDER)
# ==========================================

logs = [
    ("Ali",  "eat",  450, "2025-12-17 08:10"),
    ("Ali",  "eat",  700, "2025-12-17 13:30"),
    ("Sara", "eat",  300, "2025-12-17 09:00"),
    ("Sara", "eat",  600, "2025-12-17 19:15"),
    ("Ali",  "eat",  900, "2025-12-18 20:00"),
    ("Omar", "eat",  500, "2025-12-18 10:30"),
    ("Omar", "eat",  800, "2025-12-18 18:45"),
    ("Ali",  "eat",  1200,"2025-12-21 12:00"),
    ("Sara", "eat",  1500,"2025-12-21 14:00"),
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
    parsed_datetime=datetime.strptime(timestamp, "%Y-%m-%d %H:%M")
    if not username in user_logs:
        user_logs[username]=[(calories, parsed_datetime)]
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
        total_calories[username]=0
    for entry in log:
        calories, timestamp = entry
        total_calories[username]+=calories

print(f"Total Calories Per User: {total_calories}")

# ------------------------------------------
# PART 3: DAILY CALORIE SUMMARY
# ------------------------------------------
# Create daily_summary
# Key   → YYYY-MM-DD
# Value → dict { username → calories that day }

# daily_summary = {}
# extract date from datetime
# sum calories per user per day


# ------------------------------------------
# PART 4: WEEKLY CALORIE SUMMARY
# ------------------------------------------
# Create weekly_summary
# Key   → week_start_date (YYYY-MM-DD) of the week
# Value → dict { username → total calories that week }
#
# Hint: You can use datetime_object - timedelta(days=datetime_object.weekday())
# to get the Monday of the week

# weekly_summary = {}
# loop through daily_summary
# accumulate per user per week


# ------------------------------------------
# PART 5: ALERTS
# ------------------------------------------
# Create alerts
# Include any user who had a day with more than 2000 calories OR
# a week with more than 10000 calories
#
# Structure: { username: {"days": [dates], "weeks": [week_start_dates]} }

# alerts = {}
# loop through daily_summary and weekly_summary
# detect exceedances


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

