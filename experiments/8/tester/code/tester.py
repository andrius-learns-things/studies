import fire


def measure_http_request(url):

    return "Hello %s!" % url


if __name__ == "__main__":
    fire.Fire(measure_http_request)
