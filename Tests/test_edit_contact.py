from faker import Faker

from Models.Contact import Contact
from Pages.add_contact_page import ContactPage
from Pages.contact_page import ContactsPage

fake = Faker()
def create_contact():
    return Contact(
        fake.first_name(),
        fake.last_name(),
        fake.numerify("05#########"),
        fake.email(),
        fake.street_address(),
        fake.sentence(nb_words=2))



def test_edit_contact_name_field(authenticated_client):
    contact_page = ContactPage(authenticated_client)
    contacts_page = ContactsPage(authenticated_client)

    contact = create_contact()

    contact_page.create_contact_steps(contact)

    new_name = fake.first_name()

    contacts_page.open_contact_details_card(contact.phone)
    contacts_page.open_edit_contact_mode()
    contacts_page.set_edit_mode(contacts_page.FIRST_NAME_INPUT, new_name)
    contacts_page.submit_edit()

    assert contacts_page.contact_name_updated() == new_name

def test_edit_contact_last_name_field(authenticated_client):
    contact_page = ContactPage(authenticated_client)
    contacts_page = ContactsPage(authenticated_client)

    contact = create_contact()

    contact_page.create_contact_steps(contact)

    new_name = fake.last_name()

    contacts_page.open_contact_details_card(contact.phone)
    contacts_page.open_edit_contact_mode()
    contacts_page.set_edit_mode(contacts_page.LAST_NAME_INPUT, new_name)
    contacts_page.submit_edit()

    assert contacts_page.contact_last_name_updated() == new_name

def test_edit_contact_phone_field(authenticated_client):
    contact_page = ContactPage(authenticated_client)
    contacts_page = ContactsPage(authenticated_client)

    contact = create_contact()

    contact_page.create_contact_steps(contact)

    new_phone = fake.numerify("05#########")

    contacts_page.open_contact_details_card(contact.phone)
    contacts_page.open_edit_contact_mode()
    contacts_page.set_edit_mode(contacts_page.PHONE_INPUT, new_phone)
    contacts_page.submit_edit()

    assert contacts_page.contact_cards_visible(new_phone)

def test_edit_contact_email_field(authenticated_client):
    contact_page = ContactPage(authenticated_client)
    contacts_page = ContactsPage(authenticated_client)

    contact = create_contact()

    contact_page.create_contact_steps(contact)

    new_email = fake.email()

    contacts_page.open_contact_details_card(contact.phone)
    contacts_page.open_edit_contact_mode()
    contacts_page.set_edit_mode(contacts_page.EMAIL_INPUT, new_email)
    contacts_page.submit_edit()

    assert contacts_page.contact_email_updated() == new_email