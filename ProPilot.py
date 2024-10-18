from e3dc import E3DC
from dotenv import load_dotenv
import os
load_dotenv()

# Verbindungsdaten zu Ihrem E3/DC-System
E3DC_USER = os.getenv("E3DC_USER")
E3DC_PASSWORD = os.getenv("E3DC_PASSWORD")
E3DC_IP = os.getenv("E3DC_IP")
E3DC_RSCP_PASSWORD = os.getenv("E3DC_RSCP_PASSWORD")

# E3DC-Objekt initialisieren
e3dc = E3DC(E3DC.CONNECT_LOCAL, username=E3DC_USER, password=E3DC_PASSWORD, ipAddress=E3DC_IP, key=E3DC_RSCP_PASSWORD)

# Aktuellen Batteriestatus abfragen
try:
    battery_status = e3dc.get_battery_soc()  # SoC = State of Charge
    print(f"Aktueller Batterieladestand: {battery_status}%")
except Exception as e:
    print(f"Fehler beim Abrufen des Batteriestatus: {e}")
