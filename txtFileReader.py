class TextFileReader:
    @staticmethod
    def read_text_file(file_path: str) -> str:
        """
        Read the content of a text file.

        Args:
          file_path: The path to the text file to read.

        Returns:
          The content of the text file as a string.
        """
        with open(file_path, "r", encoding="utf-8") as file:
            text_content = file.read()
        return text_content
