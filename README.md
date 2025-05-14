# 🛠️ Basic Raspberry 🛠️
Run SSH -> depending on the IP address

# 🔍 GPIO 🔍
![Wiring](https://github.com/NugrohoESBB/ws_raspi/blob/main/GPIO%20R3B%2B.png)

# 
# 📖 Command Line 📖

## Melihat IP address yang digunakan raspi
```c++
ifconfig
```

## Melihat isi file dan direktori
```c++
ls
```

## Melihat isi file dan direktori yg hidden
```c++
ls -a
```

## Melihat isi file dan direktori beserta permission accessnya
```c++
ls -l
```

## Pindah ke direktori lain
```c++
cd
```

## Melihat posisi direktori yang sedang dibuka
```c++
pwd
```

## Melihat isi dari direktori
```c++
ls
```

## Membuat folder baru
```c++
sudo mkdir (folder name)
```

## Membuat file/edit isi file
```c++
sudo nano (file name)
```

## Copy file
```c++
sudo cp (file name) (new file name)
```

## Melihat isi file
```c++
sudo cat (file name)
```

## Memindahkan/rename file
```c++
sudo mv (current file directory) (destination file directory)

sudo mv (file name) (new file name)
```

## Menghapus direktori/file
```c++
sudo rm -R (file name)
```

## Config raspi
```c++
sudo raspi-config
```

## Reboot raspi
```c++
sudo reboot
```

## Shutdown raspi
```c++
sudo shutdown -h now
```

# 
# 📄📒 Documentation 📒📄

## Light Sensor Pin Use to Raspi

| PIN LDR | Type     | Pin Raspi| 
| :-------- | :------- |  :------- |
| `A0` | `Communication Serial` |`4` |
| `D0` | `Communication Serial` |`4`|
| `GND` | `Ground` |`GND`|
| `5V` | `VCC` | `5V`|

## Servo Pin Use to Raspi

| PIN LCD | Type     | Pin Mega| 
| :-------- | :------- |  :------- |
| `Data` | `Communication Serial` |`25`|
| `GND` | `Ground` |`GND`|
| `5V` | `VCC` | `5V`|

## Motor Driver Pin Use to Raspi

| PIN LCD | Type     | Pin Mega| 
| :-------- | :------- |  :------- |
| `ENA` | `Communication Serial` |`25`|
| `IN1` | `Communication Serial` |`8`|
| `IN2` | `Communication Serial` |`7`|
| `GND` | `Ground` |`GND`|

# ⚠️ Optional ⚠️
## Install pip in linux
```c++
sudo apt install python3-pip
```
