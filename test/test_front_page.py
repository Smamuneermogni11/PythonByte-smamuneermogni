def test_front_page(client):
    response = client.get("/posts")
    assert b"<h2>PythonByte!</h2>" in response.data