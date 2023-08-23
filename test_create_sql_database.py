import sqlite3

# Function to create the database and tables
def create_database():
    conn = sqlite3.connect("../../database/morphospecies_database.db")
    cursor = conn.cursor()

    # Create a table for the insect orders
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS insect_orders (
        id INTEGER PRIMARY KEY,
        order_name TEXT NOT NULL
    )
    """)

    # Insert some example insect orders
    orders_data = [
        ("1", "Coleoptera"),
        ("2", "Lepidoptera"),
        ("3", "Diptera"),
        ("4", "Hymenoptera"),
        ("5", "Orthoptera")
    ]
    cursor.executemany("INSERT INTO insect_orders (id, order_name) VALUES (?, ?)", orders_data)

    # Create a table for the morphospecies
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS morphospecies (
        id INTEGER PRIMARY KEY,
        species_name TEXT NOT NULL,
        characters TEXT NOT NULL,
        image_path TEXT NOT NULL,
        video_file TEXT NOT NULL,
        order_id INTEGER NOT NULL,
        FOREIGN KEY (order_id) REFERENCES insect_orders(id)
    )
    """)

    # Insert some example morphospecies data
    species_data = [
        ("1", "Tiger Beetle", "Fast and colorful", "path/to/image1.jpg", "path/to/video1.mp4", "1"),
        ("2", "Swallowtail Butterfly", "Large wingspan", "path/to/image2.jpg", "path/to/video2.mp4", "2"),
        ("3", "Fruit Fly", "Tiny and agile", "path/to/image3.jpg", "path/to/video3.mp4", "3"),
        ("4", "Honey Bee", "Social insects", "path/to/image4.jpg", "path/to/video4.mp4", "4"),
        ("5", "Grasshopper", "Strong hind legs", "path/to/image5.jpg", "path/to/video5.mp4", "5")
    ]
    cursor.executemany("""
    INSERT INTO morphospecies (id, species_name, characters, image_path, video_file, order_id)
    VALUES (?, ?, ?, ?, ?, ?)
    """, species_data)

    # Save changes and close the connection
    conn.commit()
    conn.close()

# Call the function to create the database
create_database()