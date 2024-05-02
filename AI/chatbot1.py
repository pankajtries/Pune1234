import random

# Responses to greetings
GREETING_RESPONSES = ["Hello! Welcome to our online store. How can I assist you today?", 
                      "Hi there! How can I help you with your shopping experience?", 
                      "Greetings! What can I do to make your shopping experience better?"]

# Responses to user inputs
RESPONSES = {
    "products": "We sell a variety of products including electronics, clothing, home goods, and more. Feel free to browse our online catalog to see our full selection!",
    "track_order": "You can track your order by logging into your account on our website and navigating to the 'Order History' section. From there, you can view the status and tracking information for your orders.",
    "delivery_time": "The delivery time depends on your location and the shipping method selected. Generally, orders are processed and shipped within 1-2 business days, and delivery typically takes 3-5 business days within the continental United States.",
    "international_shipping": "Yes, we offer international shipping to select countries. Shipping rates and delivery times vary depending on the destination. You can view the available shipping options during checkout.",
    "return_item": "If you're not satisfied with your purchase, you can initiate a return within 30 days of delivery. Please contact our customer service team for assistance with the return process. We'll provide you with a return authorization and instructions for returning the item.",
    "return_policy": "Our return policy allows for returns within 30 days of delivery for a full refund or exchange. Items must be returned in their original condition with all tags and packaging intact. Please note that certain items may be subject to restocking fees.",
    "contact_support": "You can contact our customer support team by phone at 1-800-123-4567 or by email at support@example.com. Our representatives are available to assist you Monday through Friday, 9:00 AM to 5:00 PM EST.",
    "promotions": "We frequently offer promotions and discounts on select products. You can sign up for our newsletter or follow us on social media to stay updated on the latest deals and offers.",
    "default": "I'm sorry, I didn't understand that. Can you please rephrase or ask a different question?"
}

def get_response(user_input):
    """
    Function to generate a response based on user input.
    """
    user_input = user_input.lower()

    if "products" in user_input:
        return RESPONSES["products"]
    elif "track" in user_input or "order" in user_input:
        return RESPONSES["track_order"]
    elif "delivery" in user_input or "arrive" in user_input:
        return RESPONSES["delivery_time"]
    elif "international" in user_input or "shipping" in user_input:
        return RESPONSES["international_shipping"]
    elif "return" in user_input or "item" in user_input:
        return RESPONSES["return_item"]
    elif "policy" in user_input:
        return RESPONSES["return_policy"]
    elif "contact" in user_input or "support" in user_input:
        return RESPONSES["contact_support"]
    elif "promotion" in user_input or "discount" in user_input:
        return RESPONSES["promotions"]
    elif any(greeting in user_input for greeting in ["hello", "hi", "hey"]):
        return random.choice(GREETING_RESPONSES)
    else:
        return RESPONSES["default"]

def main():
    print("Welcome to our online store! How can I assist you today?")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Thank you for visiting our store. Have a great day!")
            break

        response = get_response(user_input)
        print("Bot:", response)

if _name_ == "_main_":
    main()
