from data.storage import load_data, save_data
from modules.schemas import RSVP

def submit_rsvp(rsvp: RSVP):
    data = load_data()
    data[rsvp.family] = rsvp.num_people
    save_data(data)

def get_summary():
    data = load_data()
    total = sum(data.values())
    return data, total
