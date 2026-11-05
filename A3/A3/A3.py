
previous = int(input())
current = int(input())

if current >= previous:
    used = current - previous
else:
    used = 10000 - previous + current

if used <= 300:
    payment = 21
elif used <= 600:
    payment = 21 + (used - 300) * 0.06
elif used <= 800:
    payment = 21 + 300 * 0.06 + (used - 600) * 0.04
else:
    payment = 21 + 300 * 0.06 + 200 * 0.04 + (used - 800) * 0.025

if used > 0:
    average = payment / used
else:
    average = 0

print("Вывод:")
print("Предыдущее\tТекущее\tИспользовано\tК оплате\tСр. цена м^3")
print(f"{previous}\t\t{current}\t{used}\t\t{payment:.2f}\t\t{average:.2f}")
