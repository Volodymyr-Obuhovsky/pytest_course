import requests


class BookCover:

    def __init__(self, url, file):
        self.url = url
        self.image_file = file

    def get_uri(self):
        uri = f"{self.url}/storage/bookcovers/{self.image_file}"
        return uri

    def get_response(self):
        resource = self.get_uri()
        response = requests.get(resource)
        return response

    def get_image(self):
        response = self.get_response().content
        with open("book_cover.jpg", "wb") as image:
            image.write(response)


if __name__ == "__main__":
    book_cover = BookCover(url="https://freedlit.space",
                           file="cddvanKCLOThJFq7wGuLseCyACCuCS0epHZ5BvR1.jpg")

    book_cover.get_image()
