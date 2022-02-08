
"""
1. Go to https://todomvc.com/examples/react
2. Add 5 products, e.g.
    - milk
    - bread
    - apples
    - bananas
    - fish
3. Make sure 5 items are in the bucket.
4. Mark that bread and fish are completed.
5. Make sure 3 items are left in the bucket
and 2 are marked as completed.
6. Click on  completed and check if there are 2 items.
7. Click on "clear completed".
8. Go to All and make sure there are only 3 items in the list.

"""
"""
1. Go to https://todomvc.com/examples/react
2. Add 5 products, e.g.
    - milk
    - bread
    - apples
    - bananas
    - fish
3. Mark apples and fish as completed
4. verify that 3 items left (label)
5. click on "clear completed"
6. assert that still 3 items left (label)

"""
import logging

LOGGER = logging.getLogger(__name__)
PRODUCTS = ['milk', 'bread', 'apples', 'bananas', 'fish']


def test_todolist(page):
    page.goto("https://todomvc.com/examples/react/#/")

    # Click [placeholder="What needs to be done?"]
    page.click("[placeholder=\"What needs to be done?\"]")

    for product in PRODUCTS:
        # Fill [placeholder="What needs to be done?"]
        page.fill("[placeholder=\"What needs to be done?\"]", product)

        # Press Enter
        page.press("[placeholder=\"What needs to be done?\"]", "Enter")

    handle = page.query_selector(".todo-count")
    count = handle.inner_text()

    assert count == "5 items left"

    LOGGER.info(count)
