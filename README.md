wowza-zabbix-template
=====================

Description
-----------

This is a minimal template to get info about your wowza rest url in your Zabbix Platform.

Two items, by now:

* Global connections in the Wowza
* Global Live streams number

The template use Zabbix macros on Host to define the user/pass Wowza server url.

Install
-------

You should look for the external scripts directory in your config server. 
In the CentOS 6.4 RPM installation is: 

``` 
 /usr/lib/zabbix/externalscripts
 
```

Copy the python script there. A chmod/chown to get execution permission is necessary.

In your Zabbix frontend: Configuration-Templates section, Import bottom in the right.
Choose the xml file and import.

Apply this new template to your Wowza servers. 
You don't need to modify the template if you are using the standard port to access to the Wowza URL (port 8086).

To enable the user/pass you need to create two user macros wherever you prefer. I am using the Macro Tag in the Host config.
Two user macros must be created:

* {$WOWUSER}
* {$WOWPASS}

Environment
-----------

I am using this script in my production enviroment:

* Wowza 3.x
* Zabbix 2.2.x

Notes
-----

I think Zabbix < 2.2.x cannot use user macro in external scripts. Sorry, buddy.

