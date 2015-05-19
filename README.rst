
Runserver and go with chromium **and reduce the window width** so that the
input in the middle redisplays properly
http://localhost:8000/admin/test_app/testmodel/add/

To see this case

.. image:: BUG.png


I know it's really minor but I'd really like to understand why the text inputs
redraw properly and why selects don't.

Isolating the issue happens in updates of
 http://jsfiddle.net/jpic/ste4ku85/5/
 (thanks @emerson from #css for his expertise)

Somehow related to
https://code.djangoproject.com/ticket/24784
(see git history ... for history)
