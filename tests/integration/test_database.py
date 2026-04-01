import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date
from app.db.database import Base
from app.db.models import TransactionDB

# Setting up an in-memory SQLite database for testing
@pytest.fixture(scope="module")
def test_db():
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    # Create all tables in the in-memory db
    Base.metadata.create_all(bind=engine)
    
    db = TestingSessionLocal()
    yield db
    
    # Teardown
    db.close()
    Base.metadata.drop_all(bind=engine)


def test_transaction_insert_and_retrieval(test_db):
    # Setup test transaction
    tx = TransactionDB(
        date=date.today(),
        description="Integration Test Tx",
        amount=150.0,
        direction="debit",
        category="Test Category",
        confidence="high",
        classified_by="Test Suite"
    )
    
    # Insert
    test_db.add(tx)
    test_db.commit()
    
    # Retrieve
    saved_tx = test_db.query(TransactionDB).filter(TransactionDB.description == "Integration Test Tx").first()
    
    # Verify
    assert saved_tx is not None
    assert saved_tx.amount == 150.0
    assert saved_tx.category == "Test Category"
