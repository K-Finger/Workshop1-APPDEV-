package main

// STARTUP
// go mod init fraud-app
// go mod tidy
// go run . (start server)

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
// It takes in a handler and returns a new handler. 
// The new handler does everything the original does, plus logging.
func logRequest(handler http.HandlerFunc) http.HandlerFunc {
	pass
}

func main() {
	// Register a handler for getting all transactions as JSON
	// http.handleFunc("/transactions", ...)



	// Handler for getting the chart
	http.HandleFunc("/transactions/chart", func(w http.ResponseWriter, r *http.Request) {
		cmd := exec.Command("python", "charting.py")
		err := cmd.Run()

		//handle error
		if err != nil {
			// http.Error and include ResponseWriter, err.Error(), and status code
			// Make sure the code doesn't continue!
		}

		// Set content type to image & serve
		w.Header().Set("Content-Type", "image/png")
		http.ServeFile(w, r, "chart.png")
	})
	

	// Output confirmation
	fmt.Println("Server Running on :8080")

	// Listen and server on port 8080
	// ...
}
