import requests
from DEIParty.settings import API_URLS, ERROR, ACCESS_TOKEN

# .. Delete this
BASE_URL = "http://aduck.rnl.tecnico.ulisboa.pt/deiparty"
# The convention is {"objective": (url, method)}
API_URLS = {
    "LIST_BEVERAGES": BASE_URL + "/beverages",
    "CREATE_BEVERAGES": BASE_URL + "/beverages",
    "REMOVE_BEVERAGES": BASE_URL + "/beverages/{beverageId}",
    "INFO_BEVERAGE": BASE_URL + "/beverages/{beverageId}",
    "UPDATE_BEVERAGE": BASE_URL + "/beverages/{beverageId}"
}


def list_all_beverages(limit, offset):

    url = API_URLS["LIST_BEVERAGES"]
    params = {"limit": limit, "offset": offset}

    r = requests.get(url, params)

    if r.ok:
        return r.json()
    else:
        return ERROR


def get_beverage_info(id):

    url = API_URLS["INFO_BEVERAGE"].replace("{beverageId}", str(id))

    r = requests.get(url)

    if r.ok:
        return r.json()
    else:
        return ERROR


def process_removal(id):

    url = API_URLS["REMOVE_BEVERAGES"].replace("{beverageId}", str(id))

    r = requests.delete(
        url, headers={"Authorization": "Bearer " + ACCESS_TOKEN})

    return r.status_code


def process_update(id, new_quantity):

    url = API_URLS["UPDATE_BEVERAGE"].replace("{beverageId}", str(id))
    beverage = get_beverage_info(id)

    new_beverage = beverage
    new_beverage["amountInStock"] = new_quantity

    r = requests.put(url, params=new_beverage, headers={
                     "Authorization": "Bearer " + ACCESS_TOKEN})

    print("\n\n\nr status code = ", r.status_code)
    return r.status_code
