from mako.template import Template
from markdown import markdown
from glob import glob
import json
from os import path

def load_template(input_dir):
    template_path = path.join(input_dir, "template.html")
    assert path.exists(template_path)
    return Template(open(template_path).read())

def load_config(input_dir):
    config_path = path.join(input_dir, "config.json")
    assert path.exists(config_path)
    return json.load(open(config_path))

def load_input_files(input_dir):
    assert path.exists(input_dir)
    return glob(path.join(input_dir, "*.md"))

def render_page(md_name, config, template):
    # convert it to html
    contents = markdown(open(md_name).read())

    # add it to the config variables
    config['contents'] = contents
    # process the template

    return template.render(**config)

def save_result(output_dir, md_name, html):
    fname, ext = path.splitext(path.basename(md_name))
    out_name = path.join(output_dir, fname) + ".html"

    with open(out_name, 'w') as f:
        f.write(html)

def main(input_dir, output_dir):
    """
    Takes an input directory and output directory
    to produce the blog.  The input directory needs to have
    a template.html, a config.json, and *.md files to process.
    """

    # load the template file
    template = load_template(input_dir)

    # load the config.json as a dict
    config = load_config(input_dir)

    # list all the .md files
    md_files = load_input_files(input_dir)

    # go through each .md file and
    for md_name in md_files:
        # render it
        html = render_page(md_name, config, template)
        # save it in the proper location
        save_result(output_dir, md_name, html)

