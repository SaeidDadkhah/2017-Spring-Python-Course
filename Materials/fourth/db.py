import sqlite3


if __name__ == '__main__':
    db = sqlite3.connect('car.db')
    db.row_factory = sqlite3.Row
    db.execute('DROP TABLE IF EXISTS car')
    db.execute('CREATE TABLE car (model text, year int)')
    db.execute('INSERT INTO car (model, year) VALUES (?, ?)', ('pride', 1995))
    db.execute('INSERT INTO car (model, year) VALUES (?, ?)', ('pride', 2000))
    db.execute('INSERT INTO car (model, year) VALUES (?, ?)', ('pride', 2001))
    db.execute('INSERT INTO car (model, year) VALUES (?, ?)', ('pride', 2002))
    db.commit()
    cursor = db.execute('SELECT model, year FROM car ORDER BY year')
    for record in cursor:
        print(record['model'])

