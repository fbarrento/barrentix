from subprocess import Popen, PIPE


class TestApp():

    def test_main(self):
        p = Popen(["python", "tests/fixtures/app/runner.py"], stdout=PIPE)
        stdout, _ = p.communicate()

        assert "Hello" in stdout.__str__()
