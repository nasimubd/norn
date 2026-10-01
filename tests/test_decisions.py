from norn.decisions import TypedQuestion


def test_typed_question_is_immutable():
    question = TypedQuestion("choice", "Which route?", {"direct": "a tool"})
    assert question.question_type == "choice"
