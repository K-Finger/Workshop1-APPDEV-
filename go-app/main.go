package main

import (
	"fmt"
	"go-app/items"
	"log"
	"net/http"
)

func main() {
	mux := http.NewServeMux()

	// Keeps routing logic inside items package.
	// If we want to remove items functionality, simply remove this.
	items.SetupRoutes(mux)

	// Serve the swagger spec and docs UI
	mux.HandleFunc("/swagger.yaml", func(w http.ResponseWriter, r *http.Request) {
		http.ServeFile(w, r, "swagger.yaml")
	})
	mux.HandleFunc("/docs", func(w http.ResponseWriter, r *http.Request) {
		http.ServeFile(w, r, "docs.html")
	})

	fmt.Println("Server running on :8080")
	fmt.Println("Swagger UI: http://localhost:8080/docs")
	log.Fatal(http.ListenAndServe(":8080", mux))
}
