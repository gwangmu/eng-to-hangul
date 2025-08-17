import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

from eng_to_hangul import interface as api
import logging as log

class EnglishtoHangul(toga.App):
    def startup(self):
        toga.Font.register("UnDotumAug", "resources/UnDotumAug.ttf")
        
        eng_label = toga.Label("English: ", text_align="left", width=100, margin=(0, 10))
        self.eng_input = toga.MultilineTextInput(on_change=self.on_eng_input, flex=1, font_size=30)
        ahan_label = toga.Label("Aug. Hangul: ", text_align="left", width=100, margin=(0, 10))
        self.ahan_output = toga.MultilineTextInput("adsfasdf", font_family="UnDotumAug", readonly=True, flex=1, font_size=30)

        self.eng_input.margin = (10, 10, 10, 10)
        self.ahan_output.margin = (10, 10, 10, 10)

        main_box = toga.Box(direction=COLUMN)
        main_box.add(eng_label)
        main_box.add(self.eng_input)
        main_box.add(ahan_label)
        main_box.add(self.ahan_output)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

        self.commands.clear()

    def on_eng_input(self, widget):
        pass_args = {}
        eng_sent = widget.value

        ipa_sent = api.convert(eng_sent, "eng", "ipa", pass_args)
        hcl_sent = api.convert(ipa_sent, "ipa", "hcl", pass_args)
        han_sent = api.convert(hcl_sent, "hcl", "han", pass_args)

        log.info("- eng: {}".format(eng_sent))
        log.info("- ipa: {}".format(ipa_sent))
        log.debug("- hcl: {}".format(hcl_sent))
        log.info("- han: {}".format(han_sent))

        self.ahan_output.value = api.get_ahan_sentence(hcl_sent)

def main():
    return EnglishtoHangul()
