# Logs_Analysis

An internal python reporting tool to analyze server data from a PosgreSQL database.

## Overview:

This python script tool will connect to and read from the provided news database, in order to analyze user activiy by answering three questions:

1. What are the three articles with the most views?
2. Who are the three authors with the most overall views?
3. On Which days days did user requests lead to more than 1% errors?

## Requirements:

* [python 2.7.12](https://www.python.org/download/releases/2.7/) - Or later version
* [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) - A cross-platform virtualization software
* [Vagrant](https://www.vagrantup.com/downloads.html) - A tool for working with virtual environments
* [git](https://git-scm.com/downloads) - A version control tool

## Setup and Configuration:

1. Install Vagrant.
2. Install VirtualBox.
3. Clone [this repository](https://github.com/udacity/fullstack-nanodegree-vm) with the 	 needed VirtualBox configuration.
```
$ git clone https://github.com/udacity/fullstack-nanodegree-vm
```
4. cd into the vagrant reposiotry.
```
$ cd fullstack-nanodegree-vm/vagrant/
```
5. Clone [this reposiotry](https://github.com/neagkv/Logs_Analysis.git) with
	the database and python script into the vagrant directory.
```
$ git clone https://github.com/neagkv/Logs_Analysis.git
```
6. Start up the virtual machine.
```
$ vagrant up
```
7. log into the virtual machine.
```
$ vagrant ssh
```
8. cd into the Logs_Analysis directory.
```
$ cd /vagrant/Logs_Analysis
```
9. Unzip the database.
```
$ unzip newsdata.zip
```
10. Load data.
```
$ psql -d news -f newsdata.sql
```
## Connect to database and create views:

1. Connect to database.
```
$ psql -d news
```

2. Create first view.
```
news=> create view all_requests as select date_trunc('day', time) "day", count(*) as good from log group by day order by day;
```
3. Create second view.
```
news=> create view error_requests as select date_trunc('day', time) "day", count(*) as bad from log where status != '200 OK' group by day order by day;
```

## To Run the Script:

```
$ python logs_report.py
```














