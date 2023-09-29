import flet as ft #ft nome do flate


def main( pagina):#funcão que recebe  S PG
#=========================funcao===========================
  popup = ft.AlertDialog()
  def entrar_chat(evento):
    enviar = ft.Text("usuari_online")
    pagina.add(enviar)

  def caixa(evento):
    pagina.dialog = popup
    popup.open  = True
    pagina.update()
#============================================================

  texto = ft.Text("Pychat_ Amigo")
  pagina.add(texto)

  butão = ft.TextButton("Inicar",on_click=entrar_chat) #on_clic quando crair
  pagina.add(butão)
 

ft.app(target=main, view=ft.WEB_BROWSER) # quem ele vai rodar
