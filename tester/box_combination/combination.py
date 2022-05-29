import os
from pathlib import Path

offset = 416
path_boxes = Path('tester/box_combination/labels')
path_save = Path('tester/box_combination/labels/combined')
combined_boxes = []

def offset_box(box: str, offset: int, row: int, column: int) -> list[float]:
    _, x, y, width, height = [float(elem) for elem in box.strip().split(' ')]
    box_offsetted = [
        # warning, x ad y were swapped
        (x + column) * offset,  # coordinate x with offset
        (y + row) * offset,  # coordinate y with offset
        width * offset,  # width
        height * offset,  # height
    ]
    return box_offsetted


def parse_name(name: str) -> tuple[int, int, str]:
    split_name = name.split('_')
    row = int(split_name[-2])
    column = int(split_name[-1].split('.')[0])
    orig_name = ''.join(split_name[0:-2])
    return row, column, orig_name


for fullpath in path_boxes.iterdir():
    if os.path.isfile(fullpath):
        row, column, orig_name = parse_name(fullpath.name)
        with open(fullpath, 'r') as box_txt:
            boxes = box_txt.readlines()
            for box in boxes:                
                combined_boxes.append(offset_box(box, offset, row, column))


new_name = Path(path_save, f'{orig_name}.txt')
lines = []
for box in combined_boxes:
    lines.append('0 ' + ' '.join([str(elem) for elem in box]) + '\n')
with open(new_name, 'w') as combined_boxes_txt:
    combined_boxes_txt.writelines(lines)
