
from faker import Faker

from Models.Contact import Contact
from Pages.add_contact_page import ContactPage
from Pages.contact_page import ContactsPage


fake = Faker()


def create_contact():
    return Contact(
        fake.first_name(),
        fake.last_name(),
        fake.numerify("05########"),
        fake.email(),
        fake.street_address(),
        fake.sentence(nb_words=2)
    )


def test_remove_contact(authenticated_client):
    contact_page = ContactPage(authenticated_client)
    contacts_page = ContactsPage(authenticated_client)

    contact = create_contact()
    contact_page.create_contact_steps(contact)

    contacts_page.open_contact_list()
    count_before = contacts_page.get_contact_cards_number()

    contacts_page.open_first_contact()
    contacts_page.remove_current_contact()

    count_after = contacts_page.get_contact_cards_number()

    assert count_after == count_before - 1

