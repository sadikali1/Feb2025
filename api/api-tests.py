import requests

def test_get():
    response = requests.get("https://reqres.in/api/users?page=2",
                 params={'page':2},
                 headers= {"Accept":"applicaton/json"}
                 )
    print(response.json())
    assert response.status_code == 200

def test_post():
    body = {
            "name": "morpheus",
            "job": "leader"
        }

    response = requests.post("https://reqres.in/api/users",
                            data=body,
                            headers={"Accept": "applicaton/json"}
                            )
    assert response.status_code == 201
    data =  response.json()
    assert  data['name'] == 'morpheus'
    assert data['job'] == 'leader'

def test_put():
    body = {
            "name": "morpheus",
            "job": "zion resident"
        }

    response = requests.put("https://reqres.in/api/users/2",
                            data=body,
                            headers={"Accept": "applicaton/json"}
                            )
    assert response.status_code == 200
    data =  response.json()
    assert  data['name'] == 'morpheus'
    assert data['job'] == "zion resident"

def test_patch():
    body = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = requests.patch("https://reqres.in/api/users/2",
                            data=body,
                            headers={"Accept": "applicaton/json"}
                            )
    assert response.status_code == 200

def test_delete():
    response = requests.delete("https://reqres.in/api/users/2",
                            headers={"Accept": "applicaton/json"}
                            )
    assert response.status_code == 204

def test_auth():
    auth_data= (
        "postman", 'password'
    )
    response = requests.get("https://postman-echo.com/basic-auth", auth=auth_data)
    print(response.text)
