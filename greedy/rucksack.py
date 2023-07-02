
# Volume and value of items
items = [
    [5, 8],
    [5, 8],
    [15, 20],
    [15, 17],
    [10, 10],
    [6, 6],
    [12, 10],
    [30, 20],
    [8, 5],
    [11, 5]
]

def rucksack(volume: int, n: int):
    # calculate the value of each item
    for i in range(len(items)):
        items[i].append(items[i][1] / items[i][0])

    # sort items by value
    sorted_items = sorted(items, key=lambda x: x[2], reverse=True)

    current_volume = 0
    for item in sorted_items:
        if item[0] + current_volume <= volume:
            current_volume += item[0]
            print("Item with volume {} and value {} is taken".format(item[0], item[1]))

rucksack(25, len(items))