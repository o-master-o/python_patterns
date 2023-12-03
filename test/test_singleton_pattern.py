from singletone import SimpleSingleton


def test_new_method_singleton_instances_should_have_same_id():
    assert id(SimpleSingleton()) == id(SimpleSingleton())
