#4. В строке "Ivanou Ivan" поменяйте местами слова:"Ivanou Ivan" => "Ivan Ivanou"

text = "Ivanou Ivan"
words = text.split()  # ['Ivanou', 'Ivan']
result = f"{words[1]} {words[0]}"
print(result)