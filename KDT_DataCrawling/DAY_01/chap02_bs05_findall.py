from bs4 import BeautifulSoup

html_example = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BeautifulSoup 활용</title>
</head>
<body>
    <h1 id="heading">Heading 1</h1>
    <p>Paragraph</p>
    <div id="link">
        <a class="external_link" href="www.google.com">google</a>

        <div id="class1">
            <p id="first">class1's first paragraph</p>
            <a class="external_link" href="www.naver.com">naver</a>

            <p id="second">class1's second paragraph</p>
            <a class="internal_link" href="/pages/page1.html">Page1</a>
            <p id="third">class1's third paragraph</p>
        </div>
    </div>
    <div id="text_id2">
        Example page
        <p>g</p>
    </div>
    <h1 id="footer">Footer</h1>
</body>
</html>
'''

soup = BeautifulSoup(html_example, 'html.parser')

div_tags = soup.find_all('div')
print('div_tags length: ', len(div_tags))

for div in div_tags:
    print('-----------------------------------------------')
    print(div)

links = soup.find_all('a')

for alink in links:
    print(alink)
    print(f'rul:{alink["href"]}, text: {alink.string}')
    print()

link_tags = soup.find_all('a', {'class':['external_link', 'internal_link']})
print(link_tags)

p_tags = soup.find_all('p', {'id':['first','third']})
for p in p_tags:
    print(p)

