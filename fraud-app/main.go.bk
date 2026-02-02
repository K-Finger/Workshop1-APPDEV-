package main

import (
	"encoding/json" // for decoding the request into a Go struct
	"fmt"
	"log"
	"net/http" // http package
	"os/exec"
	"time"
)

type Transaction struct {
	UserID    string  `json:"user_id"`
	Price     float64 `json:"price"`
	Timestamp string  `json:"timestamp"`
}

var transactions = []Transaction{} // Initialize a dynamic array (slice) as empty 

// --------------------------------------------------------------- //

// Middleware
func logRequest(handler http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		start := time.Now()
		log.Printf("%s %s", r.Method, r.URL.Path)
		handler(w, r)
		log.Printf("Completed in %v", time.Since(start))
	}
}

func main() {
	// Register a handler for a URL pattern
	http.HandleFunc("/transactions", logRequest(func(w http.ResponseWriter, r *http.Request) { // Pass by reference. Request struct too big
		if r.Method == "POST" {
			var t Transaction
			json.NewDecoder(r.Body).Decode(&t) // JSON encoding and decoding
			transactions = append(transactions, t)
			json.NewEncoder(w).Encode(t)
		} else {
			json.NewEncoder(w).Encode(transactions) // Send transactions to the client using a response writer
		}
	}))

	http.HandleFunc("/transactions/chart", logRequest(func(w http.ResponseWriter, r *http.Request) {
		cmd := exec.Command("python", "charting.py")
		err := cmd.Run()
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError) // 500 status code if cmd fails.
			return
		}
		w.Header().Set("Content-Type", "image/png") // No png exists? ServeFile returns 404
		http.ServeFile(w, r, "chart.png")
	}))

	fmt.Println("Server running on :8080")
	http.ListenAndServe(":8080", nil)
}
