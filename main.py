from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp
from graphene import Schema
from graphqls.queries import Query
from graphqls.mutations import Mutation

from db.database import get_client

# Define the GraphQL schema
schema = Schema(query=Query, mutation=Mutation)

# Create the FastAPI app
app = FastAPI()

# Integrate Graphene with FastAPI using Starlette
graphql_app = GraphQLApp(schema=schema)

# Mount the GraphQL app to the desired route
mongo_clinet=get_client
app.mount("/graphql", graphql_app)

# Run the API
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
