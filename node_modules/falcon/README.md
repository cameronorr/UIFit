Falcon Framework
======
Kohana inspired web development framework

## The animal
The Peregrine Falcon is renowned for its speed, reaching over 322 km/h (200 mph) during its characteristic hunting stoop (high speed dive), making it the fastest member of the animal kingdom.

## #falcon.js IRC Channel at freenode.net


## Module Structure
    
    .
    |-- classes
    |   |-- controllers
    |   |   |-- admin
    |   |   |   |-- categories_controller.js
    |   |   |   |-- posts_controller.js
    |   |   |   `-- tags_controller.js
    |   |   |-- comments_controller.js
    |   |   `-- posts_controller.js
    |   |-- models
    |   |   |-- category.js
    |   |   |-- post.js
    |   |   `-- tag.js
    |   |-- views
    |   |   |-- admin
    |   |   |   `-- posts
    |   |   |       |-- edit.jade
    |   |   |       |-- index.jade
    |   |   |       |-- new.jade
    |   |   |-- layouts
    |   |   |   `-- application_layout.jade
    |   |   |-- partials
    |   |   `-- posts
    |   |       |-- index.jade
    |   |       `-- show.jade
    |   `-- helpers
    |       |-- admin
    |       |   |-- posts_helper.js
    |       |   `-- tags_helper.js
    |       `-- posts_helper.js
    `-- config
        |-- database.json
        |-- routes.js
        |-- tsl.cert
        `-- tsl.key