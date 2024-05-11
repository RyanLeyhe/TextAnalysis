from google.cloud import language_v1, language_v2


class Config:
    GOOGLE_APPLICATION_CREDENTIALS = r'C:\Users\ryanl\TextAnalysis\burnished-ember-422919-s5-337e519fbbd2.json'

    data_folder = r"C:\Users\ryanl\TextAnalysis\YoutubeData\Youtube Data"

    csv_file = "output.csv"

    @staticmethod
    def get_language_v1_client():
        return language_v1.LanguageServiceClient()

    @staticmethod
    def get_language_v2_client():
        return language_v2.LanguageServiceClient()
