import watchdog
import csv
import sys
import time
from collections import Counter
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Initialize a Counter to count word occurrences
word_counter = Counter()

def count_words_and_update_csv():
    global word_counter
    global source_file_path
    global output_csv_path

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

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"Source file '{source_file_path}' has been modified.")
        count_words_and_update_csv()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python auto_update_word_count.py source_file.txt output_csv.csv")
        sys.exit(1)

    source_file_path = sys.argv[1]
    output_csv_path = sys.argv[2]

    # Initial word count and CSV creation
    count_words_and_update_csv()

    # Set up the watchdog observer to monitor the source file
    observer = Observer()
    event_handler = MyHandler()
    observer.schedule(event_handler, path=".", recursive=False)
    observer.start()

    try:
        print(f"Watching source file '{source_file_path}' for changes...")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()