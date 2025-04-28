import db,serial,time
from arduino import Arduino
   
def principal():
    
    arduino = Arduino("COM5",9600)
    arduino.conexao_aberta()
    print("Iniciando a leitura da distância")
    try:
        while True:
            arduino.enviar("REQ\n")
            resposta = arduino.receber()
            print(f"Distancia : {resposta}")
            db.inserir_atualizar("ultrasom",resposta)
            #time.sleep(0)
        
    except KeyboardInterrupt:
        print("Código interrompido")
        
    except Exception as e:
        print(f"Erro: {e} ")
    
    finally:
        arduino.conexao_fechada()
        print("Conexão fechada")

if __name__ == "__main__":
    principal()