import json

status = {"vergiftet": {"dauer": 3, "schaden": 5}}
json_text = json.dumps(status)

print(json_text)

json_text = '{"vergiftet": {"dauer": 3, "schaden": 5}}'
status2 = json.loads(json_text)

print(status2["vergiftet"]["schaden"])
