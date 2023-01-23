# PHP Code snippets

In order to run the snippets use the following commands(Please make sure to have PHP installed see [install php](https://phptherightway.com/#mac_setup)):

* Build the docker image: `docker build . -t php`
* Run the developement server with with `docker run --name=php -p=3000:3000 php`

Then navigate to `http://localhost:3000/<file_name>.php` to run the specific file.

Should you make a change, i.e add a file for experimentation you need to delete and rebuild the image:

* Identify the container with `docker ps -a`
* Then if it's ok for you to remove the container named php, simply run `docker container rm <container_id>`, where `<container_id>` is the container id that you just got in the list. You can then build and run the server again.
