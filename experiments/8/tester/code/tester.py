import fire
import requests
import time


def measure_http_request(url, times=1):

    start = time.time()

    for i in range(times):
        do_reqest(url)

    end = time.time()

    avg = 1000 * (end - start) / times

    return "{:.1f}ms on avg for {} requests to {}.".format(avg, times, url)


def do_reqest(url):
    requests.get(url)


if __name__ == "__main__":
    fire.Fire(measure_http_request)
