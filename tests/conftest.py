import pytest

from utils.config_parser import ConfigParserIni


@pytest.fixture(scope="session")
# instantiates ini file parses object
def prep_properties():
    return ConfigParserIni("props.ini")
