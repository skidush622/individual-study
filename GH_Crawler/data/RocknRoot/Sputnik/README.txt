# Sputnik

Pastebin

* Public install : http://sputnik.rocknroot.org
* Version : 1.0

Code is free, so if you're paranoid, you can install it at home or in that little private internet
of yours. Or just participate to the development. Fork us !

## Requirements

You need some dependencies like ruby, rubygems on your system.

Tested with Ruby :

* 1.8.7
* 1.9.2
* 1.9.3
* 2.0.0

## Installation

We asume that you already have a web server capable of running Rack applications (keywords
: Apache, nginx, mod_passenger, ...).

    $ git clone git://github.com/RocknRoot/Sputnik.git sputnik
    $ cd sputnik
    $ gem install bundler
    $ bundle install

### Troubleshooting

If you have problems to run Sputnik (Database connect error, read only db, etc.), ensure that the db directory is owned by corresponding http user (www, www-data, nobody, etc.).

## Configuration

You need configure sessions in app/app.rb:

```ruby
set :sessions,
      :key          => 'BL4BL4BL4',
      :secret       => 'a_fr4k1ng_gr34t_s3cr3t',
      :expire_after => 3600
```

And Recaptcha system. Please create an account with recaptcha.

```ruby
use Rack::Recaptcha, :public_key => 'pub_key_corresponding_your_domain',
                     :private_key => 'priv_key_corresponding_your_domain'
helpers Rack::Recaptcha::Helpers
```

## Configuration with Zomburl

If you run Zomburl on your server, you can short your paste urls with it.

Look at config directory. You have to fill infos located in settings.yml file.

Needed informations are:

* zomburl - HTTP url of your zomburl instance
* hostname - HTTP url of your sputnik instance

In Sputnik app directory:

    $ mv config/settings.yml.example config/settings.yml
    $ vi config/settings.yml # Edit your configuration file with needed informations

## Running Sputnik

If you're in development mode, you can test sputnik with embedded web server with:

    $ rackup config.ru # assuming you're in Sputnik app directory

Or with passenger (on nginx), for your vhost configuration:

    server {
        listen   80;
        server_name  fraking-great.url.com;
        root  /var/www/sputnik_app_directory/public;
        passenger_enabled on;
        passenger_base_uri /;
    }

## Need help ?

Add an issue on github ! ;)

or

Join us with jabber on: support@rootfest.rocknroot.org

## License

DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
       Version 2, December 2004

Copyright (C) 2012 Thibaut Deloffre

Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.

DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

0. You just DO WHAT THE FUCK YOU WANT TO.
