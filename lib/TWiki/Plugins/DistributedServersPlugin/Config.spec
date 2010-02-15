# ---+ Extensions
# ---++ DistributedServersPlugin
# **PERL**
# a hash of Wiki URL's that are transformed round robin style to the CDN Url's
# this is most useful for skin files - and should be avoided for any Web's containing 
# secured attachments
$TWiki::cfg{Plugins}{DistributedServersPlugin}{CDNMap} = {
    'http://t42p/trunk/pub/System/' => [
        'http://starfish.foswiki.org/foswiki.org/pub/System/'
    ],
    'http://twikifork.org/pub/System/' => [
        'http://starfish.foswiki.org/foswiki.org/pub/System/'
    ],
    'http://www.twikifork.org/pub/System/' => [
        'http://starfish.foswiki.org/foswiki.org/pub/System/'
    ],
    'http://foswiki.org/pub/System/' => [
        'http://starfish.foswiki.org/foswiki.org/pub/System/'
    ],
    'http://www.foswiki.org/pub/System/' => [
        'http://starfish.foswiki.org/foswiki.org/pub/System/'
    ]
};

1;
