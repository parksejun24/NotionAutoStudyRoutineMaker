from datetime import datetime
from notion.client import NotionClient
from notion.block import PageBlock, TextBlock, TodoBlock, DividerBlock

MY_TOKEN = "8ed9e99457d811fd382453dfcb19eda1b14d5e310977e561e2b6504929d2228ed5a374b4cb06873a96136d7bbb377f39c0267970804c8aeb7934298467bbec02ebe3d6d834245784f1c6704900d7"
MY_PAGE = "https://www.notion.so/parksejun24/4bded5c407c24320938bd478c8d04e82?v=8f71a29f2b77489e8e155e421c4bb72e"

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
