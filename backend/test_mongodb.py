from app.database.mongodb import test_connection

print("Testing MongoDB connection...")

if test_connection():
    print("MongoDB connected successfully!")
