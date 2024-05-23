# Text Analysis in Python

## To Run

* Clone the GitHub Repo and run on any Python environment between versions 3.9 and 3.12!

    ### Usage

  * Change the config files to the appropriate paths and credentials:

  ```python
  class Config:
    GOOGLE_APPLICATION_CREDENTIALS = r'C:\path\to\project\project_filename.json'
  
    data_folder = r"C:\path\to\YoutubeData\Youtube Data"
  
    csv_file = "output.csv"
  
    @staticmethod
    def get_language_v1_client():
        return language_v1.LanguageServiceClient()
  
    @staticmethod
    def get_language_v2_client():
        return language_v2.LanguageServiceClient()
  ```
  
  ### Run configuration 

  * Simply run the main.py file!

  ### CSV output

  * Output is automatically written to a CSV file, 'output.csv', which is included in the root directory. 
    * Note: 'output.csv' is currently populated with the results from the given YouTube text files.

## Summary of Features

* Feature 1 is the most common consumer good/product mentioned in the transcript. 
  * This is done by inspecting the given text for known entities tagged with CONSUMER_GOOD by the API.
* Feature 2 is the most likely classification/genre of the video.
  * This is done by analyzing a document and returning a list of content categories that apply to the text found in the document. Using the API, I found the classification that was determined with the highest confidence.

## API Source: 
### https://cloud.google.com/python/docs/reference

* This project uses the Google Cloud Natural Language Python API.
  * More specifically the Python Cloud Client library, google-cloud-language. 
* This enabled Entity Analysis (Feature 1) and Content Classification (Feature 2).

## Challenges 

* The setup for Google Cloud, the associated API, Python virtual environment, and dependencies were the most difficult part of the project. Some of the documentation about Cloud Natural Language was surprisingly unclear which made going beyond the provided guides and code snippets more difficult.
