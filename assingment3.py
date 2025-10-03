try:
    with open('my_file.txt', 'r') as f:
        data = f.read()
        print("File contents:")
        print(data)
except FileNotFoundError:
    print("Error: my_file.txt was not found.")