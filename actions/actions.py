# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset

class Action_Descricao_Entrega(Action):
    def name(self) -> Text:
        return "action_descricao_entrega"
    
    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        texto = "Pedido recebido: Você deseja receber:"    
        jogo_nomes = tracker.get_slot('nome_jogo_slot')
        num = tracker.get_slot('qtd_unidades_slot')
        endereco = tracker.get_slot('endereco_slot')
        # Caso sejam detectados mais sabores do que qtdes:
        while(len(sabores)>len(num)):
            qtdes.append('uma unidade de')
        # Caso sejam detectados mais qtdes do que sabores:
        while(len(sabores)<len(num)):
            qtdes.pop(0)
        for n, nome in zip(num,jogo_nomes):
            texto = texto + "\n - "+ str(n) + " pizza(s) de " + str(nome)
        texto = texto + '\nAlém disso, o seu endereço é o: ' + str(endereco) + '. Favor confirmar com sim ou não.'
        dispatcher.utter_message(text=texto)
        return []

class Reset_Todos_Slots(Action):
    def name(self) -> Text:
        return "action_resetar_slots"
    
    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        return [AllSlotsReset()]
