import datetime
import os
import sys
import csv
import string
import math
import sqlite3

sys.path.insert(0, "D:\\learning\\Python For DQE\\Python project\\Module 4")
from Homework_Module4_Python_Basics_Alena_Rakutova_2_1 import norm as normalization

from collections import Counter

word_counter = Counter()

lowercase_counter = Counter()
uppercase_counter = Counter()
letter_counter = Counter()

if len(sys.argv) > 5:
    db_file = sys.argv[5]
else:
    db_file = "../newsletter_database.db"

conn = sqlite3.connect(sys.argv[5])
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS News (
        id INTEGER PRIMARY KEY,
        header TEXT,
        text TEXT,
        City TEXT,
        Date_time TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS PrivateAd (
        id INTEGER PRIMARY KEY,
        header TEXT,
        text TEXT,
        date TEXT,
        days_left TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Feedback (
        id INTEGER PRIMARY KEY,
        header TEXT,
        text TEXT,
        feedback_value TEXT
    )
''')

conn.commit()


def count_words_and_update_csv():
    if len(sys.argv) > 2:
        source_file_path = sys.argv[2]
    else:
        source_file_path = "../Newsletter.txt"
    if len(sys.argv) > 3:
        output_csv_path = sys.argv[3]
    else:
        output_csv_path = "../word_count.csv"

    word_counter.clear()  # Clear the previous counts

    # Read the source file and count word occurrences
    with open(source_file_path, "r", encoding="utf-8") as file:
        for line in file:
            words = line.lower().split()
            word_counter.update(words)

    # Create a list of word-count pairs
    word_count_list = [(word, count) for word, count in word_counter.items()]

    # Sort the list by word
    word_count_list.sort(key=lambda x: x[0])

    # Create or update the CSV file with headers "Words" and "Count"
    with open(output_csv_path, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["Words", "Count"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()  # Write the header row

        for word, count in word_count_list:
            writer.writerow({"Words": word, "Count": count})


def count_letters_and_update_csv():
    if len(sys.argv) > 2:
        source_file_path = sys.argv[2]
    else:
        source_file_path = "../Newsletter.txt"
    if len(sys.argv) > 4:
        output_csv_path = sys.argv[4]
    else:
        output_csv_path = "../letters_count.csv"

    letter_counter.clear()  # Clear the previous letter counts
    uppercase_counter.clear()  # Clear the previous uppercase counts
    lowercase_counter.clear()  # Clear the previous lowercase counts

    # Read the source file and count letter occurrences
    with open(source_file_path, "r", encoding="utf-8") as file:
        for line in file:
            # Remove non-letter characters
            letters = ''.join(filter(str.isalpha, line))
            lowercase_letters = [letter for letter in letters if letter.islower()]
            uppercase_letters = [letter for letter in letters if letter.isupper()]

            letter_counter.update(letters)
            uppercase_counter.update(uppercase_letters)
            lowercase_counter.update(lowercase_letters)

    # Create a list of letter-count pairs
    letter_count_list = []

    for letter in string.ascii_lowercase:
        count_all = letter_counter[letter] + letter_counter[letter.upper()]
        count_uppercase = letter_counter[letter.upper()]
        if count_all > 0:
            percentage = math.ceil((count_uppercase / count_all) * 100)
        else:
            percentage = 0
        letter_count_list.append((letter, count_all, count_uppercase, percentage))

    # Create or update the CSV file with headers
    with open(output_csv_path, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["letter", "count_all", "count_uppercase", "percentage"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()  # Write the header row

        for letter, count_all, count_uppercase, percentage in letter_count_list:
            writer.writerow({"letter": letter, "count_all": count_all, "count_uppercase": count_uppercase,
                             "percentage": percentage})


class UserInformationCollector:

    def __init__(self):
        self.news = ""
        self.city = ""
        self.date = datetime.datetime.now().strftime("%d/%m/%Y %H.%M")
        self.ads = ""
        self.feedback_map = {
            "1": "★",
            "2": "★★",
            "3": "★★★",
            "4": "★★★★",
            "5": "★★★★★"}
        self.feedback = ""
        self.feedback_value = ""
        self.header = ""
        self.footer = ""
        self.file_path = sys.argv[2]
        self.date_time = ""
        self.days_left = ""
        self.db_file = sys.argv[5]
        self.conn = sqlite3.connect(self.db_file)

    def transfer_news(self, news_info):
        if len(news_info) >= 3:
            self.header = news_info[0]
            self.news = news_info[1]
            city_date_time = news_info[2]
            city, date_time = city_date_time.split(', ')
            self.city = city
            self.date_time = date_time

    def transfer_private_ad(self, ad_info):
        if len(ad_info) >= 3:
            self.header = ad_info[0]
            self.ads = ad_info[1]
            date_and_days_left = ad_info[2]
            date_parts = date_and_days_left.split(', ')
            if len(date_parts) == 2:
                date_str, days_left_text = date_parts
                date = date_str.split(': ')[1]
                days_left = int(days_left_text.split(' ')[0])
            else:
                date = ""
                days_left = 0
            self.date = date
            self.days_left = days_left

    def transfer_feedback(self, feedback_info):
        if len(feedback_info) >= 3:
            self.header = feedback_info[0]
            self.feedback = feedback_info[1]
            num_stars = 0
            for line in feedback_info:
                if line.startswith("My feedback is:"):
                    feedback_text = line[len("My feedback is: "):].strip()
                    num_stars = feedback_text.count("★")
            self.feedback_value = num_stars

    def newsletterTrasformation(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        section = None
        entry = []

        for line in lines:
            line = line.strip()
            if line == "News -------------------------" or line == "Private Ad" or line == "Feedback":
                if entry:
                    if section == "News -------------------------":
                        self.transfer_news(entry)
                    elif section == "Private Ad":
                        self.transfer_private_ad(entry)
                    elif section == "Feedback":
                        self.transfer_feedback(entry)
                    self.insert_into_database()
                    entry = []
                section = line
            else:
                entry.append(line)

        if entry:
            if section == "News -------------------------":
                self.transfer_news(entry)
            elif section == "Private Ad":
                self.transfer_private_ad(entry)
            elif section == "Feedback":
                self.transfer_feedback(entry)
            self.insert_into_database()

    def insert_into_database(self):
        with self.conn:
            cursor = self.conn.cursor()

        if self.header == "News -------------------------":
            cursor.execute("INSERT INTO News (header, text, City, Date_time) VALUES (?, ?, ?, ?)",
                            (self.header, self.news, self.city, self.date_time))
        elif self.header == "Private Ad":
            cursor.execute("INSERT INTO PrivateAd (header, text, date, days_left) VALUES (?, ?, ?, ?)",
                            (self.header, self.ads, self.date, self.days_left))
        elif self.header == "Feedback":
            cursor.execute("INSERT INTO Feedback (header, text, feedback_value) VALUES (?, ?, ?)",
                            (self.header, self.feedback, self.feedback_value))

    def validate_future_date(self, input_date):
        try:
            input_date = datetime.datetime.strptime(input_date, "%d/%m/%Y")
            current_date = datetime.datetime.now()
            return input_date > current_date
        except ValueError:
            return False

    def process_news(self, news_info):
        if len(news_info) >= 2:
            self.header = "News -------------------------"
            self.news = news_info[0]
            self.city = news_info[1]
            self.date = datetime.datetime.now().strftime("%d/%m/%Y %H.%M")
            self.footer = f"{self.city}, {self.date}"

    def process_private_ad(self, ad_info):
        if len(ad_info) >= 2:
            self.header = "Private Ad ------------------"
            self.ads = ad_info[0]
            self.date = ad_info[1]
            days_left = (datetime.datetime.strptime(self.date, "%d/%m/%Y") - datetime.datetime.now()).days
            self.footer = f"Actual until: {self.date}, {days_left} days left"

    def process_feedback(self, feedback_info):
        if len(feedback_info) >= 2:
            self.header = "Feedback ------------------"
            feedback_value = feedback_info[0]
            self.feedback_value = self.feedback_map.get(feedback_value, "")
            self.feedback = feedback_info[1]
            self.footer = f"My feedback is: {self.feedback_value}"

    def validate_file_format(self, lines):
        news_section_found = False
        feedback_section_found = False
        ad_section_found = False
        news_text = False
        news_city = False
        ad_date_valid = False
        ad_text = False
        feedback_mark = False
        feedback_text = False

        for line in lines:
            line = line.strip()
            if line == "News":
                news_section_found = True
                news_text = False
                news_city = False
            elif line == "Private Ad":
                ad_section_found = True
                ad_text = False
                ad_date_valid = False
            elif line == "Feedback":
                feedback_section_found = True
                feedback_mark = False
                feedback_text = False
            elif news_section_found and not news_text:
                self.news = line
                news_text = True
            elif news_section_found and not news_city:
                self.news = line
                news_city = True
            elif ad_section_found and not ad_text:
                self.ads = line
                ad_text = True
            elif ad_section_found and not ad_date_valid and self.validate_future_date(line):
                self.date = line
                ad_date_valid = True
            elif feedback_section_found and not feedback_mark and line in self.feedback_map.keys():
                feedback_mark = True
            elif feedback_section_found and not feedback_text:
                self.feedback = line
                feedback_text = True

        return (
                news_section_found
                and feedback_section_found
                and ad_section_found
                and news_text
                and ad_date_valid
                and ad_text
                and feedback_text
                and feedback_mark
        )

    def save_to_file(self):
        main_title = "News feed:"

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as file:
                file.write(main_title + "\n")

        with open(self.file_path, "a", encoding="utf-8") as file:
            file.write("\n")
            file.write(self.header + "\n")
            if self.header == "News -------------------------":
                normalized_news = normalization(self.news)
                file.write(f"{normalized_news}\n")
                file.write(f"{self.footer}\n")
            elif self.header == "Private Ad ------------------":
                normalized_ads = normalization(self.ads)
                file.write(f"{normalized_ads}\n")
                file.write(f"{self.footer}\n")
            elif self.header == "Feedback ------------------":
                normalized_feedback = normalization(self.feedback)
                file.write(f"{normalized_feedback}\n")
                file.write(f"{self.footer}\n")

    def collect_information(self):
        print("Choose an option:")
        print("1. Want to post News")
        print("2. Want to post Private Ad")
        print("3. Want to leave a Feedback")
        print("4. Want to upload a File with Information")
        print("5. Skip")

        choice = input("Enter your choice (1, 2, 3, 4, 5): ")

        if choice == "1":
            self.collect_news()
            self.header = f"News -------------------------"

        elif choice == "2":
            self.header = f"Private Ad ------------------"
            self.collect_private_ad()

        elif choice == "3":
            self.header = f"Feedback ------------------"
            self.collect_feedback()

        elif choice == "4":
            self.collect_information_from_file()

        elif choice == "5":
            print("Skipping information collection.")
        else:
            print("Invalid choice. Please choose 1 or 2 or 3 or 4 or 5.")
        if choice != "5" and choice != "4":
            self.save_to_file()
            print(f"Information appended to {self.file_path}")

    def collect_news(self):
        self.news = input("Enter your news: ")
        while not self.news:
            print("News cannot be empty. Please enter News.")
            self.news = input("Enter your news: ")

        self.city = input("Enter city:")
        while not self.city:
            print("City cannot be empty. Please enter City.")
            self.city = input("Enter your city:")
        print("Information collected successfully!")

        self.footer = f"{self.city}, {self.date}"

    def collect_private_ad(self):
        self.ads = input("Enter your Private Ad: ")
        while not self.ads:
            print("Ad cannot be empty. Please enter Information.")
            self.ads = input("Enter your Private Ad: ")
        new_date = input("Enter the date and time (dd/mm/yyyy): ")
        while not self.validate_future_date(new_date):
            print("Invalid date. Please enter a future date.")
            new_date = input("Enter the date (dd/mm/yyyy): ")
        self.date = new_date
        print("Information collected successfully!")

        days_left = (datetime.datetime.strptime(self.date, "%d/%m/%Y") - datetime.datetime.now()).days

        self.footer = f"Actual until: {self.date}, {days_left} days left"

    def collect_feedback(self):
        print("Please provide feedback:")
        print("1. Very Dissatisfied")
        print("2. Dissatisfied")
        print("3. Neutral")
        print("4. Satisfied")
        print("5. Very Satisfied")

        valid_choices = {"1", "2", "3", "4", "5"}
        choice = input("Enter your choice (1-5): ")

        while choice not in valid_choices:
            print("Invalid choice. Please choose a number from 1 to 5.")
            choice = input("Enter your choice (1-5): ")

        self.feedback_map = self.feedback_map[choice]

        self.feedback = input("Enter your Feedback: ")
        while not self.feedback:
            print("Feedback cannot be empty. Please enter Information.")
            self.feedback = input("Enter your Feedback:")
        self.footer = f"My feedback is: {self.feedback_map}"

    def collect_information_from_file(self):
        default_file_path = sys.argv[1]

        if not os.path.exists(default_file_path):
            print("Default file not found.")
            return

        with open(default_file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        if not self.validate_file_format(lines):
            print("Incorrect file format. Please check the file.")
            return

        section = None
        entry = []

        for line in lines:
            line = line.strip()
            if line == "News" or line == "Private Ad" or line == "Feedback":
                if entry:
                    if section == "News":
                        self.process_news(entry)
                    elif section == "Private Ad":
                        self.process_private_ad(entry)
                    elif section == "Feedback":
                        self.process_feedback(entry)
                    self.save_to_file()
                    entry = []
                section = line
            else:
                entry.append(line)
        # Process and save the last entry
        if entry:
            if section == "News":
                self.process_news(entry)
            elif section == "Private Ad":
                self.process_private_ad(entry)
            elif section == "Feedback":
                self.process_feedback(entry)
            self.save_to_file()
        print("Information collected from file.")
        # Remove the source file
        #os.remove(default_file_path)
        #print("Source file is removed.")


def main():
    user_collector = UserInformationCollector()
    user_collector.collect_information()
    user_collector.newsletterTrasformation()

    print("Information saved to file and database.")

    if len(sys.argv) != 6:
        sys.exit(1)
    # Word count and CSV creation
    count_words_and_update_csv()
    print("Usage: python update Count in word_count.csv")
    # Letter count and CSV creation
    count_letters_and_update_csv()
    print("Usage: python update Count in letters_count.csv")


if __name__ == "__main__":
    main()
