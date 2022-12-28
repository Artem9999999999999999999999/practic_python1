import bisect as b


class StrategyDeal:
    def __init__(self, bank, entry, targets, close):
        self.bank = bank
        self.entry = entry
        self.targets = targets
        self.close = close

    def get_targets(self):
        return self.targets

    def get_target_per(self):
        return [(target / self.entry - 1) * 100 for target in self.targets]

    def get_target_banks(self):
        return [(self.bank * target) for target in self.targets]

    def get_str_target(self, i, t, p, b):
        return f"{i} target: {t}\n" \
               f"Percent: {round(p, 3)}%\n" \
               f"Bank: {round(b, 3)}"

    def __str__(self):
        z = zip(self.get_targets(), self.get_target_per(), self.get_target_banks())
        targets = "\n\n".join([self.get_str_target(i + 1, t, p, b) for i, (t, p, b) in enumerate(z)])
        return f"BANK: {self.bank}\nSTART_PRICE: {self.entry}\nSTOP_PRICE: {self.close}\n{targets}"

def get_deals(raw_data):
    raw_deals = raw_data.split("-----")
    deals = []
    list_search = []
    for raw_deal in raw_deals:
        bank_index = raw_deal.find('Bank:')
        entry_index = raw_deal.find('Entry:')
        target_index = raw_deal.find('Target:')
        close_index = raw_deal.find('Close:')

        if bank_index == -1 or entry_index == -1 or target_index == -1 or close_index == -1:
            continue

        bank_str = raw_deal[bank_index + 6:entry_index]
        entry_str = raw_deal[entry_index + 6:target_index]
        target_str = raw_deal[target_index + 8:close_index]
        close_str = raw_deal[close_index + 7:]

        bank_number = int(bank_str[:-4])
        entry_number = float(entry_str[:-4])
        targets_number = [float(t[:-4]) for t in target_str.split(";")]
        close_number = float(close_str[:-6])

        deals.append(StrategyDeal(bank_number, entry_number, targets_number, close_number))

    return deals

def read_data(file_name):
    with open(file_name) as file:
        return file.read()


def write_data(file_name, data):
    f = open(file_name, 'w')
    f.write("\n\n-----\n\n".join([str(d) for d in data]))
    f.close()


def main():
    content = read_data('input.txt')
    result = get_deals(content)
    write_data('output.txt', result)


if __name__ == '__main__':
    main()
