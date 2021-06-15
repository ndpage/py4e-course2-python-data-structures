import requests

url = 'https://httpbin.org/post'
myapp = {
  "name": "Nathan Page",
  "email": "nathanpage2018@gmail.com",
  "resume": "www.example.com/your-resume.pdf",
  "phone": "555-867-5309",
  "job_id": "9a90a063-fefa-405d-8952-e0ac5ddd0ad8",
  "github": "github.com/octocat",
  "twitter": "@example", 
  "website": "www.example.com",
  "location": "San Francisco", 
  "favorite_candy": "m&m’s", 
  "superpower": "multilingual" 
}


x = requests.post(url, data = myapp)

print(x.text)
