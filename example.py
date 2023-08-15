import sys

def validate_args(expected_length):
    if len(sys.argv) != expected_length:
        print("引数の数が正しくありません。")
        sys.exit()

def read_file(pathname):
    with open(pathname, 'r') as file:
        return file.read()

def write_file(pathname, contents):
    with open(pathname, 'w') as file:
        file.write(contents)

command = sys.argv[1]

if command == 'reverse':
    validate_args(4)
    contents = read_file(sys.argv[2])
    write_file(sys.argv[3], contents[::-1])

elif command == 'copy':
    validate_args(4)
    contents = read_file(sys.argv[2])
    write_file(sys.argv[3], contents)

elif command == 'duplicate-contents':
    validate_args(4)
    contents = read_file(sys.argv[2])
    duplicated_contents = contents * int(sys.argv[3])
    write_file(sys.argv[2], duplicated_contents)

elif command == 'replace-string':
    validate_args(5)
    contents = read_file(sys.argv[2])
    new_contents = contents.replace(sys.argv[3], sys.argv[4])
    write_file(sys.argv[2], new_contents)

else:
    print(f"不明なコマンド: {command}")
    sys.exit()
