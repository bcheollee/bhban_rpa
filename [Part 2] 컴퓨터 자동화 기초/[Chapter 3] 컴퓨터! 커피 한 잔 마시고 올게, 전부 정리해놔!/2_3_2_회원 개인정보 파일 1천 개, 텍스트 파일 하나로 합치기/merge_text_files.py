"""
Author : ByoungCheol Lee
GitHub : https://github.com/bcheollee
Book : 6개월 치 업무를 하루 만에 끝내는 업무 자동화
Last Modification : 2024.12.01.
"""

import time
import os
import logging
from pathlib import Path


def merge_files(directory, outfile_name):
    # 작업 시작 메시지를 로깅합니다.
    logging.info("프로세스 시작")

    start_time = time.time()

    directory_path = Path(directory)
    outfile_path = Path(outfile_name)

    try:
        # 결과물 파일을 생성합니다.
        with outfile_path.open('w', encoding='utf-8') as out_file:
            # 폴더의 내용물을 열람해 목록을 생성합니다.
            for file_path in directory_path.glob('*.txt'):
                try:
                    # 텍스트 파일을 읽어옵니다.
                    with file_path.open('r', encoding='utf-8') as file:
                        content = file.read()
                        # 파일의 내용물을 결과물 파일에 기재합니다.
                        out_file.write(content + "\n\n")
                except IOError as e:
                    logging.error(f"{file_path} 파일 읽기 오류: {e}")

        logging.info("프로세스 완료")

        end_time = time.time()
        logging.info(f"작업 소요 시간: {end_time - start_time:.2f}초")

    except IOError as e:
        logging.error(f"결과 파일 {outfile_name} 쓰기 오류: {e}")


if __name__ == "__main__":
    # 로깅 설정
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # 하나로 합칠 파일들이 저장된 폴더 이름을 적어주세요.
    directory = "personal_info"

    # 결과물 파일의 이름을 정의합니다.
    outfile_name = "merged_ID.txt"

    merge_files(directory, outfile_name)