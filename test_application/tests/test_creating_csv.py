import csv
row_list = [6291, "0856/АС-22", 51903, "Інститут педагогіки Національної академії педагогічних наук України", "Доктор філософії", "01 Освіта/Педагогіка", "011 Освітні"],
with open('quotes.csv', 'a', encoding="utf-8", newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=';')
    writer.writerows(row_list)
