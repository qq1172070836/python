class Document(object):
    def __init__(self, name):
        self.name = name

    def show(self):
        raise NotImplementedError('必须重新父类方法')

class Pdf(Document):
    def show(self):
        return 'show pdf contents'

class Word(Document):
    def show(self):
        return 'show word contents'

pdf_obj = Pdf('财务账单.pdf')
word_obj = Word('简历.word')
print(pdf_obj.show())
print(word_obj.show())