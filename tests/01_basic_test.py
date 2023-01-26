from other_code.services import DATA_SET_A, DATA_SET_B, DATA_SET_C


def test_example():
    """
    But really, test cases should be callables containing assertions:
    """
    print("\nRunning test_example...")
    assert DATA_SET_A == DATA_SET_B

def test_with_local_fixture_2(local_fixture):
    """
    Fixtures can be invoked simply by having a positional arg
    with the same name as a fixture:
    """
    print("Running test_with_local_fixture...")
    assert False
