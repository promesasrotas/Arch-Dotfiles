#!/usr/bin/env sh

pkill polybar

sleep 1;

polybar workspaces &
polybar appmenu &
polybar area-1 &
polybar area-2 &
polybar area-3 &
polybar area-4 &
polybar area-5 &