import psycopg

con = psycopg.connect('postgresql://postgres:postgres@localhost/biblioteca')

cursor = con.cursor()

