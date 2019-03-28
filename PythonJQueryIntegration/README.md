### JQuery and Python Integration

## STEP 1 : Python SetUp
	* Python Installation
		* python --version

	* Python Execution 
		* python HelloWorld.py

## STEP 2 : Derby SetUp
	* Download Derby - db-derby-10.14.2.0-bin.zip
	* Start Server : ./startNetworkServer (in BIN Folder)
	* Start Client : ./ij (in BIN Folder)
		* connect 'jdbc:derby://localhost:1527/db;create=true';
		* CREATE TABLE test (id integer);
		* insert into test values(1);
		* insert into test values(100);

	* pip install pydrda
		https://pypi.org/project/pydrda/

## STEP 3 : 


