import psycopg2
from faker import Faker


db_params = {
    'dbname': 'test2',
    'user': 'postgres',
    'password': '3cure',
    'host': 'localhost',
    'port': '5432',
}

fake = Faker()

try:
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "User" (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) NOT NULL,
            password VARCHAR(50) NOT NULL,
            email VARCHAR(255) NOT NULL,
            first_name VARCHAR(200),
            last_name VARCHAR(200)
        );
    ''')


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "Products" (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            price NUMERIC NOT NULL,
            color VARCHAR(255)
        );
    ''')


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "Organizations" (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) NOT NULL,
            password VARCHAR(50) NOT NULL,
            email VARCHAR(255) NOT NULL
        );
    ''')
    
    

    users_data = [(fake.user_name(), fake.password(), fake.email(), fake.first_name(), fake.last_name()) for _ in range(10)]
    
    products_data = [
        (fake.word(), fake.pydecimal(min_value=10, max_value=100, right_digits=2), fake.color_name())
        for _ in range(10)
    ]
    
    organizations_data = [
        (fake.user_name(), fake.password(), fake.email())
        for _ in range(10)
    ]

    cursor.executemany('''
        INSERT INTO "User" (username, password, email, first_name, last_name)
        VALUES (%s, %s, %s, %s, %s);
    ''', users_data)
    
    cursor.executemany('''
        INSERT INTO "Products" (name, price, color)
        VALUES (%s, %s, %s);
    ''', products_data)
    
    cursor.executemany('''
        INSERT INTO "Organizations" (username, password, email)
        VALUES (%s, %s, %s);
    ''', organizations_data)


    connection.commit()
    print("Tables created successfully!")


except psycopg2.Error as e:
    print(f'Error: Unable to connect to PostgreSQL. {e}')

finally:
    if connection:
        cursor.close()
        connection.close()
        print('Connection closed.')

