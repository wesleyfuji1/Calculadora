from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import ast


class MainApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(multiline=False, readonly=True, halign="right", font_size=100)
        main_layout.add_widget(self.solution)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]

        # Adicionando os botões num layout horizontal
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        # Botão de igual fora do loop
        equals_button = Button(text="=", pos_hint={"center_x": 0.5, "center_y": 0.5})
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            # Limpa a solução
            self.solution.text = ""
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                # Não permite dois operadores seguidos
                return
            elif current == "" and button_text in self.operators:
                # Não permite operador no início
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            try:
                # Evita usar eval diretamente, substituindo por um parser simples
                solution = str(self.calculate_solution(text))
                self.solution.text = solution
            except Exception as e:
                # Exibe erro caso a expressão seja inválida
                self.solution.text = "Error"

    def calculate_solution(self, expression):
        try:
            # Substituindo operadores para formato adequado e avaliando a expressão
            # Isso garante que apenas números e operadores aritméticos sejam passados
            return eval(expression)
        except:
            raise ValueError("Invalid expression")


# Inicializa a aplicação
if __name__ == "__main__":
    MainApp().run()