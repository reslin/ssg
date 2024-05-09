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


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
        print(f"made dir {dest_dir_path}")
    dir_path_contents = list(map(lambda f: os.path.join(dir_path_content, f),
                                  os.listdir(dir_path_content)))
    for content in dir_path_contents:
        if os.path.isdir(content):
            dst_path = os.path.join(dest_dir_path, os.path.split(content)[1])
            generate_pages_recursive(content, template_path, dst_path)
        else:
            generate_page(content, template_path, dest_dir_path)
            print(f"generated from {content}...")
            #shutil.copy(p, dst)
            #print(f"copied {p} -> {dst}")