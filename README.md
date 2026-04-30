# Claimr API
Backend api logic of Claimr

#   project structure guide

```python
claimr-backend/app
│
│   config.py
│   extensions.py
│   __init__.py
│   
├───models
│       entry.py
│       user.py
│       __init__.py
│       
├───routes
│       auth.py
│       entries.py
│       home.py
│       __init__.py
│       
├───services
│   │   __init__.py
│   │   
│   ├───auth
│   │       get_current_user_service.py
│   │       login_user_service.py
│   │       register_user_service.py
│   │       wipe_session_service.py
│   │       __init__.py
│   │       
│   └───entry
│           add_entry_service.py
│           delete_entry_service.py
│           get_entry_service.py
│           update_entry_service.py
│           __init__.py
│           
└───utils
        debug.py
        get_uptime.py
        __init__.py
```
