import pandas as pd
import os
import pytest

# Create a sample DataFrame for testing
@pytest.fixture
def sample_data():
    return pd.DataFrame({
        "Date": ["2025-09-01", "2025-09-01", "2025-09-02"],
        "Category": ["Food", "Transport", "Food"],
        "Amount": [20, 15, 30]
    })

def test_total_amount(sample_data):
    """Check if total spending is calculated correctly"""
    total = sample_data["Amount"].sum()
    assert total == 65

def test_category_summary(sample_data):
    """Check if spending by category is aggregated properly"""
    summary = sample_data.groupby("Category")["Amount"].sum()
    assert summary["Food"] == 50
    assert summary["Transport"] == 15

def test_high_spending_day(sample_data):
    """Check if highest spending day is correct"""
    daily = sample_data.groupby("Date")["Amount"].sum()
    top_day = daily.idxmax()
    assert top_day == "2025-09-02"
