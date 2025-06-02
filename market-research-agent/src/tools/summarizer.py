from typing import List

class Summarizer:
    def __init__(self):
        pass

    def summarize_text(self, text: str, max_length: int = 150) -> str:
        """
        Summarizes the given text to a specified maximum length.

        Args:
            text (str): The text to summarize.
            max_length (int): The maximum length of the summary.

        Returns:
            str: The summarized text.
        """
        # Placeholder for summarization logic
        # This could be replaced with an actual summarization algorithm
        if len(text) <= max_length:
            return text
        return text[:max_length] + '...'

    def extract_key_points(self, text: str) -> List[str]:
        """
        Extracts key points from the given text.

        Args:
            text (str): The text to analyze.

        Returns:
            List[str]: A list of key points extracted from the text.
        """
        # Placeholder for key point extraction logic
        # This could be replaced with an actual key point extraction algorithm
        sentences = text.split('. ')
        return [sentence for sentence in sentences if sentence]