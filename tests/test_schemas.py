import collections
import json
import jsonschema
import pathlib
import pytest


# types
SchemaTestData: collections.namedtuple = collections.namedtuple('SchemaTestData', ['schema_path', 'data'])


# convenience constants
CONVERSATION_VALIDATION_FAILED: bool = False


# test data constants
POSITIVE_TEST_DATA = [
    SchemaTestData(pathlib.Path('data/schemas/attribute_comparison_node_schema.json'), {
        'operator': '<',
        'attribute': 'Health',
        "value": 100
    }),
    SchemaTestData(pathlib.Path('data/schemas/talk_node_schema.json'), {
        'speaker': 'Tester',
        'text': 'This is just a test of the Talk Node schema.'
    })
]

NEGATIVE_TEST_DATA = [
    SchemaTestData(pathlib.Path('data/schemas/attribute_comparison_node_schema.json'), {
        'operator': 0,
        'attribute': 'Health',
        "value": 100
    }),
    SchemaTestData(pathlib.Path('data/schemas/attribute_comparison_node_schema.json'), {
        'operator': '<',
        'attribute': 0,
        "value": 100
    }),
    SchemaTestData(pathlib.Path('data/schemas/attribute_comparison_node_schema.json'), {
        'operator': '<',
        'attribute': 0,
        "value": "100"
    }),
    SchemaTestData(pathlib.Path('data/schemas/talk_node_schema.json'), {
        'speaker': 0,
        'text': 'This is just a test of the Talk Node schema.'
    }),
    SchemaTestData(pathlib.Path('data/schemas/talk_node_schema.json'), {
        'speaker': 'Tester',
        'text': 0
    })
]


# fixtures
@pytest.fixture(params=POSITIVE_TEST_DATA)
def positive_test_data(request):
    return request.param

@pytest.fixture(params=NEGATIVE_TEST_DATA)
def negative_test_data(request):
    return request.param


# tests
def test_schema_positive(positive_test_data) -> None:
    assert positive_test_data.schema_path.exists(), 'Schema file not found'

    # load the schema
    with open(positive_test_data.schema_path) as fp:
        schema: dict = json.load(fp)

    # try to validate the example against the schema
    try:
        jsonschema.validate(positive_test_data.data, schema)
    except jsonschema.ValidationError as e:
        assert CONVERSATION_VALIDATION_FAILED, f'Validation failed:\n{repr(e)}'

def test_schema_negative(negative_test_data) -> None:
    assert negative_test_data.schema_path.exists(), 'Schema file not found'

    # load the schema
    with open(negative_test_data.schema_path) as fp:
        schema: dict = json.load(fp)

    # try to validate the example against the schema
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(negative_test_data.data, schema)
