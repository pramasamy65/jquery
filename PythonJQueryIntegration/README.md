### JQuery and Python Integration

## STEP 1 : Python SetUp
	* Python Installation
		* python --version
	* Install PIP
		* sudo easy_install pip
		
	* pydrda Installation
		* pip install pydrda
		* pip3 install pydrda - For Python version 3
			https://pypi.org/project/pydrda/

	* Python Execution command
		* python HelloWorld.py

## STEP 2 : Derby SetUp
	* Download Derby - db-derby-10.14.2.0-bin.zip
	* Start Server : ./startNetworkServer (in BIN Folder)
	* Start Client : ./ij (in BIN Folder)
		* connect 'jdbc:derby://localhost:1527/db;create=true';
		* CREATE TABLE test (id integer);
		* insert into test values(1);
		* insert into test values(100);

## STEP 3 : Server Setup to RUN Python
	* pip install Flask - need a server to serve Python to a web page
	* pip3 install flask  - For Python 3 

## STEP 4 : 1_HelloWorld.py - First Python Program

## STEP 5 : 2_PythonWithFlask.py - Run the python Program in Server(Flask)

## STEP 6 : 3_PythonWithFlaskAndHtml.py - Render HTML Pages in Python

## STEP 7 :: 4_GetTableData.py - Data base Connect using Python





