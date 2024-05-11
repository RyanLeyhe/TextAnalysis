import csv


class CSVWriter:
    @staticmethod
    def write_results_to_csv(results, csv_file_path):
        """
        Write the analysis results to a CSV file where each record is a text file.

        Args:
            results: A list of tuples containing the analysis results.
                     Each tuple should have three elements: (filename, feature_1_output, feature_2_output).
            csv_file_path: The path to the CSV file to write the results.
        """
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['txt_file name', 'Most Common Product', 'Topic/Classification'])
            for result in results:
                writer.writerow(result)
