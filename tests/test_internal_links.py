import pyHtmlProofer

options = {"log_level": "ERROR", "disable_external": True}


def test_internal_links2():
    directory_path = ["output"]
    failures = pyHtmlProofer.directories(directory_path, options=options).check()

    assert len(failures) == 0
