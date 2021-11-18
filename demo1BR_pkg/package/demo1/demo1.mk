################################################################################
#
# demo1
#
################################################################################

DEMO1_VERSION = 1.0
DEMO1_SITE = $(TOPDIR)/../demo1BR_pkg/src
DEMO1_SITE_METHOD = local

define DEMO1_BUILD_CMDS
   $(MAKE) $(TARGET_CONFIGURE_OPTS) demo1 -C $(@D)
endef
define DEMO1_INSTALL_TARGET_CMDS 
   $(INSTALL) -D -m 0755 $(@D)/demo1 $(TARGET_DIR)/usr/bin 
endef
WORMS_LICENSE = Proprietary

$(eval $(generic-package))
