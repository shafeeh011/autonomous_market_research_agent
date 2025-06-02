import pytest
from src.memory.vector_store import VectorStore
from src.memory.persistence import Persistence

def test_vector_store_initialization():
    vector_store = VectorStore()
    assert vector_store is not None

def test_vector_store_add_and_retrieve():
    vector_store = VectorStore()
    test_vector = [0.1, 0.2, 0.3]
    vector_store.add_vector(test_vector)
    retrieved_vector = vector_store.retrieve_vector(0)
    assert retrieved_vector == test_vector

def test_persistence_initialization():
    persistence = Persistence()
    assert persistence is not None

def test_persistence_save_and_load():
    persistence = Persistence()
    test_data = {"key": "value"}
    persistence.save("test_key", test_data)
    loaded_data = persistence.load("test_key")
    assert loaded_data == test_data