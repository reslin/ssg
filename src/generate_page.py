import os

from handle_blocks import markdown_to_html_node

def extract_title(markdown):
    blocks = markdown.split("\n\n", 1)
    if not blocks[0].startswith("# "):
        raise Exception("Missing h1-level header")
    return blocks[0].lstrip("# ")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as g:
        template = g.read()

    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    new_content = template.replace("{{ Title }}", title)
    new_content = template.replace("{{ Content }}", content)

    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
        print(f"made dir {dest_path}")

    dest_file = os.path.join(dest_path, "index.html")
    with open(dest_file, "w") as f:
        f.write(new_content)