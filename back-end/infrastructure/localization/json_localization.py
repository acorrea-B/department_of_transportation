import json
from application.ports.i_localization_repository import ILocalizationRespository


class JSONLocalizationAdapter(ILocalizationRespository):
    def __init__(self, language="en", path=""):
        """
        Initializes the JSONLocalizationAdapter with the specified language and path.

        Args:
            language (str, optional): The language code to use for localization. Defaults to "en".
            path (str, optional): The path to the directory containing the localization files. Defaults to "".
        """
        self.messages = self.load_messages(language, path)

    def load_messages(self, lang, path):
        """
        Loads the localization messages from the specified language file.

        Args:
            lang (str): The language code.
            path (str): The path to the directory containing the localization files.

        Returns:
            dict: A dictionary containing the loaded messages.
        """
        try:
            with open(f"{path}messages_{lang}.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def get_message(self, key):
        """
        Retrieves the localized message for the specified key.

        Args:
            key (str): The key of the message to retrieve.

        Returns:
            str: The localized message if found, otherwise "Undefined message".
        """
        return self.messages.get(key, "Undefined message")
