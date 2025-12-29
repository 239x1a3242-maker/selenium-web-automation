# PERFECT TASK - httpbin.org ALWAYS WORKS
TASK = [
    {"action": "open", "url": "https://httpbin.org/forms/post"},
    {"action": "wait_seconds", "seconds": 2},
    {"action": "type", "selector": "input[name='custname']", "value": "Ashok Gajja"},
    {"action": "type", "selector": "input[name='custtel']", "value": "1234567890"},
    {"action": "type", "selector": "input[name='custemail']", "value": "ashok@test.com"},
    {"action": "wait_seconds", "seconds": 1},
    {"action": "click", "selector": "input[type='submit']"},
    {"action": "wait_seconds", "seconds": 2},
    {"action": "screenshot", "filename": "SUCCESS_PERFECT.png"}
]
