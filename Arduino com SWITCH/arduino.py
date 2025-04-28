import serial,time

class Arduino:
    def __init__(self,port,baudrate,timeout = None, reset_delay = 2.0):
        self.__port = port 
        self.__baudrate = baudrate
        self.__timeout = timeout
        self.__reeset_delay = reset_delay
        self.ser = None
        
    def conexao_aberta(self):
        self.ser = serial.Serial(
            port = self.__port,
            baudrate =self.__baudrate,
            timeout = self.__timeout
        )
        time.sleep(self.__reeset_delay)
        print("Conexao Aberta")
        
    def conexao_fechada(self):
        if self.ser and self.ser.is_open:
            self.ser.close()
            
    def enviar(self,dados):
        if not (self.ser and self.ser.is_open):
            raise serial.SerialException("Porta Serial não está aberta")
        self.ser.write(dados.encode("utf-8"))
        self.ser.flush()
    
    def receber(self):
        if not (self.ser and self.ser.is_open):
            raise serial.SerialException("Porta Serial não está aberta")
        dado = self.ser.readline()
        return dado.decode("utf-8").rstrip("\r\n")