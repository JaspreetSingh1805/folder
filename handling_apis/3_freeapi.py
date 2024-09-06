import requests
def demo1():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = requests.get(url)
    data = response.json()
    if data['success'] and 'data' in data:
       userdata =  data['data']
       id = userdata['id']
       content = userdata['content']
       return id, content
    else: 
        raise Exception("data not found")
def main():
    try:
        id,content = demo1()
        print(f" id: {id}\n content: {content}")
    except Exception as e:
        print(str(e))
if __name__ == "__main__":
   main()