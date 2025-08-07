# Mathematical functions API
### An API for basic mathematical needs
![image](dan-cristian-padure-h3kuhYUCE9A-unsplash.jpg)

The Api solves and returns in a __JSON__ format the result of some basic mathematical 
operations. Easy to use it comes with a JWT endpoint for authentification and call validation.
The available mathematical functions are:


### Available Mathematical functions
---
- Fibonnaci sequence (nth element)
- Pow function
- Factorial of a number
- GCD (greatest common divisor)
- LCM (lowest common multiplier)
- Sum:  $\sum_{k=1}^n = ?$

Additional for the purpose of the repo we have a folder (not related with the api) where the all homeworks from the python trainning are done.

### How to execute the project (homework)
---


For the purpose of the repo all homeworks are separated in $Hi$ where $i$ denotes the week/folder of the task. Each folder has a <span style="color: #2887c7ff">___main.py___ </span> file. Execute it to check the functionality. Additionally the file <span style="color: #2887c7ff">___r.sh___ </span> is used to create/activate/deactivate a virtual environment easier just by using in the root of the project (___homework___ folder) the command:

####  For creating and/or activation:

` source ./r.sh -a <name_of_venv> ` - in case no name is provided the default is __venv__.

#### For deactivation:
`source r.sh -d` - also in executed in the root folder


### How to execute the project (MathAPI)
---

In the root folder <span style="color: #2887c7ff">___src/backend/app/___ </span> run in the command line `source r.sh` and after all dependecies have been installed run `fastapi dev main.py`. 



__In case you don't have installed sqlite__ here is a short installation demo for those with Ubuntu
```bash
# in the cli run:
~ sudo apt update 
~ sudo apt install sqlite3

# for verification 
~ sqlite3 --version

# to connect to the database 
~ sqlite3 MathFormulas.db
```

After the installation execute the <span style="color: #2887c7ff">__create.sql__ </span>from the <span style="color: #2887c7ff">__src/backend/app/DB/__ </span> in the command line:


```bash
# connect to the database while in the DB folder
~ sqlite3 MathFormulas.db

# execute file 
~ .read create.sql 

# shortcut for both operations
~ sqlite3 MathFormulas.db < create.sql
```

__In case you don't have Redis__ here is a short tutorial how to install it on Ubuntu. 

```bash
#  instalation 
~ sudo apt update
~ sudo apt install redis-server -y 

# set the supervised mode to be managed by the systemd 
~ sudo nano /etc/redis/redis.conf
# change in the file the 'supervised no' to:
supervised systemd

# exit nano and restart  the service
~ sudo systemctl restart redis.service

# check the status 
~ systemctl status redis

# additional if you want to make redis start on boot 
~ sudo systemctl enable redis
```


### How does the it work 
--- 

The Api is comprised of the following endpoints each with its own role:
- <span style="color: #2887c7ff">__/__ </span>&rarr; the root endpoint, for the moment redirected to the base of the api.

- <span style="color: #2887c7ff">__/math_formulas/__ </span> &rarr; the base of the api it does return the whole history table (debug/testing purposes).

- <span style="color: #2887c7ff">__/signin/__ </span> &rarr; for the registration of a new user.

- <span style="color: #2887c7ff">__/users/__ </span> &rarr; for the enquiry of the user table (debug/testing purposes)

- <span style="color: #2887c7ff">__/auth/__ </span> &rarr; for authentification via email and password

- <span style="color: #2887c7ff">__/math_formulas/{NameofFormula}/__ </span> &rarr; endpoint for each formula to be executed (NameofFormula is replaced by each mathematical formula from the api).

### Expected bodies and headers
---

First a user must sing in providing some informations structured as following:

```JSON
{
    "name": "",
    "email": "",
    "password": ""
}

// The response will be in the form of
{
    "token": "",
    "token_type" : "bearer"
}
```

After that in the response will be provided a __JWT__ token that must be used in each of the __POST request__.
The token must be saved in the cookies from the frontend perspective and sent each time with the request in the header of the request. 

For the mathematical formulas we have 2 types of bodies: a body with 1 parameter denoted with $n$ and a body with 2 denoted as $n, m$ as follows:

```JSON
//  Body with 2 parameters
    {
        "n": 1,
        "m": 12
    }
// Body with 1 parameter
    {
        "n": 1
    }
```







