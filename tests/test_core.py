from json import load as load_json
from jsonschema import validate, ValidationError
from pathlib import Path
from pytest import fixture, raises

from conversation_editor.core.attribute_comparison_node import AttributeComparisonNode
from conversation_editor.core.conversation import Conversation
from conversation_editor.core.talk_node import TalkNode
from tests.json_test_data import JsonTestData


# convenience constants
CONVERSATION_VALIDATION_FAILED: bool = False


# test data constants
POSITIVE_TEST_DATA = [
    JsonTestData(
        Path('data/schemas/attribute_comparison_node_schema.json'),
        AttributeComparisonNode().__dict__
    ),
    JsonTestData(
        Path('data/schemas/talk_node_schema.json'),
        TalkNode().__dict__
    ),
    JsonTestData(
        Path('data/schemas/conversation_schema.json'),
        Conversation().__dict__
    )
]


# fixtures
@fixture(params=POSITIVE_TEST_DATA)
def positive_test_data(request):
    return request.param


# tests
def test_core_serialization(positive_test_data) -> None:
    assert positive_test_data.schema.exists(), 'Schema file not found'

    # load the schema
    with open(positive_test_data.schema) as fp:
        schema: dict = load_json(fp)

    # try to validate the example against the schema
    try:
        validate(positive_test_data.data, schema)
    except ValidationError as e:
        assert CONVERSATION_VALIDATION_FAILED, f'Validation failed:\n{repr(e)}'
