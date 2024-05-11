from google.cloud import language_v2,  language_v1
from collections import Counter


def sample_analyze_entities(text_content: str = "This product is called a toy, i love toy.") -> None:
    """
    Analyzes Entities in a string.

    Args:
      text_content: The text content to analyze
    """

    client = language_v2.LanguageServiceClient()

    # Available types: PLAIN_TEXT, HTML
    document_type_in_plain_text = language_v2.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language_code = "en"
    document = {
        "content": text_content,
        "type_": document_type_in_plain_text,
        "language_code": language_code,
    }

    # Available values: NONE, UTF8, UTF16, UTF32.
    # See https://cloud.google.com/natural-language/docs/reference/rest/v2/EncodingType.
    encoding_type = language_v2.EncodingType.UTF8

    response = client.analyze_entities(
        request={"document": document, "encoding_type": encoding_type}
    )

    for entity in response.entities:
        print(f"Representative name for the entity: {entity.name}")

        # Get entity type, e.g. PERSON, LOCATION, ADDRESS, NUMBER, et al.
        # See https://cloud.google.com/natural-language/docs/reference/rest/v2/Entity#type.
        print(f"Entity type: {language_v2.Entity.Type(entity.type_).name}")

        if language_v2.Entity.Type(entity.type_).name == "CONSUMER_GOOD":
            print("check")
            print(entity.name)

        # Loop over the metadata associated with entity.
        # Some entity types may have additional metadata, e.g. ADDRESS entities
        # may have metadata for the address street_name, postal_code, et al.
        for metadata_name, metadata_value in entity.metadata.items():
            print(f"{metadata_name}: {metadata_value}")

        # Loop over the mentions of this entity in the input document.
        # The API currently supports proper noun mentions.
        for mention in entity.mentions:
            print(f"Mention text: {mention.text.content}")

            # Get the mention type, e.g. PROPER for proper noun
            print(f"Mention type: {language_v2.EntityMention.Type(mention.type_).name}")

            # Get the probability score associated with the first mention of the entity in the (0, 1.0] range.
            print(f"Probability score: {mention.probability}")

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    print(f"Language of the text: {response.language_code}")

    consumer_goods = []

    for entity in response.entities:
        if language_v2.Entity.Type(entity.type_).name == "CONSUMER_GOOD":
            print(entity.name)
            consumer_goods.append(entity.name.lower())

    counter = Counter(consumer_goods)
    most_common_good = counter.most_common(1)[0][0]
    print("most common good >")
    print(most_common_good)

def sample_classify_text(text_content):
    """
    Classifying Content in a String

    Args:
      text_content The text content to analyze.
    """

    global best
    client = language_v1.LanguageServiceClient()

    # text_content = "That actor on TV makes movies in Hollywood and also stars in a variety of popular new TV shows."

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}

    content_categories_version = (
        language_v1.ClassificationModelOptions.V2Model.ContentCategoriesVersion.V2
    )
    response = client.classify_text(
        request={
            "document": document,
            "classification_model_options": {
                "v2_model": {"content_categories_version": content_categories_version}
            },
        }
    )
    # Loop through classified categories returned from the API
    for category in response.categories:
        # Get the name of the category representing the document.
        # See the predefined taxonomy of categories:
        # https://cloud.google.com/natural-language/docs/categories
        print(f"Category name: {category.name}")
        # Get the confidence. Number representing how certain the classifier
        # is that this category represents the provided text.
        print(f"Confidence: {category.confidence}")

    print("max: >")

    print(max(response.categories, key=lambda x: x.confidence))

    output = max(response.categories, key=lambda x: x.confidence)

    formatted_response = f"{output.name} and Confidence {output.confidence}"
    print(formatted_response)

# sample_analyze_entities()
sample_classify_text("That actor on TV makes movies in Hollywood and also stars in a variety of popular new TV shows.")
