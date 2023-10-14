import responses
from web_client.web_service import BookCover


@responses.activate
def test_get_response():
    file_path = "book_cover.jpg"
    with open(file_path, "rb") as image:
        valid_answer = image.read()
        expected_result = valid_answer

    responses.add(method=responses.GET,
                  url="https://freedlit.space/storage/bookcovers/cddvanKCLOThJFq7wGuLseCyACCuCS0epHZ5BvR1.jpg",
                  body=valid_answer,
                  status=200)

    book_cover = BookCover(url="https://freedlit.space",
                           file="cddvanKCLOThJFq7wGuLseCyACCuCS0epHZ5BvR1.jpg")
    web_client_get_response = book_cover.get_response().content
    assert web_client_get_response == expected_result
