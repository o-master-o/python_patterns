from threading import Thread

from singletone import SimpleSingleton, ThreadSingleton


def get_singleton_obj(id_storage):
    _id = id(ThreadSingleton())
    id_storage.append(_id)


def test_new_method_singleton_instances_should_have_same_id():
    assert id(SimpleSingleton()) == id(SimpleSingleton())


def test_init_method_singleton_instances_should_have_same_id():
    id_storage = []
    thread1 = Thread(target=get_singleton_obj, args=(id_storage, ))
    thread2 = Thread(target=get_singleton_obj, args=(id_storage, ))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    assert id_storage[0] == id_storage[1]
