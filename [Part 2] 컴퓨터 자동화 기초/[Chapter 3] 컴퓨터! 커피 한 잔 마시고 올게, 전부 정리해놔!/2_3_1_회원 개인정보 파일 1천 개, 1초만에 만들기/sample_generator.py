"""
Author : ByoungCheol Lee
GitHub : https://github.com/bcheollee
Book : 6개월 치 업무를 하루 만에 끝내는 업무 자동화
Last Modification : 2024.12.01
"""
import time
import random
import os
from pathlib import Path

def random_string(length):
    return ''.join(random.choices("abcdefghizklmnopqrstuvwxyz1234567890", k=length))

def random_name():
    return (random.choice("김이박최정강조윤장임") +
            random.choice("민서예지도하주윤채현지") +
            random.choice("준윤우원호후서연아은진"))

def generate_personal_info():
    name = random_name()
    return {
        "name": name,
        "age": str(random.randint(18, 85)),
        "e-mail": f"{random_string(8)}@bhban.com",
        "division": random_string(3),
        "telephone": f"010-{random.randint(0000, 9999):04d}-{random.randint(0000, 9999):04d}",
        "sex": random.choice(["male", "female"])
    }

def create_personal_info_files(num_samples, output_dir):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for i in range(num_samples):
        info = generate_personal_info()
        filename = output_path / f"{i}_{info['name']}.txt"

        with open(filename, 'w', encoding='utf-8') as outfile:
            for key, value in info.items():
                outfile.write(f"{key} : {value}\n")

def main():
    print("Process Start.")
    start_time = time.time()

    NUM_SAMPLES = 1000
    OUTPUT_DIR = "../2_3_2_회원 개인정보 파일 1천 개, 텍스트 파일 하나로 합치기/personal_info"

    create_personal_info_files(NUM_SAMPLES, OUTPUT_DIR)

    print("Process Done.")
    end_time = time.time()
    print(f"The Job Took {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()