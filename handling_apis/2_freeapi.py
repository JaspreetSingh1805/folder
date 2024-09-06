import requests
def demo():
    url = "https://api.freeapi.app/api/v1/public/randomproducts/product/random"
    response = requests.get(url)
    data = response.json()
    if data['success'] and "data" in data:
        user_data = data["data"]
        title = user_data['title']
        description = user_data['description']
        return title,description
    else: 
        raise Exception("Failed to fetch user data")
def main():
     try:
         title,description = demo()
         print(f"Title: {title}\n Description: {description} ")
         
     except Exception as e:
       print(str(e))
if __name__ == "__main__":
    main()