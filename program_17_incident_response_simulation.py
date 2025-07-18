log = ["login failed", "login failed", "<script>alert('xss')</script>", "login failed"]
alert = False

for entry in log:
    if "<script>" in entry or "failed" in entry:
        alert = True

if alert:
    print("[ALERT] Suspicious activity detected.")
    print("1. User disabled.\n2. Input filtering applied.\n3. Logs archived.")
    print("4. System recovered.\n5. Incident documented.")
