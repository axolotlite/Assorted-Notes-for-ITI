Steps:

1. Open the Terminal:
Launch a terminal session on your Linux system. You can access the terminal by using one of the default TTYs (Ctrl+Alt+F1 to Ctrl+Alt+F6) or by opening a terminal emulator.

2. Edit the Logind Configuration File:
Open the `/etc/systemd/logind.conf` file with administrative privileges using a text editor. You can do this by running the following command:
`nano /etc/systemd/logind.conf`

3. Modify the Configuration:
Within the `logind.conf` file, locate the line that begins with `#NAutoVTs=`. Remove the `#` at the beginning to uncomment the line. Then, change the value to the desired number of TTYs you want to add. For example, if you want to add ten additional TTYs, modify the line to:
`NAutoVTs=16`
then save and exit

4. Apply the Changes:
To apply the changes, restart the `systemd-logind` service. Execute the following command in the terminal:

`systemctl restart systemd-logind`

5. Accessing the New TTYs:
To access the newly added TTYs, use the Ctrl+Alt+F7 to Ctrl+Alt+F<n> key combinations, where <n> represents the number of the TTY you want to access. For instance, if you added ten additional TTYs, you can switch to TTYs 7 to 12 using the respective key combinations.
or using chvt

chvt 13

