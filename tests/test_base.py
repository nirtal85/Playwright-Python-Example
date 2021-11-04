def test_example(page, prep_properties):
    page.goto(prep_properties.config_section_dict("Base Url")["base_url"])
