from project import video, foto, contact, about, app


def test_video():
    response = app.test_client().get('/video')
    print(response)
    assert response.status_code == 200
    assert response.content_type == "text/html; charset=utf-8"

def test_foto():
    response = app.test_client().get('/foto')
    assert response.status_code == 200
    assert response.content_type == "text/html; charset=utf-8"

def test_about():
    response = app.test_client().get('/about')
    assert response.status_code == 200
    assert response.content_type == "text/html; charset=utf-8"

def test_contact():
    response = app.test_client().get('/contact')
    assert response.status_code == 200
    assert response.content_type == "text/html; charset=utf-8"
     
