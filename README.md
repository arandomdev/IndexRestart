# IndexRestart
For some reason whenever I turn on SteamVR, I need to restart my headset.
Well, instead of going through the motion of starting SteamVR and pressing the
reset button. I decided to create a completely over engineered solution that
power cycles the headset and then starts SteamVR. So instead of 2 clicks, just
one...

I uploaded this mostly for archival purposes, but if you want to implement this
yourself for some reason, here is some more info.

* Hardware is a 1 channel 5v relay from Hiletgo and an Arduino micro controller
called the Beetle. I removed the power LED from the relay and designed a small
case for the system, the CAD models for which are in the Model directory.
I then attached the relay's normally-open inline to the live wire of an extension
cable.
    * http://www.hiletgo.com/ProductDetail/1958599.html
    * https://www.dfrobot.com/product-1075.html
* The firmware implements a simple serial server. When it receives the trigger
command, it power cycles the headset. The python script sends the trigger command
and then launches SteamVR.