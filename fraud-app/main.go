package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os/exec"
	"time"
)

type Transaction struct {
	UserID    string  `json:"user_id"`
	Price     float64 `json:"price"`
	Timestamp string  `json:"timestamp"`
}

var transactions = []Transaction{}

func logRequest(handler http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		start := time.Now()
		log.Printf("%s %s", r.Method, r.URL.Path)
		handler(w, r)
		log.Printf("Completed in %v", time.Since(start))
	}
}

func main() {
	http.HandleFunc("/transactions", logRequest(func(w http.ResponseWriter, r *http.Request) {
		if r.Method == "POST" {
			var t Transaction
			json.NewDecoder(r.Body).Decode(&t)
			transactions = append(transactions, t)
			json.NewEncoder(w).Encode(t)
		} else {
			json.NewEncoder(w).Encode(transactions)
		}
	}))

	http.HandleFunc("/transactions/chart", logRequest(func(w http.ResponseWriter, r *http.Request) {
		cmd := exec.Command("python", "charting.py")
		err := cmd.Run()
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		w.Header().Set("Content-Type", "image/png")
		http.ServeFile(w, r, "chart.png")
	}))

	fmt.Println("Server running on :8080")
	http.ListenAndServe(":8080", nil)
}
