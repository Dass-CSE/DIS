risk_data = [
    {"asset": "User Credentials", "threat": "SQL Injection", "vulnerability": "Unvalidated Input", "likelihood": "High", "impact": "High"},
    {"asset": "Sensitive Data", "threat": "Data Theft", "vulnerability": "Weak Access Controls", "likelihood": "Medium", "impact": "High"},
    {"asset": "Server", "threat": "DoS Attack", "vulnerability": "Open Ports", "likelihood": "Low", "impact": "Medium"}
]

risk_matrix = {
    ("High", "High"): "Critical",
    ("High", "Medium"): "High",
    ("High", "Low"): "Moderate",
    ("Medium", "High"): "High",
    ("Medium", "Medium"): "Moderate",
    ("Medium", "Low"): "Low",
    ("Low", "High"): "Moderate",
    ("Low", "Medium"): "Low",
    ("Low", "Low"): "Low"
}

mitigations = {
    "Unvalidated Input": "Use parameterized queries",
    "Weak Access Controls": "Implement RBAC",
    "Open Ports": "Use firewall and restrict unused ports"
}

header = f"{'Asset':<20} {'Threat':<20} {'Risk Level':<15} {'Mitigation'}"
separator = "-" * len(header)
print(header)
print(separator)

for item in risk_data:
    key = (item["likelihood"], item["impact"])
    risk_level = risk_matrix.get(key, "Unknown")
    mitigation = mitigations.get(item["vulnerability"], "Apply security best practices")
    print(f"{item['asset']:<20} {item['threat']:<20} {risk_level:<15} {mitigation}")
