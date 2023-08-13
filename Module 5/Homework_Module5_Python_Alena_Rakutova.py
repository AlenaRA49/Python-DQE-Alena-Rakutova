#Create a tool, which will do user generated news feed:
# 1.User select what data type he wants to add
# 2.Provide record type required data
# 3.Record is published on text file in special format
# You need to implement:
# 1.News – text and city as input. Date is calculated during publishing.
# 2.Privat ad – text and expiration date as input. Day left is calculated during publishing.
# 3.Your unique one with unique publish rules.
import datetime
import os

class UserInformationCollector:
    def __init__(self):
        self.news = ""
        self.city = ""
        self.date = datetime.datetime.now().strftime("%d/%m/%Y %H.%M")
        self.ads = ""
        self.feedback = ""
        self.header = ""
        self.footer = ""
        self.file_path = r"D:\Newsletter.txt"

    def validate_future_date(self, input_date):
        try:
            input_date = datetime.datetime.strptime(input_date, "%d/%m/%Y")
            current_date = datetime.datetime.now()
            return input_date > current_date
        except ValueError:
            return False

    def collect_information(self):
        print("Choose an option:")
        print("1. Want to post News")
        print("2. Want to post Private Ad")
        print("3. Want to leave a Feedback")
        print("4. Skip")

        choice = input("Enter your choice (1, 2, 3 or 4): ")

        if choice == "1":
            self.header = f"News -------------------------"
            self.news = input("Enter your news: ")
            while not self.news:
                print("News cannot be empty. Please enter News.")
                self.news = input("Enter your news: ")

            self.city = input("Enter city:")
            while not self.city:
                print("City cannot be empty. Please enter City.")
                self.city = input("Enter your city: ")
            print("Information collected successfully!")

            self.footer = f" {self.city}, {self.date}"

        elif choice == "2":
            self.header = f"Private Ad ------------------"
            self.ads = input("Enter your Private Ad: ")
            while not self.ads:
                print("Ad cannot be empty. Please enter Information.")
                self.ads = input("Enter your Private Ad: ")
            new_date = input("Enter the date and time (dd/mm/yyyy): ")
            while not self.validate_future_date(new_date):
                print("Invalid date. Please enter a future date.")
                new_date = input("Enter the date and time (dd/mm/yyyy): ")
            self.date = new_date
            print("Information collected successfully!")

            days_left = (datetime.datetime.strptime(self.date, "%d/%m/%Y") - datetime.datetime.now()).days

            self.footer = f"Actual until: {self.date}, {days_left} days left"

        elif choice == "3":
            self.header = "Feedback ------------------"
            self.collect_feedback()

        elif choice == "4":
            print("Skipping information collection.")
        else:
            print("Invalid choice. Please choose 1 or 2 or 3 or 4.")

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

        feedback_map = {
            "1": "★",
            "2": "★★",
            "3": "★★★",
            "4": "★★★★",
            "5": "★★★★★"
        }
        self.feedback = input("Enter your Feedback: ")
        while not self.feedback:
            print("Feedback cannot be empty. Please enter Information.")
            self.feedback = input("Enter your Feedback: ")
        self.footer = f"My feedback is: {feedback_map[choice]}"

    def save_to_file(self):
        file_path = r"D:\Newsletter.txt"
        main_title = "News feed:"

        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                file.write(main_title + "\n")

        with open(file_path, "a", encoding="utf-8") as file:
            file.write("\n")
            file.write(self.header + "\n")
            if self.header == "News -------------------------":
                file.write(f"{self.news}\n")
                file.write(f"{self.footer}\n")
            elif self.header == "Private Ad ------------------":
                file.write(f"{self.ads}\n")
                file.write(f"{self.footer}\n")
            elif self.header == "Feedback ------------------":
                file.write(f"{self.feedback}\n")
                file.write(f"{self.footer}\n")

def main():
    user_collector = UserInformationCollector()
    user_collector.collect_information()
    user_collector.save_to_file()
    print(f"Information appended to {user_collector.file_path}")

if __name__ == "__main__":
    main()