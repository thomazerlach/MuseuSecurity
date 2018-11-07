# MuseuSecurity

### Trabalho T3 Microcontroladores  

Integrantes do Grupo:
* [Thomaz Erlach](https://github.com/thomazerlach). Email: thomazerlach@hotmail.com
* [Pedro Cattel](https://github.com/pedrocattel). Email: pedrocattel@hotmail.com
* [Victor Xavier](https://github.com/viictor1224). Email: victorxm1@gmail.com

### Simulação de um sistema de segurança de um museu. 

- Com o intuito de proteger as peças valiosas de um Museu, o grupo desenvolveu um projeto utilizando a placa Raspberry Pi 3. 

- O projeto consiste em um sistema de segurança que terá como atuador um LED RGB. Sensores de Temperatura e Fumaça/Gases estarão presentes no local de acervo e detectarão qualquer mudança que possa representar perigo às obras. Assim que for detectado algum estado de perigo, um requisição ao serviço Ubidots será feita e assim os supervisores do museu serão notificados do ocorrido.

### Equipamentos/Materiais Utilizados

* Raspberry Pi 3 model B
* Cartão de memória SD
* Protoboard com GPIO Extension Board
* Fios
* LED RGB
* Sensor de THT11
* Sensor de Fumaça MX-2
* 2x Resistor 103ohms
* 1x Resistor 102ohms
* Conversor 3v3 -> 5v

### Serviços Web Utilizados

* Ubidots

### Scripts Utilizados

* T4.py

### Referências e Links utilizados

* LED RGB
  - https://www.instructables.com/id/Raspberry-Pi-3-RGB-LED-With-Using-PWM/

* Temperatura
  - https://www.filipeflop.com/blog/temperatura-umidade-dht11-com-raspberry-pi/
  - https://github.com/adafruit/Adafruit_Python_DHT

* Gas
  - http://www.knight-of-pi.org/digital-sensors-and-the-raspberry-pi-with-the-smoke-detector-mq-x-as-example/
  - https://tutorials-raspberrypi.com/configure-and-read-out-the-raspberry-pi-gas-sensor-mq-x/
  - https://tutorials-raspberrypi.com/configure-and-read-out-the-raspberry-pi-gas-sensor-mq-x/


