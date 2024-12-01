"""
Author : ByoungCheol Lee
GitHub : https://github.com/bcheollee
Book : 6개월 치 업무를 하루 만에 끝내는 업무 자동화
Last Modification : 2024.12.01
"""
import time
import random
import logging
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

FIRST_NAMES = "김이박최정강조윤장임"
MIDDLE_NAMES = "민서예지도하주윤채현지"
LAST_NAMES = "준윤우원호후서연아은진"
DIVISIONS = ["HR", "IT", "FIN", "MKT", "OPS", "R&D", "SAL"]

def random_string(length):
    return ''.join(random.choices("abcdefghizklmnopqrstuvwxyz1234567890", k=length))

def random_name():
    return random.choice(FIRST_NAMES) + random.choice(MIDDLE_NAMES) + random.choice(LAST_NAMES)

def generate_personal_info():
    name = random_name()
    return {
        "name": name,
        "age": str(random.randint(18, 85)),
        "e-mail": f"{random_string(8)}@bhban.com",
        "division": random.choice(DIVISIONS),
        "telephone": f"010-{random.randint(0, 9999):04d}-{random.randint(0, 9999):04d}",
        "sex": random.choice(["male", "female"])
    }

def create_personal_info_file(args):
    i, output_path = args
    info = generate_personal_info()
    filename = output_path / f"{i}_{info['name']}.txt"

    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write('\n'.join(f"{key} : {value}" for key, value in info.items()))

def create_personal_info_files(num_samples, output_dir):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(create_personal_info_file, (i, output_path)) for i in range(num_samples)]
        for future in as_completed(futures):
            future.result()  # This will raise any exceptions that occurred during execution

def main():
    logging.info("프로세스 시작")
    start_time = time.time()

    NUM_SAMPLES = 1000
    OUTPUT_DIR = "../2_3_2_회원 개인정보 파일 1천 개, 텍스트 파일 하나로 합치기/personal_info"

    create_personal_info_files(NUM_SAMPLES, OUTPUT_DIR)

    logging.info("프로세스 완료")
    end_time = time.time()
    logging.info(f"The Job Took {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()