# LoRaWAN_Gateway_HAT_Software

<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/Features_banner.png" width="" height="">

Transform your Raspberry Pi into a robust LoRaWAN Gateway with our versatile HAT supporting RAK5146 concentrator module. The RAK5146 is an LPWAN Concentrator Module in a mini-PCIe form factor, featuring the Semtech SX1303 and SX126X for the Listen Before Talk (LBT) feature, enabling seamless integration into existing routers or other network equipment with LPWAN Gateway capabilities. 
With seamless communication between your Pi and LoRaWAN end node devices, this Gateway HAT supports multiple channels and global frequency bands, making it ideal for DIY IoT projects and rapid prototyping.

This Github provides getting started instructions for LoRaWAN Gateway HAT.

### Features :
- Raspberry Pi form factor with a 40-pin compatible header
- Compatible with the Raspberry Pi 3 Model B+/Raspberry 4
- Mini PCIe connector on board
- Two Programmable buttons and LEDs for additional control features addon and status or alert indications.
- SX1303 baseband processor emulates 8 x 8 channels LoRa packet detectors, 8x SF5-SF12 LoRa demodulators, 8x SF5-SF10 LoRa demodulators, one 125/250/500 kHz high-speed LoRa demodulator, and one (G)FSK demodulator
- Supports global license-free frequency band: EU868, EU433, RU864, CN470, US915, AS923, AU915, KR920, and IN865

### Hardware Overview :

<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/pinout.png" width="" height="">

## Interfacing Details : 

<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/interfacing_info.png" width="668" height="411">

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

<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/pi_login.png" width="490" height="286"> 

``` 
$ sudo apt update && sudo apt upgrade -y
```
<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/pi_lorawan_gateway1.png" width="493" height="307"> 

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
<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/pi_lorawan_gateway3.png" width="570" height="310"> 

It will take some time depending on internet speed, when the installation is complete, you will see the following on your screen. Once done you will get a success message as shown below. Also you can type command to verify version,
```
$ sudo gateway-version
```
<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/pi_lorawan_gateway5.png" width="504" height="168"> 

For demo we plan to connect Gateway with TheThingsNetwork Cloud server so we will proceed to configure settings accordingly
```
$ sudo gateway-config
```

To edit config files for Region, Service, Server address, etc.

<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/pi_lorawan_gateway6.png" width="" height=""> 

Window will appear,

<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/pi_lorawan_gateway7.png" width="480" height="298"> 

Once you change any settings, make sure to restart the packet forwarder. We need to set plan for particular server and operating frequency. 
  -	Setup RAK Gateway Channel plan => TTN Server (for TheThingsNetwork)
  -	Also, Frequency plan as per your region, e.g US_902_928 for US region
    
<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/pi_lorawan_gateway8.png" width="885" height="548"> 

Edit packet-forwarder config to change default Server Address that will correspond to your specific regions. This you can even get through TTN Cloud server under Gateway overview section.

<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/pi_lorawan_gateway9.png" width="481" height="283"> 

For Example,
- US Regions => nam1.cloud.thethings.network
- Europe Regions => eu1.cloud.thethings.network
- Australia Regions => au1.cloud.thethings.network

<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/pi_lorawan_gateway10.png" width="" height=""> 

Now save config, restart pack-forwarder and Reboot Pi once. After this proceed for Gateway Registration process on TTN Cloud server.

### Step 2 : LoRaWAN Gateway Registration to TTN Server
- Login to TheThingsNetwork Server and if not having account already then [sign up](https://www.thethingsnetwork.org/get-started) community edition for testing.
<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/ttn_gateway1.png" width="" height="">

- Once login then select console > choose cluster (as per your region) 
<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/ttn_gateway2.png" width="" height=""> 
<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/ttn_gateway3.png" width="" height="">

- Inside Gateway tab click Register Gateway, you will need Gateway EUI unique to every device which you can get with gateway-version command as shown.
<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/ttn_gateway4.png" width="" height=""> 
<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/ttn_gateway5.png" width="" height="">

- Give unique ID, name to your gateway and select correct frequency as per your region 
<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/ttn_gateway6.png" width="" height=""> 

- Now reboot your Raspberry Pi configured in previous steps, once ready it will automatically establish connection with TTN server which you can view and monitor live updates as shown below.
<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/ttn_gateway7.png" width="" height=""> 
<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/ttn_gateway8_live.png" width="" height="">

- Even you can check end node join uplink if added to network via this gateway, checkout guide [here]() how to register end node. 
<img src="https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software/blob/main/images/ttn_gateway9_endnode_uplink.png" width="" height=""> 

## Resources
  * [Schematic](https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Hardware/blob/main/Design%20Data/LORAWAN_GATEWAY_HAT%20SCH.pdf)
  * [Hardware Files](https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Hardware)
  * [RAK5146 Reference ](https://docs.rakwireless.com/product-categories/wishat/rak2287-rak5146-pi-hat/datasheet/)
  * [Getting Started with Raspberry Pi](https://www.raspberrypi.com/documentation/computers/getting-started.html)

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
