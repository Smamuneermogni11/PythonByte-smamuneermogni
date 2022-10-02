from front_page import app

def test_front_page():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'PythonByte!'
