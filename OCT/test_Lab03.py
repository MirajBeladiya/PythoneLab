#API Request -HTTP Request

import allure
import pytest
import requests

@allure.title("TC#1 - create Booking CRUD Positive")
@allure.description("TC#1- Verify the create booking")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    # to make request
    #URL
    #method = post
    #Headers = Contant-type=application/json
    #Paylod/data/body -dict /json
    #Auth(no)
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URl = base_url+base_path
    headers = {"Contant-Type": "appliction/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URl, headers=headers, json=payload)
    assert response.status_code == 200


@allure.title("TC#2 - create Booking CRUD Positive")
@allure.description("TC#2- Verifythe Booking is not create with data")
@pytest.mark.crud
def test_create_booking_positive_tc2():

    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URl = base_url+base_path
    headers = {"Contant-Type": "appliction/json"}
    payload = {}
    response = requests.post(url=URl, headers=headers, json=payload)
    assert response.status_code == 500