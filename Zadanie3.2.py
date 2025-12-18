# Zadanie 3.2
shopping_list = {
    "piekarnia": ['chleb', 'pączek', 'bułki'],
    "warzywniak": ['marchew', 'seler', 'rukola']
}
sum = 0
for key, value in shopping_list.items():
    print(f"Idę do {key.capitalize()} i kupuję tam {[value.capitalize() for value in value]}")
    sum += len(value)