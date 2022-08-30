from mycroft import MycroftSkill, intent_file_handler


class SirTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('test.sir.intent')
    def handle_test_sir(self, message):
        self.speak_dialog('test.sir')


def create_skill():
    return SirTest()

