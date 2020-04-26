import fire
import requests


def measure_http_request(url):

    r = requests.get(url)

    return "HTTP {} : {}".format(r.status_code, r.text)


if __name__ == "__main__":
    fire.Fire(measure_http_request)
