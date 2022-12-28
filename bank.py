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
        return [self.bank * target / self.entry for target in self.targets]

    def get_str_target(self, i, t, p, b):
        return f"{i} target: {t}\n" \
               f"Percent: {round(p, 3)}%\n" \
               f"Bank: {round(b, 3)}"

    def __str__(self):
        z = zip(self.get_targets(), self.get_target_per(), self.get_target_banks())
        targets = "\n\n".join([self.get_str_target(i + 1, t, p, b) for i, (t, p, b) in enumerate(z)])
        return f"BANK: {self.bank}\nSTART_PRICE: {self.entry}\nSTOP_PRICE: {self.close}\n\n{targets}"


def pars(raw_data):
    raw_deals = raw_data.split("-----")
    deals = []
    for raw_deal in raw_deals:
        bank_index = raw_deal.find('Bank:')
        entry_index = raw_deal.find('Entry:')
        target_index = raw_deal.find('Target:')
        out_index = raw_deal.find('Close:')

        if bank_index == -1 or entry_index == -1 or target_index == -1 or out_index == -1:
            continue

        bank_str = raw_deal[bank_index + 5:entry_index]
        entry_str = raw_deal[entry_index + 6:target_index]
        target_str = raw_deal[target_index + 7:out_index]
        clos_str = raw_deal[out_index + 6:]

        bank_num = float(bank_str[:-4])
        entry_num = float(entry_str[:-4])
        targets_num = [float(t[:-4]) for t in target_str.split(";")]
        clos_number = float(clos_str[:-5])

        deals.append(StrategyDeal(bank_num, entry_num, targets_num, clos_number))

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
    result = pars(content)
    write_data('output.txt', result)


if __name__ == '__main__':
    main()
