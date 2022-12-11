class Monkey:
    def __init__(self, starting_items, operation, test_div, test_true, test_false):
        self.starting_items: list = starting_items
        self.operation: str = operation
        self.test_div: int = test_div
        self.test_true: int = test_true
        self.test_false: int = test_false
        self.inspected = 0
    
    def has_item(self):
        return bool(self.starting_items)

    def operate(self) -> int:
        self.inspected += 1
        old = self.starting_items[0]
        new = eval(self.operation.replace('old', str(old))) // 3
        self.starting_items[0] = new
        return new

    def test(self, new) -> bool:
        return new % self.test_div == 0

    def throw(self, monkey):
        item =  self.starting_items.pop(0)
        monkey.starting_items.append(item)

def part1():
    monkeys = []
    with open('data/day11input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
        monke_count = (len(lines) + 1) // 7
        
        for monke in range(monke_count):
            items = lines[monke*7 + 1][16:].split(',')
            starting_items = list(map(int, items))
            operation = lines[monke*7 + 2][17:]
            test = int(lines[monke*7 + 3][19:])
            test_true = int(lines[monke*7 + 4][25:])
            test_false = int(lines[monke*7 + 5][26:])
            monke = Monkey(starting_items, operation, test, test_true, test_false)
            monkeys.append(monke)

    for _ in range(20):
        for monkey in monkeys:
            while monkey.has_item():
                new = monkey.operate()
                if monkey.test(new):
                    dest = monkeys[monkey.test_true]
                    monkey.throw(dest)
                else:
                    dest = monkeys[monkey.test_false]
                    monkey.throw(dest)
    t = sorted([monke.inspected for monke in monkeys], reverse=True)  
    return t[0] * t[1]  

print(part1())