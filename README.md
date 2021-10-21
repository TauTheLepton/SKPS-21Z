# SKPS21Z_mpalczuk_tkobylecki

fdt addr $fdt_addr
fdt get value bootargs_org /chosen
setenv bootargs $bootargs_org

printenv bootargs

bootargs

BR/.config


setenv bootargs "root=/dev/mmcblk0p4 $bootargs_org root=/dev/mmcblk0p4"


sudo dd if=rootfs.ext4 of=/dev/mmcblk0p4

wget https://10.42.0.1/rootfs/.......

root=/dev/mmcblk0p4
