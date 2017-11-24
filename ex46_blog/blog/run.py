from mako.template import Template
from markdown import markdown

def main(argv):
    text = "hello *${data}!*"
    md = markdown(text)
    print(Template(md).render(data="world"))


