# Claimr API
Backend api logic of Claimr

#   project structure guide

```python
claimr-backend/app # application folder
│
│   config.py # application config
│   extensions.py # application database and other extensions required
│   __init__.py #entry to app
│   
├───models # database tables
│       entry.py
│       user.py
│       __init__.py #blueprints join
│       
├───routes #endpoints
│       auth.py # auth related routes
│       entries.py # entry routes
│       home.py # server info
│       __init__.py # blueprint join
│       
├───services # route logic store
│   │   __init__.py #blueprint join
│   │   
│   ├───auth # auth logic folder
│   │       get_current_user_service.py #get session
│   │       login_user_service.py #login
│   │       register_user_service.py # register
│   │       wipe_session_service.py # logout
│   │       __init__.py #blueprint
│   │       
│   └───entry # entries folder logic
│           add_entry_service.py
│           delete_entry_service.py
│           get_entry_service.py
│           update_entry_service.py 
│           __init__.py #blueprint join
│           
└───utils #utility for debuging/ other uses
        debug.py #debug logic
        get_uptime.py # get server uptime
        __init__.py #blueprint  join
```
