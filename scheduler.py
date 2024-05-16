# scheduler.py
import os
import schedule
import time
from dotenv import load_dotenv
from main import upload  # Importe a função upload diretamente

load_dotenv(override=True)


def get_schedule_time():
    schedule_time = os.getenv("SCHEDULE_TIME")
    return schedule_time

def job():
    print("Iniciando o upload para o S3...")
    upload()  # Chame a função upload diretamente

def main_upload():
    schedule_time = get_schedule_time()
    print(f"Scheduler agendado para executar diariamente às {schedule_time}")
    schedule.every().day.at(schedule_time).do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)  # Espera 1 minuto antes de verificar novamente

if __name__ == "__main__":
    main_upload()
