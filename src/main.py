from textnode import TextNode
from textnode import (extract_markdown_images,
                      extract_markdown_links,
)





def main():
    textnode = TextNode("bla bla", "italic", "https://www.example.com")

    print(textnode)
    t = "This is text with a **bolded** **word**"
    tt = t.split("**")
    print(tt)
    print("**" in t)
    print(len(tt))

    text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
    print(extract_markdown_images(text))

    text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
    print(extract_markdown_links(text))
    # [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]


"""  props = {"href": "https://www.google.com", "target": "_blank"}
    htmlnode = HTMLNode("p", "text in paragraph", None, props)

    print(htmlnode)

    print(text_node_to_html_node(textnode)) """

    



main()
