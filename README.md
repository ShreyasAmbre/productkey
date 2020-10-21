# productkey
Product Key Genration for Antivirus User

# Dependencies need to install

    Python3 :- https://www.python.org/downloads/windows/ :- Note (version 3.8 will stable)

    sqlite3 :- https://www.sqlitetutorial.net/download-install-sqlite/ :- https://www.sqlite.org/download.html

    Virtualenv :- 
	Below docs to create virtualenv 
		:- https://docs.python.org/3/library/venv.html 
		OR 
		:- If u have pycharm install pycharm will help to create virtualenv automatically when you set the python interpreter for the project

# Now, activate the virtualenv and install all the packages present in requirements.txt using below command 
  :- pip install -r requirements.txt

# Run the project

# After all installation, Run python views.py file to start the project Note:- (It will automatically create the Database and tables in sqlite3)

# Endpoint 
	:- 127.0.0.1:5000/productkeygeneration 
    Note:- (After hitting this url id and random product key will generate which will be unique to every user)

	:- 127.0.0.1:5000/keycheck [params :- {id: value}]
    Note :- (After hitting this url if the key present the status will get change from unused to used of Keys table)

# To verify open cmd navigate to prokect root folder enter command

    sqlite3 Note:- Here u will navigate to sqlite shell

    .open test.sqlite3 Note:- This command used to open the database file

    SELECT * FROM productkey
