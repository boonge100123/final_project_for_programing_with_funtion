import pytest
import pandas as pd
from create_graph import read_from_csv, create_graph
import matplotlib.pyplot as plt

#! this is a test function that tests that the data is being read from the csv file
def test_read_from_csv(monkeypatch):
    df = read_from_csv("scraped_data.csv")  # Use actual CSV file
    
    assert not df.empty  # Ensure data is read
    assert 'website' in df.columns  # Check for normalized column name
    assert 'product name' in df.columns  # Ensure column exists
    assert isinstance(df.iloc[0]['product name'], str)  # Validate type
    assert isinstance(df.iloc[0]['price'], str)  # Ensure price is read as a string before conversion

#! this is a test function that tests that the graph is being created
def test_create_graph(monkeypatch):
    df = read_from_csv("scraped_data.csv")  # Ensure the file exists
    
    assert not df.empty  # Ensure data is read
    
    #plt.show to prevent graph display during testing
    plt.show = lambda: None  

    try:
        create_graph()
        assert True  # Test passes if no exception occurs
    except Exception as e:
        pytest.fail(f"graph is not working: {e}")

# Run the tests
if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])
