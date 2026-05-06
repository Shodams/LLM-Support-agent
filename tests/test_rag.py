import pytest
from app.rag_pipeline import load_rag_pipeline

def test_pipeline_loads():
    pipeline = load_rag_pipeline()
    assert pipeline is not None


def test_basic_query():
    pipeline = load_rag_pipeline()
    response = pipeline.run("What is refund policy?")
    assert isinstance(response, str)
    assert len(response) > 0
