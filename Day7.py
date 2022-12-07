class Directory():
    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent: Directory = parent
        self.size = 0
    
    def __str__(self) -> str:
        return self.name

    def __lt__(self, other) -> bool:
        return self.size < other.size


def part1():
    directories = []
    with open('data/day7input.txt') as f:
        current_dir = None
        for line in f:
            line = line.strip()
            if line.startswith('$ cd'):
                if line[5:] != '..':
                    current_dir = Directory(name=line[5:], parent=current_dir)
                    directories.append(current_dir)
                else:
                    current_dir = current_dir.parent
            elif line[0].isdigit():
                file_size = int(line.split(' ')[0])
                current_dir.size += file_size
                tmp = current_dir.parent
                while tmp:
                    tmp.size += file_size
                    tmp = tmp.parent

    result = 0
    for directory in directories:
        if directory.size < 100000:
            result += directory.size
    
    return result


def part2():
    directories = []
    used_space = 0
    with open('data/day7input.txt') as f:
        current_dir = None
        for line in f:
            line = line.strip()
            if line.startswith('$ cd'):
                if line[5:] != '..':
                    current_dir = Directory(name=line[5:], parent=current_dir)
                    directories.append(current_dir)
                else:
                    current_dir = current_dir.parent
            elif line[0].isdigit():
                file_size = int(line.split(' ')[0])
                used_space += file_size
                current_dir.size += file_size
                tmp = current_dir.parent
                while tmp:
                    tmp.size += file_size
                    tmp = tmp.parent

    directories.sort()
    for directory in directories:
        if directory.size > used_space - 40000000:
            return directory.size


print(part1())
print(part2())