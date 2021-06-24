from tkinter import *
import psycopg2
import uuid


def connect():
    conn=psycopg2.connect("dbname='database2' user='postgres' password='101216' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books3 (id SERIAL PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn=psycopg2.connect("dbname='database2' user='postgres' password='101216' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO books3(id,title,author,year,isbn) VALUES(DEFAULT,%s,%s,%s,%s)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn=psycopg2.connect("dbname='database2' user='postgres' password='101216' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM books3")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year=int(),isbn=int()):
    conn=psycopg2.connect("dbname='database2' user='postgres' password='101216' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM books3 WHERE title=%s OR author=%s OR year=%s OR isbn=%s",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=psycopg2.connect("dbname='database2' user='postgres' password='101216' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM books3 WHERE id=%s",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn=psycopg2.connect("dbname='database2' user='postgres' password='101216' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE books3 SET title=%s, author=%s, year=%s, isbn=%s WHERE id=%s",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

connect()
