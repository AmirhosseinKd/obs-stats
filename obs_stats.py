from obswebsocket import obsws, requests
import datetime
import json
import sys
import os

# --- LOAD CONFIGURATION ---
try:
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(script_dir, 'config.json')

    with open(config_path, 'r') as f:
        config = json.load(f)
        
    host = config.get('host', 'localhost')
    port = config.get('port', 4455)
    password = config.get('password')
    
    if not password:
        raise ValueError("password not found in config.json")

except FileNotFoundError:
    print(f"Error: config.json not found at {config_path}")
    sys.exit(1)
except Exception as e:
    print(f"Config Error: {e}")
    sys.exit(1)
# ---------------------

try:
    ws = obsws(host, port, password)
    ws.connect()

    # Get Current Scene Name
    scene_response = ws.call(requests.GetCurrentProgramScene())
    scene_name = scene_response.getSceneName()

    # Get Recording Status & Time
    record_response = ws.call(requests.GetRecordStatus())
    is_recording = record_response.getOutputActive()
    rec_time_ms = record_response.getOutputDuration()

    # Format the Time (Milliseconds -> HH:MM:SS)
    if is_recording:
        rec_time = str(datetime.timedelta(milliseconds=rec_time_ms)).split('.')[0]
        # Remove "0:" if it's less than an hour to save space (optional)
        if rec_time.startswith("0:"):
            rec_time = rec_time[2:]
        status_icon = "🔴" # Red circle for recording
    else:
        rec_time = "00:00"
        status_icon = "zz" # Idle text

    # Final Output to Panel
    print(f"{status_icon} {rec_time} | {scene_name}")

    ws.disconnect()

except Exception as e:
    # If OBS is closed, print nothing or a generic message
    print("OBS Offline")