== Introduction

Sugar is a simple blood sugar test log application.  It provides a
simple mobile device optimized form to input your test results quickly
and easily, and then provides a graphical chart of the results.  It is
intended for a single user, and doesn't include any sort of user
authentication because it both doesn't contain any personal
information and it is intended to be quick to use and logging in takes
time.

The application is written in Rails 3, the UI utilizes {jQuery
Mobile}[link:http://jquerymobile.com] and the charting is done using
{Highcharts JS}[link:http://highcharts.com/].




== Install

 git clone git@github.com:pothoven/sugar.git
 cd sugar

== Run locally

 bundle install
 rake db:migrate
 rails server

== Run on Heroku

 gem install heroku
 heroku create
 git push heroku master
 heroku rake db:migrate
 heroku open

== Update

 git pull
 git push heroku master
