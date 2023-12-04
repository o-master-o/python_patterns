from threading import Thread

from singletone import SimpleSingleton, ThreadSingleton


class SingletonA(SimpleSingleton):
    pass


class SingletonB(SimpleSingleton):
    pass


def get_singleton_obj(id_storage):
    _id = id(SingletonA())
    id_storage.append(_id)


def test_for_simple_singleton_same_sub_classes_instances_should_be_the_same_instances_and_different_sub_classes_instances_should_be_the_different():
    singleton_a1 = SingletonA()
    singleton_a2 = SingletonA()
    singleton_b1 = SingletonB()
    singleton_b2 = SingletonB()

    assert singleton_a1 is singleton_a2
    assert singleton_b1 is singleton_b2
    assert singleton_a1 is not singleton_b1


def test_for_thread_singleton_same_sub_classes_instances_should_be_the_same_instances_and_different_sub_classes_instances_should_be_the_different():
    id_storage = []
    thread1 = Thread(target=get_singleton_obj, args=(id_storage, ))
    thread2 = Thread(target=get_singleton_obj, args=(id_storage, ))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    assert id_storage[0] == id_storage[1]
