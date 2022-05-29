from pathlib import Path

BASE_IMAGES = Path('tester/image_prep/images')
CONVERSION_IMAGES = Path('tester/control/conversion')

YOLO_CONFIG = Path('tester/models/warlus_3/yolov3.cfg')
YOLO_WEIGHT = Path('tester/models/warlus_3/warlus.weights')
YOLO_LABELS = Path('tester/models/warlus_3/coco.names')

CSV_DIR = Path('tester/control/csv')
