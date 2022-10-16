class MyMixin(object):
    mixin_prop = ''

    def get_prop(self):
        return self.mixin_prop.capitalize()

    @staticmethod
    def get_upper(word):
        if isinstance(word, str):
            return word.capitalize()
        else:
            return word.title.capitalize()

