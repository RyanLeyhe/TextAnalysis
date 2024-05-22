import os
from config import Config
from txtFileReader import TextFileReader
from analysis import TextAnalysis
from csvWriter import CSVWriter

# Use the configuration (config.py) to set environment variables
if not os.getenv('GOOGLE_APPLICATION_CREDENTIALS'):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Config.GOOGLE_APPLICATION_CREDENTIALS

# Path to data folder
data_folder = Config.data_folder

# List to store the results
results = []

# Instantiate analyzer
analyzer = TextAnalysis()

# Iterate through each text file in the YouTube Data folder
for filename in os.listdir(data_folder):
    if filename.endswith(".txt"):
        file_path = os.path.join(data_folder, filename)
        text_content = TextFileReader.read_text_file(file_path)

        # Analyze entities and classification for the current text file:

        # Finds the most common consumer product mentioned
        entities_output = analyzer.most_common_product(text_content)

        # Classifies the type of content the video is about
        classification_output = analyzer.classify_content(text_content)

        # Store the results
        results.append((filename, entities_output, classification_output))

# Write the results to a CSV file using the CSVWriter class
csv_file_path = Config.csv_file
CSVWriter.write_results_to_csv(results, csv_file_path)

print(f"Results successfully written to {csv_file_path}")

# Note: if run multiple times, output.csv will be overwritten each time with new results
