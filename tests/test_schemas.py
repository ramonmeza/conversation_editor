from json import load as load_json
from jsonschema import validate, ValidationError
from pathlib import Path
from pytest import fixture, raises

from tests.json_test_data import JsonTestData


# convenience constants
CONVERSATION_VALIDATION_FAILED: bool = False


# test data constants
POSITIVE_TEST_DATA = [
    JsonTestData(
        Path('data/schemas/attribute_comparison_node_schema.json'),
        {
            'operator': '<',
            'attribute': 'Health',
            "value": 100
        }
    ),
    JsonTestData(
        Path('data/schemas/talk_node_schema.json'),
        {
            'speaker': 'Tester',
            'text': 'This is just a test of the Talk Node schema.'
        }
    ),
    JsonTestData(
        Path('data/schemas/conversation_schema.json'),
        {
            'name': 'Tester',
            'description': 'This is just a test of the Conversation schema.',
            'nodes': [{
                'speaker': 'Tester',
                'text': 'This is just a test of the Talk Node schema.'
            }, {
            'operator': '<',
            'attribute': 'Health',
            "value": 100
            }],
            'connections': [
                [1],
                [2],
                [0, 1]
            ]
        }
    )
]

NEGATIVE_TEST_DATA = [
    JsonTestData(
        Path('data/schemas/attribute_comparison_node_schema.json'),
        {}
    ),
    JsonTestData(
        Path('data/schemas/attribute_comparison_node_schema.json'),
        {
            'operator': 0,
            'attribute': 'Health',
            "value": 100
        }
    ),
    JsonTestData(
        Path('data/schemas/attribute_comparison_node_schema.json'),
        {
            'operator': '<',
            'attribute': 0,
            "value": 100
        }
    ),
    JsonTestData(
        Path('data/schemas/attribute_comparison_node_schema.json'),
        {
            'operator': '<',
            'attribute': 0,
            "value": "100"
        }
    ),
    JsonTestData(
        Path('data/schemas/talk_node_schema.json'),
        {
            'speaker': 0,
            'text': 'This is just a test of the Talk Node schema.'
        }
    ),
    JsonTestData(
        Path('data/schemas/talk_node_schema.json'),
        {
            'speaker': 'Tester',
            'text': 0
        }
    )
]


# fixtures
@fixture(params=POSITIVE_TEST_DATA)
def positive_test_data(request):
    return request.param

@fixture(params=NEGATIVE_TEST_DATA)
def negative_test_data(request):
    return request.param


# tests
def test_schema_positive(positive_test_data) -> None:
    assert positive_test_data.schema.exists(), 'Schema file not found'

    # load the schema
    with open(positive_test_data.schema) as fp:
        schema: dict = load_json(fp)

    # try to validate the example against the schema
    try:
        validate(positive_test_data.data, schema)
    except ValidationError as e:
        assert CONVERSATION_VALIDATION_FAILED, f'Validation failed:\n{repr(e)}'

def test_schema_negative(negative_test_data) -> None:
    assert negative_test_data.schema.exists(), 'Schema file not found'

    # load the schema
    with open(negative_test_data.schema) as fp:
        schema: dict = load_json(fp)

    # try to validate the example against the schema
    with raises(ValidationError):
        validate(negative_test_data.data, schema)
