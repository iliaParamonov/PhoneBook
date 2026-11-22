import random
from Models.Contact import Contact
from Pages.add_contact_page import ContactPage


def test_add_contact(authenticated_client):
    contact_page = ContactPage(authenticated_client)
    random_suffix = random.randint(10000, 99999)

    contact = Contact(
        "ilia",
        "Paramonov",
        f"05220{random_suffix}",
        f"test{random_suffix}@gmail.com",
        "RishonLeZion",
        "QA",
    )

    contact_page.open_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.contact_card_visible(contact.phone)