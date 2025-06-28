import platform, socket, time
from core.sheets_api import append_to_sheet

def log_bot(bot_id):
    data = [
        bot_id,
        socket.gethostname(),
        platform.system(),
        socket.gethostbyname(socket.gethostname()),
        time.ctime()
    ]
    append_to_sheet("Bots", data)

