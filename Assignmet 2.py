post_data = [
{
"userId": "Alex Gates",
"id": 1,
"title": "sunt aut facere repellat provident",
"body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
},
{
"userId": "Alex Gates",
"id": 2,
"title": "qui est esse ",
"body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
},
{
"userId": "Alex Gates",
"id": 3,
"title": "ea molestias quasi exercitationem ",
"body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
},
{
"userId": "Alex Gates",
"id": 4,
"title": "eum et est occaecati ",
"body": "ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit"
},
{
"userId": "Alex Gates",
"id": 5,
"title": " nesciunt quas odio",
"body": "repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque"
}]

# Sample output
# {
# 'userId': 'Alex Gates',
# 'id': 5,
# 'title': ' nesciunt quas odio',
# 'body': 'repudiandae veniam quaerat sunt sed.....',
# 'slug': '-nesciunt-quas-odio'
# }


i=0
while i<len(post_data):
    title = post_data[i]['title']
    title = title.strip()
    title = title.rjust(len(title) + 1, ' ')
    post_data[i]['title']=title
    slug = title
    url = slug.replace(" ",'-').lower()
    post_data[i]['slug']=url
    print(post_data[i])
    i+=1
