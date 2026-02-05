package items

// CreateItemRequest is the expected JSON body for POST and PUT
type CreateItemRequest struct {
	Item string `json:"item"`
}
