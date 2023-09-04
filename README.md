# LLM e-Commerce Product Search
Utilize LLM vectorizer, vector database and LLM summarizer to retrieve most relevant products to a user query.
Uses langchain under the hood to enable this pipeline.

## Product Roadmap

## v1

1. Indexer: indexes product descriptions in a vector store.
2. User query fetches a static relevant product list.
3. Product Summarizer: User is presented with this list with a reasoning for each product match.

## v2

1. The (User <-> Product) interaction is a conversation. The Product Summarizer is now a conversation agent (or, a chatbot), capable of re-fetching products if the user updates their query.

## v3

1. It will be fun to see if the chatbot can handle vector arithmetic. An example conversation would be:  
  a. Human: I am looking for a slow cooker. Can you suggest any good ones?  
  b. Chatbot: <vectorizes user query; queries and fetches the vector store for relevant products>  
  c. Chatbot: Sure! Here are 3 suggestions, ...  
  d. Human: But all of these do not have induction support. It should have induction support.  
  e. Chatbot: <vectorizes user query; vectorizes "should have induction support" and adds to the previous vector>  
  f. Chatbot: Oops, my bad. Here, these 3 suggestions come with an induction bottom: ...  