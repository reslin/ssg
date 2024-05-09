from copystatic import copy_recursive
from generate_page import generate_pages_recursive

def main():
    copy_recursive("static", "public")
    #generate_page("content/index.md", "template.html", "public")
    generate_pages_recursive("content", "template.html", "public")
    
main()
