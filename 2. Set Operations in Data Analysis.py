# Task 1

def remove_duplicates(list):
    return set(list)

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]


print(sorted(remove_duplicates(customer_ids)))