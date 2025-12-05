#!/usr/bin/env python3
from obswebsocket import obsws, requests
import datetime

# --- CONFIGURATION ---
host = "localhost"
port = 4455
password = "oLb02O2uTzpcUcgE" # Put your OBS password here
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