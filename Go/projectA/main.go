package main

import "net/http"
import "log"

func main() {
	http.HandleFunc("/", func(http.ResponseWriter, *http.Request) {
		log.Println("This is my web server")
	})
	
	http.ListenAndServe("127.0.0.1:8080", nil)
}