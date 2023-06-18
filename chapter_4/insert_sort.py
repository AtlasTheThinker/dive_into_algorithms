def insert_cabinet(cabinet, to_insert):
    check_location = len(cabinet) - 1
    insert_location = 0
    while check_location >= 0:
        if to_insert > cabinet[check_location]:
            insert_location = check_location + 1
            check_location = -1
        check_location -= 1
    cabinet.insert(insert_location, to_insert)
    return cabinet

def insertion_sort(cabinet):
    new_cabinet = []
    while len(cabinet):
        new_cabinet = insert_cabinet(new_cabinet, cabinet.pop(0))
    return new_cabinet

cabinet = [8, 6, 14, 3, 2, 15, 11, 9]
cabinet = insertion_sort(cabinet)
print(cabinet)