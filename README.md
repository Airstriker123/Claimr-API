# Claimr API
Backend api logic of Claimr

#   project structure guide

```jupyterpython
claimr-backend/
│
├── app/
│   ├── __init__.py          # create_app() here
│   ├── config.py           # config (DB, secret key)
│   ├── extensions.py       # db, bcrypt, etc.
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── entry.py
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py         # login/register
│   │   ├── entries.py      # CRUD
│   │   └── dashboard.py    # summaries (optional)
│   │
│   ├── services/           # logic layer (VERY good for marks)
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   └── entry_service.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── validators.py
│   │   └── helpers.py
│
├── migrations/             # if using Flask-Migrate (optional)
│
├── run.py                  # entry point
├── requirements.txt
├── .env
└── README.md
```