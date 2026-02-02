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
	Pass
}

func main() {
	// Register a handler for a URL pattern
	// http.handleFunc("/transactions", ...)

	// http.handleFunc("/transactions/chart", ...)

	// Listen and server on port 8080
	// Output confirmation
}
