dates = [
    {
        "day": 6,
        "from": "10:00",
        "to": "23:00"
    },
    {
        "day": 0,
        "from": "11:00",
        "to": "23:00"
    },
    {
        "day": 1,
        "from": "11:00",
        "to": "23:00"
    },
    {
        "day": 2,
        "from": "11:00",
        "to": "23:00"
    },
    {
        "day": 3,
        "from": "12:00",
        "to": "23:00"
    },
    {
        "day": 4,
        "from": "12:00",
        "to": "23:00"
    },
    {
        "day": 5,
        "from": "11:00",
        "to": "23:00"
    }
]
dates.sort(key=lambda x: x['day'])
print(dates)