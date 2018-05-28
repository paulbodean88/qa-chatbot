"""

Python wrapper over aiml package. It provides basic functions used to communicate with the chatbot
"""
import aiml
import os

from src.chat_executor import chat_executor
from src.qa_scenarios.wiki_search_click import WikiActions


class BotTrainer:
    def __init__(self):
        self._kernel = aiml.Kernel()

    def _start_chat(self):
        """

        Start the communication with the bot
        """
        executor = WikiActions()
        while True:
            message = input("Enter your message to the bot: ")
            if message == "quit":
                exit()
            elif message == "save":
                self._kernel.saveBrain("public/bot_brain.brn")
            else:
                chat_executor(message, executor, 70)
                print(self._kernel.respond(message))

    def simple_learning(self, pattern):
        """
        Train the bot based on a pre-defined pattern
        :param pattern: pattern used to train the bot
        """
        self._kernel.learn("public/std-startup.xml")
        self._kernel.respond(pattern)
        self._start_chat()

    def brain_learning(self, pattern):
        """
        Train the bot based on a pre-defined pattern including a storage option into the brain bot of some actions
        :param pattern: pattern used to train the bot
        """
        if os.path.isfile("bot_brain.brn"):
            self._kernel.bootstrap(brainFile="public/bot_brain.brn")
        else:
            self._kernel.bootstrap(learnFiles="public/std-startup.xml", commands=pattern)
            self._kernel.saveBrain("public/bot_brain.brn")
        self._start_chat()
