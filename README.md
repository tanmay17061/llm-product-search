# LLM e-Commerce Product Search
Utilize LLM vectorizer, vector database and LLM summarizer to retrieve most relevant products to a user query.
Uses langchain under the hood to enable this pipeline.

## Product Roadmap

## v1

1. Indexer: indexes product descriptions in a vector store.
2. User query fetches a static relevant product list.
3. Product Summarizer: User is presented with this list with a reasoning for each product match.

## v2

1. The (User <-> Product) interaction is a conversation. The Product Summarizer is now a conversation agent, capable of re-fetching products if the user updates their query.
