import sqlite3

conn = sqlite3.connect('hw.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_title TEXT NOT NULL,
        price REAL NOT NULL DEFAULT 0.0,
        quantity INTEGER NOT NULL DEFAULT 0
    )
''')

def add_products():
    products = [
        ('Мыло', 25.5, 10),
        ('Зубная паста', 75.9, 15),
        ('Шампунь', 150.75, 8),
        ('Кондиционер', 130.5, 7),
        ('Лосьон', 250.0, 12),
        ('Крем', 90.0, 6),
        ('Маска для лица', 300.0, 4),
        ('Мочалка', 35.0, 10),
        ('Дезодорант', 120.0, 9),
        ('Пенка для умывания', 180.0, 5),
        ('Зубная щетка', 45.0, 20),
        ('Гель для душа', 100.0, 6),
        ('Скраб', 85.0, 3),
        ('Бальзам для губ', 40.0, 14),
        ('Тональный крем', 290.0, 2)
    ]
    cursor.executemany('INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)', products)
    conn.commit()

def update_quantity(product_id, new_quantity):
    cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (new_quantity, product_id))
    conn.commit()

def update_price(product_id, new_price):
    cursor.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, product_id))
    conn.commit()

def delete_product(product_id):
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()

def get_all_products():
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    for product in products:
        print(product)

def get_filtered_products(max_price, min_quantity):
    cursor.execute('SELECT * FROM products WHERE price <= ? AND quantity >= ?',
                   (max_price, min_quantity))
    products = cursor.fetchall()
    for product in products:
        print(product)

def search_by_name(search_term):
    cursor.execute('SELECT * FROM products WHERE product_title LIKE ?',
                   ('%' + search_term + '%',))
    products = cursor.fetchall()
    for product in products:
        print(product)

add_products()
update_quantity(1, 20)
update_price(2, 80.0)
delete_product(3)
get_all_products()
get_filtered_products(100, 5)
search_by_name('Мыло')

conn.close()


