from copystatic import copy_recursive
from generate_page import generate_page

def main():
    copy_recursive("static", "public")
    generate_page("content/index.md", "template.html", "public")
    
main()
