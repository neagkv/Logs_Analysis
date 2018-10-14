#!/usr/bin/python2.7.12

import psycopg2
import datetime

DB = "news"


# Function to connect to the news database and run queries
def psql_connection(query):
    """Connect to the PostGreSQL database,run selected query
    and return the result"""
    try:
        conn = psycopg2.connect(database=DB)
        cur = conn.cursor()
        cur.execute(query)
    except Exception:
        ("Error connecting to database")
    else:
        print("Calling database...")
        print("")
        results = cur.fetchall()
        conn.close()
        return results


# Function to find the three most viewed articles
def most_viewed_articles():
    """Create query string, connect to the database and parse results"""
    query = """
        SELECT articles.title, COUNT(*) AS views
        FROM articles
        JOIN log
        ON log.path = '/article/' || articles.slug
        WHERE log.status ='200 OK'
        GROUP BY articles.title ORDER BY views DESC LIMIT 3;
    """
    results = psql_connection(query)

    print("Most viewed articles:")
    for result in results:
        print '{article} - {count} views'.format(
            article=result[0], count=result[1])


# Function to find the three most viewed authors
def most_viewed_authors():
    """Create query string, connect to the database and parse results"""
    query = """
        SELECT authors.name, COUNT(*) AS views
        FROM articles
        JOIN log
        ON log.path = '/article/' || articles.slug
        JOIN authors
        ON authors.id = articles.author
        WHERE log.status ='200 OK'
        GROUP BY authors.name ORDER BY views DESC LIMIT 3;
    """
    results = psql_connection(query)

    print("Most viewed authors:")
    for result in results:
        print '{author} - {count} views'.format(
            author=result[0], count=result[1])


# Function to find the days with more than 1% errors on user requests
def find_error_days():
    """Create query string, connect to the database and parse results"""
    query = """
        SELECT all_requests.day,
        (ROUND((error_requests.bad * 1000)/all_requests.good)/10)
        AS percent
        FROM all_requests
        JOIN error_requests
        ON all_requests.day = error_requests.day
        WHERE ROUND((error_requests.bad * 1000)/all_requests.good) > 10
    """
    results = psql_connection(query)

    print("Days with more than 1% errors")
    for result in results:
        print '{date} - {errors} % errors'.format(
            date=result[0].strftime('%B %d, %Y'), errors=result[1])


# Run all query functions
if __name__ == '__main__':
    most_viewed_articles()
    print("")
    most_viewed_authors()
    print("")
    find_error_days()
