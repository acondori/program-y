import unittest

from programy.config.file.yaml_file import YamlConfigurationFile
from programy.config.sections.bot.spelling import BotSpellingConfiguration
from programy.config.sections.client.console import ConsoleConfiguration

class BotSpellingConfigurationTests(unittest.TestCase):

    def test_with_data(self):
        yaml = YamlConfigurationFile()
        self.assertIsNotNone(yaml)
        yaml.load_from_text("""
        bot:
            spelling:
              classname: programy.utils.spelling.checker.SpellingChecker
              corpus: $BOT_ROOT/corpus.txt
              alphabet: abcdefghijklmnopqrstuvwxyz
              check_before: true
              check_and_retry: true
        """, ConsoleConfiguration(), ".")

        bot_config = yaml.get_section("bot")

        spelling_config = BotSpellingConfiguration()
        spelling_config.load_config_section(yaml, bot_config, ".")

        self.assertEquals("programy.utils.spelling.checker.SpellingChecker", spelling_config.classname)
        self.assertEquals("./corpus.txt", spelling_config.corpus)
        self.assertEquals("abcdefghijklmnopqrstuvwxyz", spelling_config.alphabet)
        self.assertTrue(spelling_config.check_before)
        self.assertTrue(spelling_config.check_and_retry)

    def test_without_data(self):
        yaml = YamlConfigurationFile()
        self.assertIsNotNone(yaml)
        yaml.load_from_text("""
        bot:
            spelling:
        """, ConsoleConfiguration(), ".")

        bot_config = yaml.get_section("bot")

        spelling_config = BotSpellingConfiguration()
        spelling_config.load_config_section(yaml, bot_config, ".")

        self.assertIsNone(spelling_config.classname)
        self.assertIsNone(spelling_config.corpus)
        self.assertIsNone(spelling_config.alphabet)
        self.assertFalse(spelling_config.check_before)
        self.assertFalse(spelling_config.check_and_retry)

    def test_with_no_data(self):
        yaml = YamlConfigurationFile()
        self.assertIsNotNone(yaml)
        yaml.load_from_text("""
        bot:
        """, ConsoleConfiguration(), ".")

        bot_config = yaml.get_section("bot")

        spelling_config = BotSpellingConfiguration()
        spelling_config.load_config_section(yaml, bot_config, ".")

        self.assertIsNone(spelling_config.classname)
        self.assertIsNone(spelling_config.corpus)
        self.assertIsNone(spelling_config.alphabet)
        self.assertFalse(spelling_config.check_before)
        self.assertFalse(spelling_config.check_and_retry)
