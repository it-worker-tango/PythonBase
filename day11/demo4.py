with open("msg.txt", 'r', encoding='utf-8') as file:
    while True:
        line = file.readline()
        if line == '':
            break
        print(line)
