import whois, time
from core.sheets_api import append_to_sheet

def run_recon(bot_id, domain):
    try:
        result = whois.whois(domain)
        append_to_sheet("Recon", [
            bot_id, domain, "whois", str(result)[:500], time.ctime()
        ])
    except Exception as e:
        append_to_sheet("Recon", [
            bot_id, domain, "error", str(e), time.ctime()
        ])
