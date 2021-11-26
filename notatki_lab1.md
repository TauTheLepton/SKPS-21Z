fdt addr $fdt_addr
fdt get value bootargs_org /chosen
setenv bootargs $bootargs_org


printenv bootargs

bootargs

BR/.config





sudo dd if=rootfs.ext4 of=/dev/mmcblk0p4

wget https://10.42.0.1/rootfs/.......

root=/dev/mmcblk0p4