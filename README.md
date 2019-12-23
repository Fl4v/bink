## Bink Project

Bink Test Project.

### Installation

- Make sure that **python 3.7** is installed in your local environment.

Install the requirements:

- `pip3 install -r requirements.txt`

### Run

To run the script after the requirements have been installed:
```
$ python3 main.py
```

Please follow the instruction on your terminal.

### Tests

#### Given/When/Then formula:

This project template proposes the `given-when-then` testing formula:

```python
def test_example():
    # Given:
    tested = SomeClass()
    number = 5

    # When:
    result = tested.do_thing(number)

    # Then:
    assert result == 25
```

* `Given` section should include all variable declarations and initiation steps necessary to perform the test.
* `When` section should consist of a one-liner (ideally) that executes the tested functionality.
* `Then` section should contain all asserts that check the output of the tested function. As a rule of thumb, it should
contain a single `assert` to separate tests responsibilities, but multiple assertions are acceptable.

Tests can be run from the command line with `$ pytest`
