#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------
# (C) Crown copyright Met Office. All rights reserved.
#-----------------------------------------------------------------------------
"""Module containing test upgrade macros"""

import rose.upgrade


class UpgradeNull01(rose.upgrade.MacroUpgrade):

    """Upgrade nothing..."""

    BEFORE_TAG = "0.1"
    AFTER_TAG = "0.2"

    def upgrade(self, config, meta_config=None):
        self.add_report(None, None, None, "nothing...", is_warning=True)
        self.add_report("made", "up", None, "made up option", is_warning=True)
        return config, self.reports
