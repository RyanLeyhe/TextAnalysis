import os
from google.cloud import language_v1  # Imports the Google Cloud client library

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\ryanl\TextAnalysis\burnished-ember-422919-s5-337e519fbbd2' \
                                               r'.json '

google_application_credentials = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

# Instantiates a client
client = language_v1.LanguageServiceClient()

# The text to analyze
text = "Hello, world!"
document = language_v1.types.Document(
    content=text, type=language_v1.types.Document.Type.PLAIN_TEXT
)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(
    request={"document": document}
).document_sentiment

print(f"Text: {text}")
print(f"Sentiment: {sentiment.score}, {sentiment.magnitude}")
