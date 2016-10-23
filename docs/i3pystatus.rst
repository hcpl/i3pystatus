Module reference
================

.. Don't list *every* module here, e.g. cpu-usage suffices, because the other
    variants are listed below that one.

.. rubric:: Module overview:

:System: `clock`_ - `cpu_freq`_ - `cpu_usage`_ - `disk`_ - `gpu_mem`_ - `gpu_temp`_ - `keyboard_locks`_ -
         `load`_ - `mem`_ - `swap`_ - `uname`_ - `uptime`_ - `weekcal`_ - `xkblayout`_
:Audio: `alsa`_ - `pulseaudio`_
:Hardware: `backlight`_ - `battery`_ - `dpms`_ - `redshift`_ - `solaar`_ - `temp`_
:Network: `net_speed`_ - `network`_ - `online`_ - `openstack_vms`_ - `openvpn`_ - `ping`_ - `zabbix`_
:Music: `cmus`_ - `lastfm`_ - `moc`_ - `mpd`_ - `now_playing`_ - `pianobar`_ - `playerctl`_ - `spotify`_
:Streaming: `abc_radio`_ - `plexstatus`_
:Websites: `bitcoin`_ - `dota2wins`_ - `github`_ - `google_calendar`_ - `modsde`_ - `parcel`_ -
           `reddit`_ - `vk`_ - `weather`_ - `whosonlocation`_
:Other: `anybar`_ - `iinet`_ - `mail`_ - `moon`_ - `pomodoro`_ - `pyload`_ - `scores`_ - `sge`_ -
        `syncthing`_ - `taskwarrior`_ - `text`_ - `timer`_ - `timewarrior`_ - `updates`_
:Advanced: `file`_ - `makewatch`_ - `openfiles`_ - `regex`_ - `runwatch`_ - `scratchpad`_ - `shell`_ -
           `window_title`_

.. autogen:: i3pystatus Module

   .. rubric:: Module list:

.. _mailbackends:

Mail Backends
-------------

The generic mail module can be configured to use multiple mail backends. Here is an
example configuration for the MaildirMail backend:

.. code:: python

    from i3pystatus.mail import maildir
    status.register("mail",
                    backends=[maildir.MaildirMail(
                            directory="/home/name/Mail/inbox")
                    ],
                    format="P {unread}",
                    log_level=20,
                    hide_if_null=False, )

.. autogen:: i3pystatus.mail SettingsBase

   .. nothin'

.. _scorebackends:

Score Backends
--------------

.. autogen:: i3pystatus.scores SettingsBase

    .. nothin'

.. _updatebackends:

Update Backends
---------------

.. autogen:: i3pystatus.updates SettingsBase

    .. nothin'

.. _weatherbackends:

Weather Backends
----------------

.. autogen:: i3pystatus.weather SettingsBase

    .. nothin'
