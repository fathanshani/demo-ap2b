import requests

parameter = {'id': 5}

getPostId = requests.get("https://jsonplaceholder.typicode.com/posts", params=parameter)

if (len(getPostId.json()) > 0):
  print('Mencoba melakukan Get Request')
  print('url: ', getPostId.url)
  print('Payload: ', getPostId.text)

# payload = [{
#   'nama': 'Fathan Shani',
#   'npm': 50421488,
#   'userId': 1
#   },
#   {
#   'nama': 'Aji Murad',
#   'npm': 50420999,
#   'userId': 2
#   }]

# addPost = requests.post("https://httpbin.org/post", json=payload)

# if (addPost.status_code == 200 or addPost.status_code == 201):
#   print('Mencoba melakukan Post Request')
#   print('Status Code: ', addPost.status_code)
#   print('Payload: ', addPost.text)