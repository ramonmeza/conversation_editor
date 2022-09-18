import json
import jsonschema
import pathlib

CONVERSATION_VALIDATION_FAILED: bool = False


def test_conversation_example() -> None:
    """Test if the Conversation Example is valid against the schema.
    """
    schema_path: pathlib.Path = pathlib.Path('data/conversation_schema.json')
    example_path: pathlib.Path = pathlib.Path('data/conversation_example.json')

    assert schema_path.exists(), 'Schema file not found'
    assert example_path.exists(), 'Example file not found'

    # load the schema
    with open(schema_path) as fp:
        schema = json.load(fp)

    # load the example json
    with open(example_path) as fp:
        example = json.load(fp)

    # try to validate the example against the schema
    try:
        jsonschema.validate(example, schema)
    except jsonschema.ValidationError as e:
        assert CONVERSATION_VALIDATION_FAILED, f'Validation failed:\n{repr(e)}'
