# LoRaWAN_Gateway_HAT_Software

<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/Features_banner.png" width="" height="">

This Github provides getting started instructions for LoRaWAN Gateway HAT.

### Features :


### Hardware Overview :

<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/pinout.png" width="" height="">

## Interfacing Details : 

## Getting Started with LoRaWAN Gateway HAT:
### Step 1 : Setup Raspberry Pi Headless for Easy Access and Interface configuration 
- Checkout instructional guide [here](https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/Documents/RPi_headless_setup.pdf) to perform headless setup for remote access. After this step you should be able to login and access Raspberry remotely from other PC/Laptop by SSH using PuTTy or VNC tool.
- After you log in, you need to configure the Raspberry Pi – enable SSH, SPI, I2C, etc. For this follow guide [here](https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/Documents/Interface%20Configuration%20of%20Raspberry%20Pi.pdf)
- Now, you can proceed for further steps.
  
### Step 2 : LoRaWAN Gateway setup and configuration
- Gateway HAT is equipped with RAK5146 concentrator module. Make gateway connection to raspberry pi with onboard antenna as shown in below image,

  <img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/Hardware%20connection.png" width="396" height="247"> 

> ⚠️ **WARNING :** Do not power board without Antenna connection otherwise this might damage the circuitry!

- Login to Raspberry Pi and follow below commands in sequence:

<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/pi_login.png" width="" height=""> 

``` 
$ sudo apt update && sudo apt upgrade -y
```
<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/pi_lorawan_gateway1.png" width="" height=""> 

This command will update packages and wait for sometime depending on internet connection speed it will take a few minutes to complete.

Before moving for next command check if git already available in Raspberry Pi,
```
$ git --version
```
<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/pi_lorawan_gateway2.png" width="" height=""> 

If not present then install with below command,
``` 
$ sudo apt install git
```

Now download packages for onboard rak5146 concentrator module of Gateway,
```
$ git clone https://github.com/RAKWireless/rak_common_for_gateway.git ~/rak_common_for_gateway
```
```
$ cd ~/rak_common_for_gateway
```

From inside the folder install the packages, for our gateway we need to select option 11. In case facing any issue do fresh installation with option 12,
```
$ sudo ./install.sh
```
<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/pi_lorawan_gateway3.png" width="" height=""> 

It will take some time depending on internet speed, when the installation is complete, you will see the following on your screen. Once done you will get a success message as shown below. Also you can type command to verify version,
```
$ sudo gateway-version
```
<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/pi_lorawan_gateway5.png" width="" height=""> 

For demo we plan to connect Gateway with TheThingsNetwork Cloud server so we will proceed to configure settings accordingly
```
$ sudo gateway-config
```

To edit config files for Region, Service, Server address, etc.

<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/pi_lorawan_gateway6.png" width="" height=""> 

Window will appear,

<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/pi_lorawan_gateway7.png" width="" height=""> 

Once you change any settings, make sure to restart the packet forwarder. To connect with ThingsNetworkSetup we need to set server and correct frequency 
  -	Setup RAK Gateway Channel plan => TTN Server
  -	Also, Frequency plan as per your region, e.g US_902_928 for US region
    
<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/pi_lorawan_gateway8.png" width="" height=""> 

Edit packet-forwarder config to change default Server Address that will correspond to your specific regions. This you can even get through TTN Cloud server under Gateway overview section.

<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/pi_lorawan_gateway9.png" width="" height=""> 

For Example,
- US Regions => nam1.cloud.thethings.network
- Europe Regions => eu1.cloud.thethings.network
- Australia Regions => au1.cloud.thethings.network

<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/pi_lorawan_gateway10.png" width="" height=""> 

Now save config, restart pack-forwarder and Reboot Pi once. After this proceed for Gateway Registration process on TTN Cloud server.

### Step 2 : LoRaWAN Gateway Registration to TTN Server

<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/ttn_gateway1.png" width="" height=""> 
<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/ttn_gateway2.png" width="" height=""> 
<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/ttn_gateway3.png" width="" height=""> 
<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/ttn_gateway4.png" width="" height=""> 
<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/ttn_gateway5.png" width="" height=""> 
<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/ttn_gateway6.png" width="" height=""> 
<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/ttn_gateway7.png" width="" height=""> 
<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/ttn_gateway8.png" width="" height=""> 


## Related Products  

  * [LoRaWAN Breakout Board](https://shop.sb-components.co.uk/products/lorawan-breakout)

  * [LoRaWAN for Raspberry Pi Pico](https://shop.sb-components.co.uk/products/lorawan-for-raspberry-pi-pico)
  
  * [LoRaWAN RP2040 USB Dongle](https://shop.sb-components.co.uk/products/lorawan-rp2040-usb-dongle)

  * [LoRaWAN For ESP32](https://shop.sb-components.co.uk/products/lorawan-for-esp32)

  * [LoRaWAN HAT for Raspberry Pi](https://shop.sb-components.co.uk/products/lorawan-hat-for-raspberry-pi)
     

## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>
