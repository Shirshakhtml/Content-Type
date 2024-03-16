import requests
import magic

def content_type(url):
    try:
        response = requests.get(url, stream=True)
        content_type_header = response.headers.get('Content-Type', '').split(';')[0]
        content_from_body = magic.from_buffer(response.content, mime=True)
        print(f"Content-Type header: {content_type_header}")
        print(f"Content Type obtained from Body: {content_from_body}")
        if content_type_header == content_from_body:
            return "Matched"
        else:
            return "Not Matched"
    except Exception as e:
        return f"Error: {str(e)}"

url = input("Enter the URL : ")
result = content_type(url)
print(result)
