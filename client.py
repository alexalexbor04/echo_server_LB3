import socket
# from time import sleep

# sock = socket.socket()
# sock.setblocking(1)
# sock.connect(('10.38.165.12', 9090))

# #msg = input()
# msg = "Hi!"
# sock.send(msg.encode())

# data = sock.recv(1024)

# sock.close()

# print(data.decode())

IP = input('Введите ip адрес для подключения: ')
port = int(input('Введите порт для подключения: '))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, port))
print(f'Соединение с {IP}:{port} успешно установлено')

try:
    while True:
        message_from_server = client_socket.recv(1024).decode()
        print(f'Получено: {message_from_server}')

        message_from_client = input('Введите текст для отправки: ')

        client_socket.sendall(message_from_client.encode())
        print(f'Отправлено: {message_from_client}')

        if message_from_client == 'exit':
            break
except:
    print('Возникла непредвиденная ошибка, попробуйте снова.')
    client_socket.close()
client_socket.close()