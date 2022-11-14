import requests 

BASE_URL = "http://127.0.0.1:5000/tasks"

def delete_task(pk, title):
    task_dictionary = {
        "title": title,

    }
    url ="%s/%s" % (BASE_URL, pk)
    response = requests.put(url, json=task_dictionary)
    if response.status_code == 204:
        print ("Delete successfull")
    else:
        print ("Somethine went wrong")

if __name__ == "__main__":
    task_id = input ("Target task id: ")
    title = input ("New title: ")
    delete_task(task_id, title) 