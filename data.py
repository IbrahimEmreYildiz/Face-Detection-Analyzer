from datetime import datetime
import csv


def save_data(face_count):
    with open("kayit.csv", mode='a', newline='')as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(),face_count])
        writer.writerow([])



