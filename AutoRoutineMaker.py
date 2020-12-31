from datetime import datetime
from notion.client import NotionClient
from notion.block import PageBlock, TextBlock, TodoBlock, DividerBlock

MY_TOKEN = "<your page v2 token>"
MY_PAGE = "<your notion page url>"

today = datetime.now().strftime('%m/%d')
client = NotionClient(token_v2=MY_TOKEN)
page = client.get_collection_view(MY_PAGE)

row = page.collection.add_row()
row.name = today

for child in row.collection.get_rows():
    child_page = client.get_block(child.id)
    if child_page.name == today:
        child_page.children.add_new(TextBlock, title="**국어**")
        child_page.children.add_new(DividerBlock)
        child_page.children.add_new(TodoBlock)
        child_page.children.add_new(TextBlock, title="**수학**")
        child_page.children.add_new(DividerBlock)
        child_page.children.add_new(TodoBlock)
        child_page.children.add_new(TextBlock, title="**영어**")
        child_page.children.add_new(DividerBlock)
        child_page.children.add_new(TodoBlock)
