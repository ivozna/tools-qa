"""
1. Go to page.
2. Click download.
3. Assert the file is downloaded.

4. Click choose file.
5. Give file path.
6. Assert the file is uploaded.
"""


def test_download(updown_page):
    filename = updown_page.download()
    assert filename == 'sampleFile.jpeg'


def test_upload(updown_page):
    updown_page.upload("C:\\Users\\iravo\\Desktop\\logocat.jpg")
    assert updown_page.get_path() == 'C:\\fakepath\\logocat.jpg'
