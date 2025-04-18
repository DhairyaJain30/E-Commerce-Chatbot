# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionSetResetStageStarted(Action):
    def name(self):
        return "action_set_reset_stage_started"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("reset_stage", "started")]

class ActionSetResetStageEmailIssue(Action):
    def name(self):
        return "action_set_reset_stage_email_issue"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("reset_stage", "email_issue")]

class ActionClearResetStage(Action):
    def name(self):
        return "action_clear_reset_stage"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("reset_stage", None)]

class ActionSetTrackStage(Action):
    def name(self):
        return "action_set_track_stage"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("track_stage", "tracking_started")]

class ActionSetTrackStageIssue(Action):
    def name(self):
        return "action_set_track_stage_issue"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("track_stage", "tracking_issue")]

class ActionClearTrackStage(Action):
    def name(self):
        return "action_clear_track_stage"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("track_stage", None)]


class ActionSetShippingStage(Action):
    def name(self):
        return "action_set_shipping_stage"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("shipping_stage", "address_change_requested")]

class ActionSetShippingStageIssue(Action):
    def name(self):
        return "action_set_shipping_stage_issue"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("shipping_stage", "change_issue")]

class ActionClearShippingStage(Action):
    def name(self):
        return "action_clear_shipping_stage"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("shipping_stage", None)]

class ActionSetAccountStageStarted(Action):
    def name(self) -> str:
        return "action_set_account_stage_started"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: dict,
    ) -> list:
        # User has started the account‑creation flow
        return [SlotSet("creating_account", "started")]

class ActionSetAccountStageIssue(Action):
    def name(self) -> str:
        return "action_set_account_stage_issue"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: dict,
    ) -> list:
        # User is having trouble with signing up
        return [SlotSet("creating_account", "issue")]

class ActionClearAccountStage(Action):
    def name(self) -> str:
        return "action_clear_account_stage"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: dict,
    ) -> list:
        # Reset the slot once the flow is complete
        return [SlotSet("creating_account", None)]