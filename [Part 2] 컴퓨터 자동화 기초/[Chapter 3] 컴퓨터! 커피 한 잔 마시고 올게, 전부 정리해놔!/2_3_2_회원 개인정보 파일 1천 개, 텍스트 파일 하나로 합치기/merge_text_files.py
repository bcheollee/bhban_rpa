"""
Author : ByoungCheol Lee
GitHub : https://github.com/bcheollee
Book : 6개월 치 업무를 하루 만에 끝내는 업무 자동화
Last Modification : 2024.12.01.
"""

import time
import logging
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_file(file_path):
    try:
        with file_path.open('r', encoding='utf-8') as file:
            return file.read() + "\n\n"
    except IOError as e:
        logging.error(f"{file_path} 파일 읽기 오류: {e}")
        return ""

def merge_files(directory, outfile_name):
    logging.info("프로세스 시작")
    start_time = time.time()

    directory_path = Path(directory)
    outfile_path = Path(outfile_name)

    try:
        with outfile_path.open('w', encoding='utf-8') as out_file:
            with ThreadPoolExecutor() as executor:
                futures = [executor.submit(read_file, file_path) for file_path in directory_path.glob('*.txt')]
                for future in as_completed(futures):
                    out_file.write(future.result())

        logging.info("프로세스 완료")
        end_time = time.time()
        logging.info(f"작업 소요 시간: {end_time - start_time:.2f}초")

    except IOError as e:
        logging.error(f"결과 파일 {outfile_name} 쓰기 오류: {e}")

if __name__ == "__main__":
    directory = "personal_info"
    outfile_name = "merged_ID.txt"
    merge_files(directory, outfile_name)