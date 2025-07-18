import logging
import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

log_progress = logging.getLogger(__name__)
log_progress.setLevel(logging.INFO)


formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
progress_handler = logging.FileHandler(f"./.logs/progress_{current_time}.txt")

progress_handler.setFormatter(formatter)
log_progress.addHandler(progress_handler)