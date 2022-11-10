from Stack import Stack
from html.parser import  HTMLParser

class MyHtmlParser(HTMLParser):
    def __init__(self, *, convert_charrefs: bool = ...) -> None:
        super().__init__(convert_charrefs=convert_charrefs)
        self.rawdata = ''
        self.stack = Stack()
        self.unclosed_tag = ''
  
    def handle_starttag(self, tag, attrs):
        if not tag in ['meta']:
            self.stack.push(tag)
            return(f"Pushed Start Tag: {tag}")

    def handle_endtag(self, tag):
        if tag == self.stack.peek():
            self.stack.pop()
            return(f"Popped End Tag: {tag}")
        else:
            if self.unclosed_tag == '':
                self.unclosed_tag = self.stack.peek()

    def validate_text(self):

        if self.unclosed_tag == '':
            return 'Valid HTML'
        else:
            return f'Invalid HTML, mismatched opening and closing for tag "<{self.unclosed_tag}>"'

class HtmlValidator():
    def __init__(self) -> None:
        self.file_path = None
        self.read_text = ''
        self.import_file()
        self.read_file()
        htmlParser = MyHtmlParser()
        htmlParser.feed(self.read_text)
        print(htmlParser.validate_text())
        return
    def import_file(self):
        self.file_path = input('Enter path of the Html File: \n')

    def read_file(self):
        with open(self.file_path) as f:
            self.read_text = f.read()

    def return_calss(self):
        return
        # self.html_tags = re.findall(self.html_tag_regex, self.read_text)

htmlValidator = HtmlValidator()

# C:\Users\user\Documents\Python\linkedListStack\sampleHtmlFile.html