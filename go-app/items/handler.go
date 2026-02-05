package items

import (
	"encoding/json"
	"go-app/api"
	"net/http"
	"strconv"
)

// In-memory store — resets when server restarts
var items = []string{}

// SetupRoutes registers the /items route on the given router
func SetupRoutes(mux *http.ServeMux) {
	mux.HandleFunc("/items", handleItems)
}

// handleItems is the entry point for all /items requests.
// Go's ServeMux only routes by path, not by method,
// This is better code practice because it keeps SetupRoutes from doing two things: registering and routing
func handleItems(w http.ResponseWriter, r *http.Request) {
	switch r.Method {
	case http.MethodGet:
		getItems(w, r)
	case http.MethodPost:
		createItem(w, r)
	case http.MethodPut:
		updateItem(w, r)
	case http.MethodDelete:
		deleteItem(w, r)
	default:
		api.WriteError(w, http.StatusMethodNotAllowed, "method not allowed", nil)
	}
}

func getItems(w http.ResponseWriter, r *http.Request) {
	api.WriteSuccess(w, http.StatusOK, items)
}

func createItem(w http.ResponseWriter, r *http.Request) {
	var body CreateItemRequest // pulls the request format from models.go

	if err := json.NewDecoder(r.Body).Decode(&body); err != nil {
		api.WriteError(w, http.StatusBadRequest, "invalid JSON", err)
		return
	}

	if body.Item == "" {
		api.WriteError(w, http.StatusBadRequest, "item cannot be empty", nil)
		return
	}

	items = append(items, body.Item)
	api.WriteSuccess(w, http.StatusCreated, items)
}

// PUT /items?index=0
func updateItem(w http.ResponseWriter, r *http.Request) {
	indexStr := r.URL.Query().Get("index")
	index, err := strconv.Atoi(indexStr)

	if err != nil || index < 0 || index >= len(items) {
		api.WriteError(w, http.StatusBadRequest, "invalid index", err)
		return
	}

	var body CreateItemRequest
	if err := json.NewDecoder(r.Body).Decode(&body); err != nil {
		api.WriteError(w, http.StatusBadRequest, "invalid JSON", err)
		return
	}
	if body.Item == "" {
		api.WriteError(w, http.StatusBadRequest, "item cannot be empty", nil)
		return
	}

	items[index] = body.Item
	api.WriteSuccess(w, http.StatusOK, items)
}

// DELETE /items — always returns an error to demonstrate how api.WriteError works
func deleteItem(w http.ResponseWriter, r *http.Request) {
	api.WriteError(w, http.StatusBadRequest, "this always fails on purpose", nil)
}
