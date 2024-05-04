from textnode import TextNode






def main():
    textnode = TextNode("bla bla", "italic", "https://www.example.com")

    print(textnode)
    t = "This is text with a **bolded** **word**"
    tt = t.split("**")
    print(tt)
    print("**" in t)
    print(len(tt))

"""  props = {"href": "https://www.google.com", "target": "_blank"}
    htmlnode = HTMLNode("p", "text in paragraph", None, props)

    print(htmlnode)

    print(text_node_to_html_node(textnode)) """

    



main()
