# Zadanie 3.2
shopping_list = {
    "piekarnia": ['chleb', 'pączek', 'bułki'],
    "warzywniak": ['marchew', 'seler', 'rukola'],
    "kwiacirania": ['róże', 'tulipany', 'stokrotki'],
    "sklep_elektroniczny": ['klawiatura', 'myszka']
}
sum = 0
for key, value in shopping_list.items():
    print(f"Idę do {key.capitalize()} i kupuję tam {[value.capitalize() for value in value]}")
    sum += len(value)

print(f"W sumie kupuję {sum} produktów.")