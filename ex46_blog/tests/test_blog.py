from blog.run import *
import pytest
import os

def test_load_template():
    with pytest.raises(AssertionError):
        load_template("tests/doesnotexist")
    template = load_template("tests/sample")
    assert template
    return template

def test_load_config():
    with pytest.raises(AssertionError):
        load_config("tests/doesnotexist")

    config = load_config("tests/sample")
    assert config['title'] == "Zed's Blog"
    return config

def test_load_input_files():
    with pytest.raises(AssertionError):
        load_input_files("tests/doesnotexist")

    files = load_input_files("tests/sample")
    assert "tests/sample/index.md" in files
    return files

def test_render_page():
    template = test_load_template()
    config = test_load_config()
    files = test_load_input_files()

    html = render_page(files[0], config, template)
    assert "Zed's" in html
    assert "Hello There" in html
    return files[0], html

def test_save_result():
    md_name, html = test_render_page()
    output_dir = "tests/output"
    save_result(output_dir, md_name, html)
    assert os.path.exists("tests/output/index.html")



