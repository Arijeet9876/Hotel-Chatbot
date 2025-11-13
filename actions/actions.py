from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionConfirmBooking(Action):
    def name(self) -> Text:
        return "action_confirm_booking"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        name = tracker.get_slot("name")
        check_in_date = tracker.get_slot("check_in_date")
        check_out_date = tracker.get_slot("check_out_date")
        num_guests = tracker.get_slot("num_guests")
        breakfast_option = tracker.get_slot("breakfast_option")
        payment_method = tracker.get_slot("payment_method")
        
        confirmation_message = f"Thank you {name}! I've noted your booking:\n"
        confirmation_message += f"• Dates: {check_in_date} to {check_out_date}\n"
        confirmation_message += f"• Guests: {num_guests}\n"
        confirmation_message += f"• Breakfast: {breakfast_option}\n"
        confirmation_message += f"• Payment: {payment_method}\n\n"
        confirmation_message += "Is this information correct?(Correct/Wrong)"
        
        dispatcher.utter_message(text=confirmation_message)
        
        return []
    
