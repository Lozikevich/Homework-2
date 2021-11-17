from devices.Device import *


if __name__ == '__main__':
    print('Вы хотите ввести данные с устройства или вручную? d/r')
    ch1 = input()
    if ch1 == 'd':
        device: Device = open_device('/devices/dev4')
        res = []
        for p in range(len(device.data)):
            a = read_line(device)
            res.insert(p, a)

        device: Device = open_device('/devices/dev3')
        i = len(device.data)

        for k in range(len(res)):
            write_line(device, res[k], i)
            i = i + 1
        print(device.data)

    elif ch1 == 'r':
        ch2 = 'y'
        device: Device = open_device('/devices/dev3')
        i = len(device.data)
        while ch2 == 'y':
            print('Введите строку для записи в устройство:')
            a = input()
            try:
                i = i + 1
                write_line(device, a, i)
                print(device.data)
                print('Хотите ввести еще строку для записи в устройство?')
                ch2 = input()
                if ch2 == 'n':
                    print('Buy!')
                    break

            except Exception as exception:
                print(f'Error: {exception}')
