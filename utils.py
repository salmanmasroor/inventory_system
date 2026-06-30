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


def _get_int(prompt, min_value=None):
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None:
                if value < min_value:
                    print(f"Value must be at least {min_value}.")
                    continue
            return value
        except ValueError:
            print("Enter a valid whole number.")


def _get_float(prompt, min_value=0.01):
    while True:
        try:
            value = float(input(prompt))
            if min_value is not None:
                if value < min_value:
                    print(f"Value must be greater than {min_value}.")
                    continue
            return value
        except ValueError:
            print("Enter a valid number.")


def _get_text(prompt, allow_spaces=True, max_length=100):
    while True:
        value = input(prompt).strip()
        if not value:
            print("Field can't be empty.")
            continue
        check_value = value.replace(" ", "") if allow_spaces else value
        if not check_value.isalnum():
            print("Only letters and numbers allowed.")
            continue
        if len(value) > max_length:
            print(f"Max {max_length} characters.")
            continue
        return value