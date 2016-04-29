wowza-zabbix-template
=====================

Description
-----------

This is a minimal template to get info about your wowza rest url in your Zabbix Platform.

Two items, by now:

* Global connections in the Wowza
* Global Live streams number

The template uses Zabbix macros to define the user/pass Wowza server url.

It permits a fast configuration because of you can apply the same template to all your Wowza servers without modification/installation in the agents.

Of course, it can work in the agent/client side too.

Install
-------

You should look for the external scripts directory in your Zabbix configuration file. 
In the CentOS 6.7 RPM installation is: 

``` 
 /usr/lib/zabbix/externalscripts 
```

Copy the python script there. A chmod/chown to get execution permission is necessary.

Now, in your Zabbix frontend: Configuration-Templates section, Import bottom in the right.
Choose the XML file and import.

Apply this new template to your Wowza servers. 

You don't need to modify the template if you are using the standard port to access to the Wowza URL (port 8086).

To enable the user/pass you will need to create two user macros wherever you prefer. I am using the Macros tag in the host config screen.

Two user macros should be created:

* {$WOWUSER}
* {$WOWPASS}

Environment
-----------

I am using this script in my production environment:

* Wowza 4.x
* Zabbix > 2.2.x 


Notes
-----

__About User Macros__

I think Zabbix < 2.2.x cannot use user macros in external scripts. Sorry, buddy.

__About WOWZA3__

Wowza3 is deprecated. Anyway you will find one release with the last code for that version: https://github.com/vicendominguez/wowza-zabbix-template/tree/v1.00 

Check the old releases: https://github.com/vicendominguez/wowza-zabbix-template/releases



Screenshots
-----------
![Screenshot](img/zabbix-wowza-graph.png)
