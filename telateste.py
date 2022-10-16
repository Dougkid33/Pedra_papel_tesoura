import PySimpleGUI as sg


class TelaPython:

    def _init_(self):

        # Layout
        layout = [
            [sg.Text('Jogo do Pedra, Papel e Tesoura')],
            [sg.Text('pedra, papel ou tesoura ?'), sg.Input()],
            [sg.Button('Enviar')]
        ]
        # Janela
        janela = sg.Window("Pedra,Papel e Tesoura").layout(layout)
        # Extrair os dados da tela
        self.button, self.values = janela.Read()

    def iniciar(self):
        print(self.values)


tela = TelaPython()

tela.iniciar()
