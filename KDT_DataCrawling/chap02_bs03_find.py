html_example='''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BeautifulSoup 활용</title>
</head>
<body>
    <h1 id="heading">Heading 1</h1>
    <p>Paragraph</p>
    <span class="red">BeautifulSoup Library Examples!</span>
    <div id="link">
        <a class="external_link" href="www.google.com">google</a>

        <div id="class1">
            <p id="first">class1's first paragraph</p>
            <a class="exteranl_link" href="www.naver.com">naver</a>

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
</html>'''

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_example, 'html.parser')
print(soup.find('div'))

print(soup.find('div', {'id':'text_id2'}))

div_text = soup.find('div', {'id':'text_id2'})
print(div_text.text)
print(div_text.string)

href_link = soup.find('a', {'class':'internal_link'})
# href_link = soup.find('a', 'class'='internal_link')

print(href_link)
print(href_link['href'])
print(href_link.get('href'))
print(href_link.text)

print('href_link.attrs: ', href_link.attrs)
print('class 속성값: ', href_link['class'])

print('values():', href_link.attrs.values())

values = list(href_link.attrs.values())
print('values[0]: {0}, values[1]: {1}'.format(values[0], values[1]))

href_value = soup.find(attrs={'href':'www.google.com'})

print('href_value: ', href_value)
print(href_value['href'])
print(href_value.string)

span_tag = soup.find('span')

print('span tag: ', span_tag)
print('attrs: ', span_tag.attrs)
print('value: ', span_tag.attrs['class'])
print('text: ', span_tag.string)

