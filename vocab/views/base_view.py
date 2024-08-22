from questionary import prompt

class BaseView:
    template = []

    def __call__(self, *args, **kwargs):
        prompt(self.get_template(*args, **kwargs))

    def get_template(self, *args, **kwargs):
        return self.template
