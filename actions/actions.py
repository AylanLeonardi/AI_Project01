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

        # Dicionário para converter números escritos em números inteiros em string
        number_map = {
            "um": "1", "uma": "1", "dois": "2", "duas": "2", "três": "3",
            "quatro": "4", "cinco": "5", "seis": "6", "sete": "7", "oito": "8",
            "nove": "9", "dez": "10", "onze": "11", "doze": "12", "treze": "13",
            "quatorze": "14", "quinze": "15"
        }

        # Converter números escritos para dígitos
        if num is not None:
            num = [number_map.get(n.lower(), n) for n in num]

        # Caso sejam detectados mais sabores do que qtdes:
        while len(jogo_nomes) > len(num):
            num.append('1')  # adicionar '1' para quantidade padrão

        # Caso sejam detectados mais qtdes do que sabores:
        while len(jogo_nomes) < len(num):
            num.pop(0)

        for n, nome in zip(num, jogo_nomes):
            if n != "1":
                texto += f"\n - {n} unidade(s) do {nome}"
            else:
                texto += f"\n - {n} unidade do {nome}"

        texto += f'\nO endereço fornecido foi: {endereco}. Favor confirmar com sim ou não.'

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
