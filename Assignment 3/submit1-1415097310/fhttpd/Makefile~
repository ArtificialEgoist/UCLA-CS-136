project : webserver.c

webserver.c : server/webserver.c
	gcc -g -o server/webserver -lpthread  -lnsl -lresolv -D_TS_ERRNO server/webserver.c
install :
	sudo /etc/init.d/fhttpd.init stop
	sudo rm /usr/local/fhttpd/fhttpd
	sudo cp server/webserver /usr/local/fhttpd/fhttpd
	sudo chmod 4755 /usr/local/fhttpd/fhttpd
	sudo /etc/init.d/fhttpd.init start

clean : 
	rm server/webserver
