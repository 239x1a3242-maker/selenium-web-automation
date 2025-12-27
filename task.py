TASK = [
    {
        "action": "open",
        "url": "https://www.ilovepdf.com/register"
    },

    # Name
    {
        "action": "type",
        "selector": "input[placeholder='Name']",
        "value": "ashok7582"
    },

    # Email
    {
        "action": "type",
        "selector": "input[placeholder='Email']",
        "value": "ashok7582@example.com"
    },

    # Password
    {
        "action": "type",
        "selector": "input[placeholder='Password']",
        "value": "StrongPassword123!"
    },

    # Sign up
    {
        "action": "click",
        "selector": "button[type='submit']"
    },

    # WAIT — human completes CAPTCHA / email verification
    {
        "action": "wait_for",
        "selector": "a[href='/account']"
    }
]
