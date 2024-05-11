from google.cloud import language_v1, language_v2
from config import Config
from collections import Counter


class TextAnalysis:

    @staticmethod
    def most_common_product(text_content: str):
        """
        Finds the most common consumer product in the text.

        Args:
          text_content: The text content to analyze
        """

        text_content_short = text_content[:1000]

        document_type_in_plain_text = language_v2.Document.Type.PLAIN_TEXT

        language_code = "en"
        document = {
            "content": text_content_short,
            "type_": document_type_in_plain_text,
            "language_code": language_code,
        }

        encoding_type = language_v2.EncodingType.UTF8

        client_v2 = Config.get_language_v2_client()

        response = client_v2.analyze_entities(
            request={"document": document, "encoding_type": encoding_type}
        )

        consumer_goods = []

        for entity in response.entities:
            if language_v2.Entity.Type(entity.type_).name == "CONSUMER_GOOD":
                consumer_goods.append(entity.name.lower())

        counter = Counter(consumer_goods)
        if counter:
            most_common_good = counter.most_common(1)[0][0]
            return most_common_good
        else:
            return "No consumer good detected"

    @staticmethod
    def classify_content(text_content: str):
        """
        Tags the content with a classification.

        Args:
          text_content The text content to analyze
        """

        text_content_short = text_content[:1000]

        type_ = language_v1.Document.Type.PLAIN_TEXT

        client_v1 = Config.get_language_v1_client()

        language = "en"
        document = {"content": text_content_short, "type_": type_, "language": language}

        content_categories_version = (
            language_v1.ClassificationModelOptions.V2Model.ContentCategoriesVersion.V2
        )
        response = client_v1.classify_text(
            request={
                "document": document,
                "classification_model_options": {
                    "v2_model": {"content_categories_version": content_categories_version}
                },
            }
        )

        output = max(response.categories, key=lambda x: x.confidence)
        formatted_response = f"{output.name} with Confidence {output.confidence}"

        return formatted_response
