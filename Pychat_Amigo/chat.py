from logging import debug
import flet as ft #ft nome do flate


def main( pagina):#funcão que recebe  S PG
#=========================funcao===========================
  chat = ft.Column()
  nome_usuariio = ft.TextField(label="Escreva seu nome")


  def enviar_msg_sevidor(mensagem):
    tipo = mensagem["tipo"]
    if tipo == "mensagem":
      texto_mensgem  = mensagem["texto"]
      usuario_nome  = mensagem["usuario"]
      chat.controls.append(ft.Text(f"{usuario_nome}:{texto_mensgem}"))
    else:
       usuario_nome  = mensagem["usuario"]
       chat.controls.append(ft.Text(f"{usuario_nome} entrou no chat",size =12 ,italic=True , color=ft.colors.DEEP_ORANGE_500)) 
    pagina.update()

  pagina.pubsub.subscribe(enviar_msg_sevidor)
  #interligar 








  def enviar_msg (envet):
    pagina.pubsub.send_all(  {"texto":campo_msg.value,"usuario":nome_usuariio.value,"tipo":"mensagem"}) # mandando
    campo_msg.value =""
    pagina.update()
     
  campo_msg     = ft.TextField(label="Digite uma mensagem",on_submit=enviar_msg) 
  btn_env_mgs   = ft.ElevatedButton("Enviar",on_click= enviar_msg, )







  def entrar_popup (ex):
    #fechar poupo
    pagina.pubsub.send_all({"usuario":nome_usuariio.value, "tipo":"entrada"})
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
                         title=ft.Text("Entrar no chat"),
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
  texto2 = ft.Text("Um projeto de envios e recebimentos de mensagens",color=ft.colors.RED_500,size=30)
  texto = ft.Text("-------------------Pychat_ Amigo----------------------")
  
  pagina.add(texto)
  pagina.add(texto2)

  butão = ft.TextButton("Click aqui",on_click=caixa) #on_clic quando crair
  pagina.add(butão)
  
 # butão_online= ft.TextButton("Inicar",on_click=entrar_chat) #on_clic quando crair
  #pagina.add(butão_online)

  

ft.app(target=main, view=ft.WEB_BROWSER,port=8000) # quem ele vai rodar
