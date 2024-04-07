# Horti Price

Este é um sistema desenvolvido em Python que automatiza a coleta de cotações de frutas de um site específico e as envia de forma conveniente através de um bot no Telegram.

## Visão Geral

O objetivo deste sistema é simplificar o processo de obtenção de cotações de frutas, automatizando a coleta dessas informações e fornecendo uma maneira fácil de acessá-las por meio do Telegram. Com este sistema, os usuários podem economizar tempo e esforço ao acompanhar os preços das frutas de interesse.

## Funcionalidades

- **Coleta Automatizada:** Utiliza a biblioteca Selenium para navegar até o site desejado e extrair as cotações das frutas.
- **Armazenamento em Arquivo CSV:** As cotações coletadas são armazenadas em um arquivo CSV para referência futura.
- **Envio pelo Telegram:** Utiliza a biblioteca Telebot para enviar as cotações coletadas diretamente para os destinatários via Telegram.

## Requisitos

- Python 3.x
- Bibliotecas:
  - Selenium
  - Pandas
  - Telebot
