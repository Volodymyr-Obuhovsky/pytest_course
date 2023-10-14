from mimesis import Address


def get_fake_address():
    address = {}
    fake_address = Address()
    address["continent"] = fake_address.continent()
    address["country"] = fake_address.country()
    address["state"] = fake_address.state()
    address["city"] = fake_address.state()
    address["street"] = fake_address.street_name()
    address["apartment"] = fake_address.street_number()
    address["postal_code"] = fake_address.postal_code()
    return address


if __name__ == "__main__":
    print(get_fake_address())
