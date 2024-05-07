import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "unordered_list"
block_type_olist = "ordered_list"


#re_code_start = r"^`{3}"
#re_code_end = r"`{3}$"
re_heading = r"^#{1,6}\s+\w+"
#re_ulist = r"^[*-]{1}\s+"
re_olist = r"[0-9]\.+\s+"

def markdown_to_blocks(markdown):
    blocks = []
    splitters = markdown.split("\n\n")
    for splitter in splitters:
        s = splitter.strip()
        if s != "":
            blocks.append(s)
    return blocks

def block_to_block_type(markdown):
    if re.match(re_heading, markdown):
        return block_type_heading
    if markdown.startswith("```") and markdown.endswith("```"):
        return block_type_code
    if markdown.startswith(">"):
        is_quote = True
        splitters = markdown.split("\n")
        for splitter in splitters:
            if not splitter.startswith(">"):
                is_quote = False
                break
        if is_quote:
            return block_type_quote
    if markdown.startswith("* "):
        is_ulist = True
        splitters = markdown.split("\n")
        for splitter in splitters:
            if not splitter.startswith("* "):
                is_ulist = False
                break
        if is_ulist:
            return block_type_ulist  
    if markdown.startswith("- "):
        is_ulist = True
        splitters = markdown.split("\n")
        for splitter in splitters:
            if not splitter.startswith("- "):
                is_ulist = False
                break
        if is_ulist:
            return block_type_ulist
    if re.match(re_olist, markdown):
        is_olist = True
        splitters = markdown.split(".", 1)
        if splitters[0] != "1":
            is_olist = False
        if is_olist:
            num = 1
            lines = markdown.split("\n")
            for line in lines:
                numbers = line.split(".", 1)
                if not numbers[0].isdigit() or int(numbers[0]) != num:
                    is_olist = False
                    break
                num = int(numbers[0]) + 1
        if is_olist:
            return block_type_olist
    return block_type_paragraph