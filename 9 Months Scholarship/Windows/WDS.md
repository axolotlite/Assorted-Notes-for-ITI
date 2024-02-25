
first, we'll need to configure some basic things.
- DHCP
- DNS
then we install WDS (Windows Deployment Service) from the roles.
after finishing its basic configurations, we have to capture a .wim file.
to do this, we must first have windows 10 installed on a device.
so, we select PC1 and select any windows ISO, then boot from it.
once it starts `shift+f10` to open a console.
the drives should've shifted or moved, we can find them through the command
`fsutil fsinfo drives`
this'll return all available drives, we should easily find the "C:" drive by entering each drive and inspecting its contents.

once the C drive is found, we have to creat a .wim file from it.
we can either capture the image directly, or optimize it.
optimization:
`dism /image:c:\ /optimise-image /boot`
note: 'c:' may be different. so check before writing it.
next, we capture the .wim file.
`dism /capture-image /imagefile:"D:\image_name.wim" /capture:C:\ /name:whatever`
alternatively from an ISO you can extract it through
`dism /export-image /sourceImageFile:install.esd /sourceIndex:1 /DesignationImageFile:C:\install.wim /checkintegrity`
another warning, `C:` is not garunteed. so, get it from the install.esd instead.
next we move it to the windows server.
next, we require a boot.wim. which can easily be acquired from mounting a windows ISO into the cd room. 
it's in the `sources` directory.