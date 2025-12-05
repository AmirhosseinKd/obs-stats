# **OBS Stats Display**

This simple Python script connects to your OBS Studio instance via WebSocket and prints the current status, including:

* **Recording Status:** (🔴 Recording / ⏸️ Paused / zz Idle)  
* **Recording Timer:** (HH:MM:SS)  
* **Current Scene Name**

It is designed to be used with status bars (like Polybar, i3blocks, or tmux) or simply as a CLI tool.

## **Prerequisites**

1. **OBS Studio** installed.  
2. **OBS WebSocket Server** enabled:  
   * Open OBS.  
   * Go to Tools \-\> WebSocket Server Settings.  
   * Check Enable WebSocket server.  
   * Note your **Port** (default 4455\) and **Server Password**.

## **Installation**

1. Clone this repository or download the files.  
2. Install the required Python packages:  
   pip install \-r requirements.txt

## **Configuration**

For security reasons, your actual credentials are not stored in the code.

1. Rename the example configuration file:  
   * Rename config.example.json to config.json.  
2. Open config.json and enter your details:  
   {  
       "obs\_host": "localhost",  
       "obs\_port": 4455,  
       "obs\_password": "YOUR\_OBS\_PASSWORD\_HERE"  
   }

**Note:** The config.json file is ignored by Git to prevent your password from being uploaded. Always keep your secrets local\!

## **Usage**

Run the script using Python:

python obs\_stats.py

### **Output Examples**

* **Idle:** zz 00:00 | Scene Name  
* **Recording:** 🔴 01:23 | Gameplay
* **Paused:** ⏸️ 01:23 | Gameplay
## **Troubleshooting**

* **"OBS Offline":** Ensure OBS is running and the WebSocket server is enabled.  
* **"Authentication Failed":** Double-check the password in config.json.  
* **"config.json not found":** Ensure you have renamed the example file and it is in the same folder as the script.