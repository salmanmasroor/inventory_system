def _print_table(self,data):
    print("ID  | Name         | Price    | Qty")
    print("-------------------------------------")
    for row in data:
        print(
            str(row[0]).ljust(3), "|",
            str(row[1]).ljust(12), "|",
            str(row[2]).ljust(8), "|",
            str(row[3])
        )


def _get_int(self,prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Enter a Valid Number")

def _get_float(self,prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Enter the Valid Number")