# The Teyvat Educational Press official website

This repo is the official website repo, dedicated to building a standardized player community

[中文README](README.zh.md)
## Overall structure

1. Home page
2. Publications
3. Notifications
4. Products
5. Contact us/About us
6. Login page



## Install

Docker build:

```bash
    docker build -t teyvatedu .
```

prechecks:
```bash
mkdir -p /usr/tep/static /usr/tep/templates /usr/tep/sqlite3
```

Docker run:

```bash
    docker run -d -p 80:80 \
    --name teyvatedu-app \
    -e APP_NAME=TEPBackendAPI \
    -e JWT_SECRET_KEY=randomkey \
    -e JWT_ALGORITHM=HS256 \
    -v /usr/tep/static:/app/static \
    -v /usr/tep/templates:/app/templates \
    -v /usr/tep/sqlite3:/app/sqlite3 \
    my_fastapi_app
```

Generate JWT_SECRET_KEY: 
```bash
tr -dc 'A-Z0-9' < /dev/urandom | head -c 64
```
replace JWT_SECRET_KEY with the generated key.

## Credits

This project includes code from [Editorial by HTML5 UP](html5up.net) by [@ajlkn], used under [CC BY 3.0](html5up.net/license). Changes were made to the original code.

Last modified: 2024-7-1