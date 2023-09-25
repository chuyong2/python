def read_non_terminals():
    non_terminals = input("请输入非终结符（以#结束）：").strip().split()
    return non_terminals

def read_terminals():
    terminals = input("请输入终结符（以#结束）：").strip().split()
    return terminals

def read_productions():
    productions = []
    while True:
        production = input("请输入产生式（以#结束）：").strip()
        if production == "#":
            break
        productions.append(production)
    return productions

def is_ll1_grammar(non_terminals, terminals, productions):
    # 构造First集合
    first = {}
    for terminal in terminals:
        first[terminal] = {terminal}
    for non_terminal in non_terminals:
        first[non_terminal] = set()

    changed = True
    while changed:
        changed = False
        for production in productions:
            lhs, rhs = production.split('->')
            rhs_symbols = rhs.strip().split()
            for symbol in rhs_symbols:
                if symbol in terminals:
                    if symbol not in first[lhs]:
                        first[lhs].add(symbol)
                        changed = True
                    break
                elif symbol in non_terminals:
                    prev_size = len(first[lhs])
                    first[lhs].update(first[symbol])
                    if prev_size != len(first[lhs]):
                        changed = True
                    if '' not in first[symbol]:
                        break
            else:
                if '' not in first[lhs]:
                    first[lhs].add('')

    # 构造Follow集合
    follow = {}
    for non_terminal in non_terminals:
        follow[non_terminal] = set()

    follow[non_terminals[0]].add('#')

    changed = True
    while changed:
        changed = False
        for production in productions:
            lhs, rhs = production.split('->')
            rhs_symbols = rhs.strip().split()
            for i, symbol in enumerate(rhs_symbols):
                if symbol in non_terminals:
                    prev_size = len(follow[symbol])
                    if i == len(rhs_symbols) - 1:
                        follow[symbol].update(follow[lhs])
                    else:
                        next_symbol = rhs_symbols[i + 1]
                        if next_symbol in terminals:
                            follow[symbol].add(next_symbol)
                        elif next_symbol in non_terminals:
                            follow[symbol].update(first[next_symbol])
                            if '' in first[next_symbol]:
                                follow[symbol].update(follow[lhs])
                    if prev_size != len(follow[symbol]):
                        changed = True

    # 构造预测分析表
    table = {}
    for non_terminal in non_terminals:
        table[non_terminal] = {}
        for terminal in terminals:
            table[non_terminal][terminal] = []

    for production in productions:
        lhs, rhs = production.split('->')
        rhs_symbols = rhs.strip().split()
        for terminal in terminals:
            if terminal in first[lhs]:
                table[lhs][terminal].append(production)
        if '' in first[lhs]:
            for terminal in terminals:
                if terminal in follow[lhs]:
                    table[lhs][terminal].append(production)

    # 检查是否是LL(1)文法
    for non_terminal in non_terminals:
        for terminal in terminals:
            if len(table[non_terminal][terminal]) > 1:
                return False

    return True, table

def print_ll1_table(table):
    print("LL(1)分析表如下：\n")
    headers = [""] + table[next(iter(table))].keys()
    print("{:10}".format(""), end="")
    for header in headers:
        print("{:20}".format(header), end="")
    print()

    for non_terminal, row in table.items():
        print("{:10}".format(non_terminal), end="")
        for productions in row.values():
            print("{:20}".format(" ".join(productions)), end="")
        print()

non_terminals = read_non_terminals()
terminals = read_terminals()
productions = read_productions()

is_ll1, ll1_table = is_ll1_grammar(non_terminals, terminals, productions)

if is_ll1:
    print_ll1_table(ll1_table)
else:
    print("该文法不是LL(1)文法。")
