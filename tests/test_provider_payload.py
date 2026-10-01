from norn.decisions import TypedQuestion


def test_question_can_describe_a_choice():
    question = TypedQuestion("choice", "Which executor?", {"direct": "local tool", "approval": "human review"})
    assert list(question.criteria) == ["direct", "approval"]
