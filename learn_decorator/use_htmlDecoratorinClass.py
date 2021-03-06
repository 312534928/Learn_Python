def makeHtmlTag(tag, *args, **kwargs):
    def real_decorator(fn):
        css_class = " class='{0}' ".format(kwargs["css_class"])

        def wrapped(*args, **kwargs):
            return '<' + tag + css_class + fn(*args, **kwargs) + '</' + tag + '>'

        return wrapped

    return real_decorator


@makeHtmlTag(tag="b", css_class="bold_css")
@makeHtmlTag(tag="i", css_class="italic_css")
def hello():
    return "hello,world!"

print(hello())


class makeHtmlTagClass(object):

    def __init__(self, tag, css_class=""):
        self._tag = tag
        self._css_class = " class='{0}'".format(css_class) \
                                       if css_class !="" else ""

    def __call__(self, fn):
        def wrapped(*args, **kwargs):
            return "<" + self._tag + self._css_class+">"  \
                       + fn(*args, **kwargs) + "</" + self._tag + ">"
        return wrapped

@makeHtmlTagClass(tag="b", css_class="bold_css")
@makeHtmlTagClass(tag="i", css_class="italic_css")
def hello(name):
    return "Hello, {}".format(name)

print(hello("Hao Chen"))