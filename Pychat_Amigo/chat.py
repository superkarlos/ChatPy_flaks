import flet as ft #ft nome do flate


def main( pagina):#funcão que recebe  S PG
#=========================funcao===========================
  chat = ft.Column()
  nome_usuariio = ft.TextField(label="Escreva seu nome")


  def enviar_msg_sevidor(mensagem):
    chat.controls.append(ft.Text(mensagem))
    pagina.update()

  pagina.pubsub.subscribe(enviar_msg_sevidor)
  #interligar 
  def enviar_msg (envet):
    pagina.pubsub.send_all(  campo_msg ) # mandando
    campo_msg.value =""
    pagina.update()
     
  campo_msg     = ft.TextField(label="Digite uma mensagem") 
  btn_env_mgs   = ft.ElevatedButton("Enviar",on_click= enviar_msg)

  def entrar_popup (ex):
    #fechar poupo
    popup.open= False

    pagina.add(chat)
    pagina.remove(butão)

    lista_items =[campo_msg,btn_env_mgs]
    pagina.add(ft.Row(lista_items))
    

    pagina.remove(texto)
    pagina.update()
    
    
    # remover o btn_inic_chat
    #cirar msg usuario


  popup = ft.AlertDialog(open=False,
                         modal=True,
                         title=ft.Text("bem vindo"),
                         content=nome_usuariio,
                         actions=[ft.ElevatedButton("entrar",on_click= entrar_popup)]
                       
                         )

  def caixa(evento):
    pagina.dialog = popup
    popup.open  = True
    pagina.update()

  def entrar_chat(evento):
    enviar = ft.Text("usuari_online")
    pagina.add(enviar)
#============================================================

  texto = ft.Text("Pychat_ Amigo")
  pagina.add(texto)

  butão = ft.TextButton("entrar no site",on_click=caixa) #on_clic quando crair
  pagina.add(butão)
  
 # butão_online= ft.TextButton("Inicar",on_click=entrar_chat) #on_clic quando crair
  #pagina.add(butão_online)

  

ft.app(target=main, view=ft.WEB_BROWSER) # quem ele vai rodar
