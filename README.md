# To run the Server from the CLI execute the following command

```
cd app

uvicorn main:app --reload
||
fastapi dev main.py
```

# Overall view of the application

1. Entering the main page (landing page) you can select the mathematical formula you want and to make it intuitive you have at your disposal boxes with a minimalistic design and the name of the of the mathematical formula/computation you may want.

2. From there the application displays a form like widget that request for the information needed for the computation. Input them and press enter of 'compute' button and wait for the result to be displayed.

## Routing

1. **auth** - for authentication/authorization purposes used **JWT**
2. **signin** - basic login in the app
3. **/math_formulas**

- **/fibo** - fibonacci series
- **/fact** - factorial series
- **/pow** - exponentiation  
- **/cmmmc** - lcm
- **/cmmdc** - gcd

## Project structure

```
.
├── app
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── models.py ----- requests / responses
│   ├── routes
│   │   ├── __init__.py
│   │   └── routes.py ----- routing
│   ├── services
│   │   ├── auth_serv.py -- authorization 
│   │   ├── __init__.py
│   │   ├── math_serv.py -- math operations service 
│   └── utils
│       ├── algorithms.py - math agos
│       ├── __init__.py
└── README.md
```

### Tables created

1.

```
CREATE TABLE IF NOT EXISTS User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    date TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    func_name TEXT NOT NULL,
    nr_params INTEGER NOT NULL,
    params_name TEXT NOT NULL,
    params_value TEXT NOT NULL,
    date TEXT NOT NULL
);
```

2. How to query the db

```
sqlite3 app.db
.tables -> gives all the tables
select * from history;
select * from User;
```
